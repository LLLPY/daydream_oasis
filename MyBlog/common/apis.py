# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/3/15 9:56
from django.http import JsonResponse
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from user.models import User


def require_login(require_self=False):
    def outer(func):
        def inner(*args, **kwargs):
            # 根据第一个参数是否是视图函数的实例来取self和request的值
            if isinstance(args[0], View):
                self = args[0]
                request = args[1]
            else:
                request = args[0]

            if not request.user.is_authenticated:
                return JsonResponse({
                    'code': '400',
                    'msg': '请先登录!'
                })

            if require_self:
                tmp_user_id = request.data.get('user') or request.POST.get('user') or request.GET.get('user')
                if str(request.user.id) != tmp_user_id:
                    return JsonResponse({
                        'code': '400',
                        'msg': '非本人操作!'
                    })
            try:
                res = func(*args, **kwargs)
            except Exception as e:
                print(e)
                return None
            return res

        return inner

    return outer


# 关闭csrf
class CsrfExemptSessionAuthentication(SessionAuthentication):
    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


# 分页类
class MyPageNumberPagination(PageNumberPagination):
    # 设置url中的取多少页的key
    page_query_param = 'page'
    # 设置url中设置取数据条数的key
    page_size_query_param = 'size'
    # 设置每一页的数据条数
    page_size = 10
    # 设置每一页最多可取的数据数
    max_page_size = 100


# 对返回值进一步封装，添加自己的返回提示
class MyBaseViewSet(viewsets.ModelViewSet):
    pagination_class = MyPageNumberPagination  # 指定该视图类的分页器
    authentication_classes = (CsrfExemptSessionAuthentication,)

    @require_login()
    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        return Response({
            'code': '200',
            'msg': '响应成功!',
            'data': res.data
        })

    def retrieve(self, request, pk=None, *args, **kwargs):
        res = super().retrieve(request, pk, *args, **kwargs)
        return Response({
            'code': '200',
            'msg': '响应成功!',
            'data': res.data

        })

    @require_login(require_self=True)
    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)

        if res.data.get('user'):
            res.data['user'] = User.get_by_id(res.data['user']).to_dict()

        return Response({
            'code': '200',
            'msg': '新建成功!',
            'data': res.data

        })

    @require_login()
    def update(self, request, pk=None, *args, **kwargs):
        res = super().update(request, pk, *args, **kwargs)
        return Response({
            'code': '200',
            'msg': '更新成功!',
            'data': res.data
        })

    # 删除
    @require_login(require_self=True)
    def destroy(self, request, pk=None):
        res = super().destroy(request, pk)
        return Response({
            'code': '200',
            'msg': '删除成功!',
            'data': res.data
        })
