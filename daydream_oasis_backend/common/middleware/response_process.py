# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/10/14 13:26  
from django.utils.deprecation import MiddlewareMixin
import uuid


class ResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        # 生成的uuid来标识
        _uuid = request.COOKIES.get('uuid')
        if not _uuid:
            _uuid = str(uuid.uuid4())
            response.set_cookie('uuid', _uuid, samesite='None', secure='true')

        return response
