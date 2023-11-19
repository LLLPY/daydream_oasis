from datetime import datetime, timedelta
from random import choices
from django.contrib.auth.hashers import check_password
from user.models import User, ChatRecord
from user.serializers import UserSerializers
from utils.message_service import send_message
from django.contrib.auth import logout as default_logout
from common.exception import exception
from rest_framework.decorators import action
from common.drf.response import SucResponse
from common.views import BaseViewSet
from utils import tools

# 在登录中往往都需要使用post请求，在使用该请求是，需要进行csrf_token的验证，通过该验证有3中方法
'''
1.在settings的MIDDLEWARE中注释掉csrf验证的中间件
2.在模板的form表单中添加{%csrf_token%}
3.使用装饰器获取豁免权:在视图函数的上一行使用装饰器:@csrf_exempt
'''


class UserViewSet(BaseViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()

    # 注册
    @action(methods=['post'], detail=False)
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get('mobile')
        code = serializer.data.get('code')

        # 比较验证码是否正确
        local_code = self.redis_conn.get(f'register:code:{mobile}')
        if not local_code:
            raise exception.CustomValidationError('验证码已过期,请重新发送!')

        if code != local_code:
            raise exception.CustomValidationError('验证码错误!')

        # 检测手机号是否已注册
        if User.get_by_mobile(mobile):
            raise exception.CustomValidationError('该手机号已注册!')

        # 注册
        password = ''
        user = User.create_user(mobile=mobile, password=password)

        # 通知
        content = f'亲爱的{user.username}:<br>欢迎来到0318-SPACE,在这里,博主会不定期更博客,学习心得,知识点等等,和大家一起学习,' \
                  f'如果您也想在本站发布,只需提交申请理由后,待管理员授权即可。欢迎大家积极申请!!!<br><br><br>&nbsp;&nbsp;&nbsp;' \
                  f'&nbsp;&nbsp;&nbsp;---LLL'

        sender = User.get_by_id('1')
        ChatRecord.create_record(sender, user, content)
        return SucResponse('注册成功!')

    @action(methods=['post'], detail=True)
    def modify_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get('mobile')
        code = serializer.data.get('code')
        password = serializer.data.get('password')

        # 比较验证码是否正确
        local_code = self.redis_conn.get(f'modify_password:code:{mobile}')
        if not local_code:
            raise exception.CustomValidationError('验证码已过期,请重新发送!')

        if code != local_code:
            raise exception.CustomValidationError('验证码错误!')

        # 检测手机号是否已注册
        if not User.get_by_mobile(mobile):
            raise exception.CustomValidationError('手机号不存在!')

        tmp_user = User.get_by_mobile(mobile)
        tmp_user.update_password(password)
        return SucResponse('密码修改成功!')

    # 登录
    @action(methods=['post'], detail=False)
    def login(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data, include_fields=['username', 'password', 'code'])
        serializer.is_valid(raise_exception=True)

        username = serializer.data.get('username')  # 用户名
        # mobile = serializer.data.get('mobile')  # 手机号
        password = serializer.data.get('password')
        tmp_user = User.get_by_username(username)

        # 检查用户是否存在
        if not tmp_user:
            raise exception.CustomValidationError('用户不存在!')

        # 检查密码是否正确
        if not check_password(password, tmp_user.password):  # 参数顺序:明文 密文
            raise exception.CustomValidationError('密码错误!')

        res = SucResponse('登录成功!')
        res.set_signed_cookie('user_id', tmp_user.id, salt=tools.md5('daydream_oasis'), max_age=3600 * 24 * 7,
                              samesite='None', secure=False)
        # raise exception.CustomValidationError('')
        return res

    # 发送验证码
    @action(methods=['post'], detail=False)
    def send_code(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get('mobile')
        action = serializer.data.get('action')
        verify_code = serializer.data.get('code')  # 验证码

        local_verify_code = self.redis_conn.get(f'verify_code:{mobile}')
        if verify_code != local_verify_code:
            raise exception.CustomValidationError('验证码不正确!')

        # 判断验证码是否已发送 5分钟内只能发一次
        key = f'{action}:code:{mobile}'

        # 随机验证码
        local_code = ''.join(map(str, choices(range(9), k=4)))
        success = self.redis_conn.setnx(key, local_code)
        if not success:
            raise exception.CustomValidationError(f'验证码已发送,距离下次可发送时间为:{self.redis_conn.ttl(key)}s')

        # 设置过期时间
        self.redis_conn.expire(key, 60 * 5)

        if action == 'register':
            if User.get_by_mobile(mobile):
                raise exception.CustomValidationError('该手机号已注册!')

        # 获取今天发送短信的次数
        used_key = f'used:{mobile}'
        use_count = self.redis_conn.get(used_key, 0)
        if use_count >= 3:
            raise exception.CustomValidationError('一天最多可发送3次短信!')

        # 发送短信
        send_success = send_message(phoneNumber=mobile, code=local_code)
        if send_success:

            # 计算当前距离明天的时间 每天只能发送3次短信
            now = datetime.now()
            expired = (timedelta(hours=24, minutes=0, seconds=0) - timedelta(hours=now.hour, minutes=now.minute,
                                                                             seconds=now.second)).seconds
            self.redis_conn.set(used_key, use_count + 1)
            self.redis_conn.expire(used_key, expired)


            return SucResponse('验证码已发送至您的手机,请注意查收!')
        else:

            # 发送失败就删除验证码的缓存
            self.redis_conn.delete(key)
            raise exception.CustomValidationError('验证码发送失败!')

    # 退出登录
    @action(methods=['post'], detail=True)
    def logout(self, request, *args, **kwargs):
        default_logout(self.request)
        return SucResponse('退出登录成功!')
