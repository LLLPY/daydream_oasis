import time
from django.core.cache import cache
from django.http import JsonResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.urls import reverse
from django.utils.deprecation import MiddlewareMixin
from log.models import Error, RequestRecord
from log.logger import logger
import uuid
import re

'''
中间件的基本流程:
1.在工程目录下创建一个middleware目录
2.在middleware中创建一个Python文件
3.在这个Python文件中创建一个类，继承自django内置的中间件MiddlewareMixin
4.注册，在工程的配置文件settings中找到MIDDLEWARE的配置，将这个类的路径添加到MIDDLEWARE列表里面
5.封装类方法
'''


class MyMiddleWare(MiddlewareMixin):

    def process_request(self, request):
        # return HttpResponse('后台维护，暂停访问...')

        start_time = time.time()
        path = request.path

        if path.find('sendCode') != -1:
            return HttpResponseBadRequest('!')

        ip = request.META.get('REMOTE_ADDR', '')  # 客户端的ip地址
        request.start_time = start_time
        method = request.method
        user_agent = request.META.get('HTTP_USER_AGENT')
        http_refer = request.META.get('HTTP_REFERER', '')
        os = request.META.get('OS', '')
        computer_name = request.META.get('COMPUTERNAME', '')
        _username = request.META.get('USERNAME', '')

        # 获取ip的位置信息 TODO先将ip的基本信息写入，后期再启动定时任务对ip的地址进行更新
        # country, province, city = RequestRecord.get_address(ip)
        request_log = {
            'path': path,
            'method': method,
            'ip': ip,
            'user_agent': user_agent,
            'http_refer': http_refer,
            'os': os,
            'country': '',
            'province': '',
            'city': '',
            'computer_name': computer_name,
            'username': _username

        }

        request.request_log = request_log

        res = None
        # 实现限制某个时间段内的访问次数(例:1分钟内只能访问200次)
        ip_list = cache.get(ip, [])
        # 时间限制在1分钟 (比较最新的请求和最早的请求的时间差，如果大于60秒，则踢出最早的请求)
        # 如果ip列表的长度大于200，就处于封禁状态，就不能进行pop操作
        while ip_list and time.time() - ip_list[-1] > 60 and len(ip_list) < 200:
            ip_list.pop()

        # # 最新的请求添加到请求列表的头部，那么最早的请求就在列表的尾部
        ip_list.insert(0, time.time())
        # 将请求列表保存在缓存中
        if len(ip_list) <= 200:
            cache.set(ip, ip_list, timeout=60)

        elif len(ip_list) <= 300:
            cache.set(ip, ip_list, timeout=60 * 30)  # 封禁30分钟
            res = {
                'code': '400',
                'msg': '喝杯茶休息一下吧!'
            }
            logger.warning(
                f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden for 0.5 hours...')

        elif len(ip_list) <= 500:
            cache.set(ip, ip_list, timeout=60 * 60 * 2)  # 封禁两个小时
            res = {
                'code': '400',
                'msg': '看个电影再来吧!'
            }
            logger.warning(
                f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden for 2 hours...')

        elif len(ip_list) <= 800:
            cache.set(ip, ip_list, timeout=60 * 60 * 24)  # 封禁一天
            res = {
                'code': '400',
                'msg': '不早了，睡觉觉吧!'
            }
            logger.warning(
                f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden for 1 day...')

        else:
            cache.set(ip, ip_list)  # 永久封禁
            res = {
                'code': '400',
                'msg': '对不起,是我们缘分不够!'
            }
            logger.warning(
                f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden forever...')

        # 如果用户登录了就进行用户位置的更新
        if request.user.is_authenticated:
            user = request.user
            longitude = request.GET.get('longitude') or request.POST.get('longitude')
            latitude = request.GET.get('latitude') or request.POST.get('latitude')
            user.update_location(longitude, latitude)
            request.user = user

        # 个性推荐
        user = request.user.id if request.user.is_authenticated else request.COOKIES.get('uuid', '-')
        if not cache.has_key(f'{user}_recommend_list'):
            user_recommend_queue = cache.get('user_recommend_queue') or []
            if user not in user_recommend_queue:
                user_recommend_queue.insert(0, user)
            cache.set('user_recommend_queue', user_recommend_queue)

        return JsonResponse(res) if res else None

    def process_response(self, request, response):

        # 生成的uuid来标识
        _uuid = request.COOKIES.get('uuid')
        if not _uuid:
            _uuid = str(uuid.uuid4())
            response.set_cookie('uuid', _uuid)

        return response

    # 界面友好化处理(当服务器出现异常，状态码为500时，为了不让用户知道服务器的故障，可以使用中间件对此进行处理)
    # def process_exception(self, request, exception):
    #     error = Error()
    #     error.request_log = request.request_log
    #     error.reason = str(exception)
    #     error.save()
    #
    #     if request.method == 'POST':
    #         return JsonResponse({
    #             'code': '500',
    #             'msg': '抱歉,遇到了未知错误!'
    #         })
    #
    #     # 如果报错，将页面重定向到指定页面
    #     return render(request, '404.html')
