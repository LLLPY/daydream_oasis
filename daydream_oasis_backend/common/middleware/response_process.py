# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/10/14 13:26  
import uuid

from django.utils.deprecation import MiddlewareMixin

from utils import tools
from utils.cache import redis_conn


class ResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # 生成的uuid来标识
        uid = request.COOKIES.get('uuid') or uuid.uuid4().hex

        # 只要响应成功就更新超时时间
        response.set_cookie('uuid', uid, samesite='', secure='', httponly='')

        # 更新登录状态
        auth_token = request.get_signed_cookie('auth_token', default='', salt=tools.md5('daydream_oasis'))
        user_id = redis_conn.get(auth_token)
        if auth_token and user_id:
            # cookie过期时间更新
            response.set_signed_cookie('auth_token', auth_token, salt=tools.md5('daydream_oasis'),
                                       max_age=3600 * 24 * 7,
                                       samesite='', secure='', httponly='')
            # 缓存过期时间更新
            redis_conn.expire(auth_token, 3600 * 24 * 7)

        # 更新请求的状态
        request_record = getattr(request, 'request_record', None)
        if request_record:
            # 失败的请求
            if getattr(response, 'CODE', '0') != '0':
                fail_detail = response.data.get('fail_detail') or response.data.get('message')
                extra = request_record.extra
                extra['fail_detail'] = fail_detail
                status = request_record.FAIL
            else:
                status = request_record.SUCCESS
            request_record.status = status
            request_record.save()

        return response
