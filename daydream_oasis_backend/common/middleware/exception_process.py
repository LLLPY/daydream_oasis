# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/10/14 13:23
from django.utils.deprecation import MiddlewareMixin
from common.exception.handler import custom_exception_handler


class ExceptionMiddleware(MiddlewareMixin):

    def process_exception(self, request, exception):
        return custom_exception_handler(exception, request.context)
