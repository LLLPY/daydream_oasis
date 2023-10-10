import time
from django.core.cache import cache
from django.http import HttpResponseBadRequest
from django.utils.deprecation import MiddlewareMixin
from log.models import Error, RequestRecord
from log.logger import logger
import uuid
from utils import tools
from .rate_limit_middleware import RateLimitMixin

'''
中间件的基本流程:
1.在工程目录下创建一个middleware目录
2.在middleware中创建一个Python文件
3.在这个Python文件中创建一个类，继承自django内置的中间件MiddlewareMixin
4.注册，在工程的配置文件settings中找到MIDDLEWARE的配置，将这个类的路径添加到MIDDLEWARE列表里面
5.封装类方法
'''


class MyMiddleWare(RateLimitMixin, MiddlewareMixin):

    def process_request(self, request):
        super().process_request(request)
        print(11111, request.get_signed_cookie('user_id', default=None, salt=tools.md5('daydream_oasis')))
        print(2222, request.COOKIES)
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

        # 个性推荐
        user = request.user.id if request.user.is_authenticated else request.COOKIES.get('uuid', '-')
        if not cache.has_key(f'{user}_recommend_list'):
            user_recommend_queue = cache.get('user_recommend_queue') or []
            if user not in user_recommend_queue:
                user_recommend_queue.insert(0, user)
            cache.set('user_recommend_queue', user_recommend_queue)

    def process_response(self, request, response):

        # 生成的uuid来标识
        _uuid = request.COOKIES.get('uuid')
        if not _uuid:
            _uuid = str(uuid.uuid4())
            response.set_cookie('uuid', _uuid)

        # 处理跨域问题
        headers = response.headers or {}
        headers['Access-Control-Expose-Headers'] = 'set-cookie'
        headers['Access-Control-Allow-Credentials'] = 'true'
        response.headers = headers
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
