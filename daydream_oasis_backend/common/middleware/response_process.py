# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/10/14 13:26
import logging
import uuid

from django.conf import settings
from django.utils.deprecation import MiddlewareMixin
from utils import tools
from utils.cache import redis_conn

logger = logging.getLogger('daydream_oasis')


class ResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):

        # 生成的uuid来标识
        uid = request.COOKIES.get('uuid')
        if not uid:
            # 如果uid不存在就重新生成
            response.set_cookie('uuid', uuid.uuid4().hex, samesite='', secure='',
                                httponly='', max_age=settings.SESSION_COOKIE_AGE*1000)

        # 更新登录状态
        auth_token = request.get_signed_cookie('auth_token', default='', salt=tools.md5('daydream_oasis'))
        user_id = redis_conn.get(auth_token)
        logger.info(f'auth_token:{auth_token},user_id:{user_id}')
        if auth_token and user_id:
            # cookie过期时间更新
            response.set_signed_cookie('auth_token', auth_token, salt=tools.md5('daydream_oasis'),
                                       max_age=settings.SESSION_COOKIE_AGE,
                                       samesite='', secure='', httponly='')
            # 缓存过期时间更新
            redis_conn.expire(auth_token, settings.SESSION_COOKIE_AGE)
        else:
            tools.delete_cookie(response)

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
