# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/10/14 13:23  
from django.utils.deprecation import MiddlewareMixin

class ExceptionMiddleware(MiddlewareMixin):

    # 界面友好化处理(当服务器出现异常，状态码为500时，为了不让用户知道服务器的故障，可以使用中间件对此进行处理)
    def process_exception(self, request, exception):
        error = Error()
        error.request_log = request.request_log
        error.reason = str(exception)
        error.save()

        if request.method == 'POST':
            return JsonResponse({
                'code': '500',
                'msg': '抱歉,遇到了未知错误!'
            })

        # 如果报错，将页面重定向到指定页面
        return render(request, '404.html')
