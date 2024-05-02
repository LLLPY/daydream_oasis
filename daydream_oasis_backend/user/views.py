from datetime import datetime, timedelta
from random import choices

from common.drf.decorators import login_required
from common.drf.response import SucResponse
from common.exception import exception
from common.views import BaseViewSet
from django.conf import settings
from django.contrib.auth import logout as default_logout
from django.contrib.auth.hashers import check_password
from rest_framework.decorators import action
from user.models import User
from user.serializers import UserSerializers
from utils import tools
from utils.message_service import send_message

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
        serializer = self.get_serializer(data=self.request.data, include_fields=[
                                         'mobile', 'code', 'password'])
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get('mobile')
        code = serializer.data.get('code')
        password = serializer.data.get('password')

        # 比较验证码是否正确
        local_code = self.redis_conn.get(f'register:code:{mobile}')
        if not local_code:
            raise exception.CustomValidationError('验证码已过期,请重新发送!')

        if code != local_code.decode('utf-8'):
            raise exception.CustomValidationError('验证码错误!')

        # 检测手机号是否已注册
        if User.get_by_mobile(mobile):
            raise exception.CustomValidationError('该手机号已注册!')

        # 注册
        user = User.create_user(mobile=mobile, password=password)
        return SucResponse('注册成功!')

    @action(methods=['post'], detail=False)
    def modify_password(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data, include_fields=[
                                         'username', 'code', 'password'])
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get('username')
        code = str(serializer.data.get('code'))
        password = serializer.data.get('password')

        # 比较验证码是否正确
        local_code = self.redis_conn.get(f'forget:code:{mobile}')
        if not local_code:
            raise exception.CustomValidationError('验证码已过期,请重新发送!')
        if code != local_code.decode('utf-8'):
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
        serializer = self.get_serializer(
            data=self.request.data, include_fields=['username', 'password'])
        serializer.is_valid(raise_exception=True)

        username = serializer.data.get('username')  # 用户名
        password = serializer.data.get('password')
        tmp_user = User.get_by_username(username)

        # 检查用户是否存在
        if not tmp_user:
            raise exception.CustomValidationError('用户不存在!')

        # 检查密码是否正确
        if not check_password(password, tmp_user.password):  # 参数顺序:明文 密文
            raise exception.CustomValidationError('密码错误!')
        serializer = self.get_serializer(tmp_user, include_fields=['id', 'username', 'email', 'avatar'])
        res = SucResponse('登录成功!', data=serializer.data)
        auth_token = tools.md5(f'{tmp_user.id}_daydream_oasis')
        res.set_signed_cookie('auth_token', auth_token, salt=tools.md5('daydream_oasis'), max_age=settings.SESSION_COOKIE_AGE,
                              samesite='', secure='', httponly='')
        res.set_cookie('user_id', tmp_user.id, samesite='', secure='',
                       httponly='', max_age=settings.SESSION_COOKIE_AGE*1000)
        res.set_cookie('username', tools.char2ord(tmp_user.username), samesite='',
                       secure='', httponly='', max_age=settings.SESSION_COOKIE_AGE*1000)
        res.set_cookie('avatar', tools.char2ord(tools.get_full_media_url(
            tmp_user.avatar)), samesite='', secure='', httponly='', max_age=settings.SESSION_COOKIE_AGE*1000)
        # 登录信息写入缓存
        self.redis_conn.set(auth_token, tmp_user.id, settings.SESSION_COOKIE_AGE)

        return res

    # 发送验证码
    @action(methods=['post'], detail=False)
    def send_code(self, request, *args, **kwargs):

        uid = self.request.COOKIES.get('uuid')
        if not uid:
            raise exception.CustomValidationError('非法请求!')

        serializer = self.get_serializer(
            data=self.request.data, include_fields=['mobile', 'action'])
        serializer.is_valid(raise_exception=True)
        mobile = serializer.data.get('mobile')
        _action = serializer.data.get('action')

        if _action == 'register':
            if User.get_by_mobile(mobile):
                raise exception.CustomValidationError(f'{mobile}该手机号已注册!')

        # 判断验证码是否已发送 5分钟内只能发一次
        key = f'{_action}:code:{mobile}'

        # 随机验证码
        local_code = ''.join(map(str, choices(range(9), k=4)))
        success = self.redis_conn.setnx(key, local_code)
        if not success:
            raise exception.CustomValidationError(f'验证码已发送,距离下次可发送时间为:{self.redis_conn.ttl(key)}s')

        # 设置过期时间
        self.redis_conn.expire(key, 60 * 5)

        # 获取今天发送短信的次数
        used_key = f'used:{mobile}'
        use_count = int(self.redis_conn.get(used_key) or 0)
        if use_count >= 3:
            # 让验证码直接过期
            self.redis_conn.expire(key, 0)
            raise exception.CustomValidationError('一天最多可发送3次短信!')

        # 发送短信
        send_success = send_message(phone_number=mobile, code=local_code)
        if send_success:
            # 计算当前距离明天的时间 每天只能发送3次短信
            now = datetime.now()
            expired = (timedelta(hours=24, minutes=0, seconds=0) - timedelta(hours=now.hour, minutes=now.minute,
                                                                             seconds=now.second)).seconds
            self.redis_conn.set(used_key, use_count + 1, expired)
            return SucResponse('验证码已发送至您的手机,请注意查收!')
        else:
            # 发送失败就删除验证码的缓存
            self.redis_conn.delete(key)
            raise exception.CustomValidationError('验证码发送失败!')

    # 退出登录
    @action(methods=['post'], detail=False)
    def logout(self, request, *args, **kwargs):
        auth_token = request.get_signed_cookie(
            'auth_token', default='', salt=tools.md5('daydream_oasis'))
        self.redis_conn.delete(auth_token)
        default_logout(self.request)
        res = SucResponse('退出登录成功!')
        tools.delete_cookie(res)
        return res

    @action(methods=['get'], detail=False)
    @login_required
    def info(self, request, *args, **kwargs):
        '''用户信息'''
        serializer = self.get_serializer(request.user, include_fields=['username', 'avatar', 'id'])
        return SucResponse(data=serializer.data)

    @action(methods=['get'], detail=False)
    def email_demo(self, request, *args, **kwargs):
        ''''''
        email = 'yangjingge11555@qq.com'
        email = '2474605919@qq.com'
        message = '你好👋'

        blog_title = '《Python源码剖析》之PyTypeObject'
        blog_id = 1439
        operator_username = '白日梦想猿'
        tools.send_email(
            subject="新的评论通知！",
            message=message,
            blog_title=blog_title,
            blog_id=blog_id,
            operator_username=operator_username,
            recipient_list=[email],
            block=True
        )
        return SucResponse(message="邮件发送成功！")
