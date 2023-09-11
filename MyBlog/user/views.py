from datetime import datetime, timedelta
from random import choices
from time import time
from django.contrib.auth.hashers import check_password
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.cache import cache
from blog.views import search
from user.models import User, ChatRecord
from blog.models import Blog
from user.serializers import UserSerializers
from utils.message_service import send_message
from django.contrib.auth import login, logout
from common.views import common_data
from rest_framework import viewsets
# 在登录中往往都需要使用post请求，在使用该请求是，需要进行csrf_token的验证，通过该验证有3中方法
'''
1.在settings的MIDDLEWARE中注释掉csrf验证的中间件
2.在模板的form表单中添加{%csrf_token%}
3.使用装饰器获取豁免权:在视图函数的上一行使用装饰器:@csrf_exempt
'''

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    queryset = User.objects.all()

    # 注册
    # @cache_page(timeout=60, cache='default')
    def register(self,request,*args,**kwargs):

        forgetPwd = request.POST.get('forgetPwd')

        # 监测手机号是否格式正确
        if not User.is_valid_mobile(mobile):
            return JsonResponse({
                'code': '400',
                'msg': '手机号码格式不正确!'
            })

        # 如果不是修改密码就检测手机号是否已注册
        if not forgetPwd and User.get_by_mobile(mobile):
            return JsonResponse({
                'code': '400',
                'msg': '该手机号已注册!'
            })

        # 存在本地的验证码
        local_code = cache.get(f'{mobile}-code')
        if not local_code:
            return JsonResponse({
                'code': '400',
                'msg': '验证码已过期,请重新发送!'
            })

        if code != local_code:
            return JsonResponse({
                'code': '400',
                'msg': '验证码错误!'
            })

        if forgetPwd:  # 如果是进行密码修改就不需要更新用户名
            tmp_user = User.get_by_mobile(mobile)
            tmp_user.update(tmp_user.mobile, tmp_user.username, password)  # 更新user
            return JsonResponse({
                'code': '200',
                'msg': '密码修改成功!'
            })

        # 注册
        user = User.create_user(mobile=mobile, password=password)

        # 通知
        content = f'亲爱的{user.username}:<br>欢迎来到0318-SPACE,在这里,博主会不定期更博客,学习心得,知识点等等,和大家一起学习,' \
                  f'如果您也想在本站发布,只需提交申请理由后,待管理员授权即可。欢迎大家积极申请!!!<br><br><br>&nbsp;&nbsp;&nbsp;' \
                  f'&nbsp;&nbsp;&nbsp;---LLL'

        sender = User.get_by_id('1')
        ChatRecord.create_record(sender, user, content)
        return JsonResponse({
            'code': '200',
            'msg': '注册成功!'
        })


# 发送验证码
def send_code(request):
    if request.method == 'POST':

        # 用户的手机号码
        mobile = request.POST.get('mobile', '')

        # 检测手机号是否格式正确
        if not User.is_valid_mobile(mobile):
            return JsonResponse({
                'code': '400',
                'msg': '手机号码格式不正确!'
            })

        action = request.POST.get('action', '')
        if action == 'register':
            if User.get_by_mobile(mobile):
                return JsonResponse({
                    'code': '400',
                    'msg': '该手机号已注册!'
                })

        # 获取今天发送短信的次数
        use_count = cache.get(mobile, 0)
        if use_count >= 3:
            return JsonResponse({
                'code': '400',
                'msg': '一天最多可发送3次短信!'
            })

        # 随机验证码
        local_code = ''.join(map(str, choices(range(9), k=4)))

        # 发送短信
        send_success = send_message(phoneNumber=mobile, code=local_code)
        if send_success:
            # 保存当前手机号码的验证码 时效5分钟
            cache.set(f'{mobile}-code', local_code, 60 * 5)

            # 计算当前距离明天的时间 每天只能发送3次短信
            now = datetime.now()
            expired = (timedelta(hours=24, minutes=0, seconds=0) - timedelta(hours=now.hour, minutes=now.minute,
                                                                             seconds=now.second)).seconds
            cache.set(mobile, use_count + 1, expired)

            # 60秒内只能发送一次验证码
            cache.set(f'{mobile}-send', time(), 60)

            return JsonResponse({
                'code': '200',
                'msg': '验证码已发送至您的手机,请注意查收!'
            })
        else:
            return JsonResponse({
                'code': '400',
                'msg': '验证码发送失败!'
            })




# 缓存的使用 登录
# @cache_page(timeout=60, cache='default')  # timeout指定缓存过期时间,cache指定缓存用的数据库，
def my_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')

    if request.method == 'POST':
        username = request.POST.get('username')  # 用户名或者手机号
        password = request.POST.get('password')
        tmp_user = User.get_by_username(username)

        # 检查用户是否存在
        if not tmp_user:
            return JsonResponse({
                'code': '400',
                'msg': '用户名/手机不存在!'
            })

        # 检查密码是否正确
        if not check_password(password, tmp_user.password):  # 参数顺序:明文 密文
            return JsonResponse({
                'code': '400',
                'msg': '密码错误!'
            })

        # django自带的登录
        login(request, tmp_user)

        return JsonResponse({
            'code': '200',
            'msg': '登录成功!'
        })


# 退出登录
def my_logout(request):
    logout(request)
    return redirect(reverse('user:index'))


# 忘记密码
def forget_password(request):
    if request.method == 'GET':
        action = 'forgetpwd'
        return render(request, 'forgetPassword.html', context={'action': action})


# 博客首页
def index(request):
    if request.method == 'GET':
        keyword = request.GET.get('keyword', '')[:20]
        category = request.GET.get('category', '')
        tag = request.GET.get('tag', '')

        # 分页
        page, page_dict, blog_list, placeholder = search(request)

        context = {
            'keyword': keyword,
            'category': category,
            'tag': tag,
            'page': page,
            'page_dict': page_dict,
            'blog_list': blog_list,
            'placeholder': placeholder
        }
        context.update(common_data(request))
        return render(request, 'index.html', context=context)


# 个人中心 #数据的管理使用admin来代替 个人中心完成个人资料 私信聊天功能即可
def personal_center(request, user_id):
    # 没有登录就直接跳转到首页
    if not request.user.is_authenticated:
        return redirect(reverse('/'))

    if request.method == 'GET':
        user = User.get_by_id(user_id)
        isManager = user.is_superuser  # 查看该用户是否是管理者

        blogObj = Blog.objects.all()
        blogNum = blogObj.count()  # 博客数量

        # 返回通知的数据
        # 未读的通知数量

        return render(request, 'personalCenter.html', context=locals())
