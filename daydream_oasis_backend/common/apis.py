# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/3/15 9:56
from django.http import JsonResponse
from django.views.generic.base import View
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from user.models import User


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

    def create(self, request, *args, **kwargs):
        res = super().create(request, *args, **kwargs)

        if res.data.get('user'):
            res.data['user'] = User.get_by_id(res.data['user']).to_dict()

        return Response({
            'code': '200',
            'msg': '新建成功!',
            'data': res.data

        })

    def update(self, request, pk=None, *args, **kwargs):
        res = super().update(request, pk, *args, **kwargs)
        return Response({
            'code': '200',
            'msg': '更新成功!',
            'data': res.data
        })

    # 删除
    def destroy(self, request, pk=None):
        res = super().destroy(request, pk)
        return Response({
            'code': '200',
            'msg': '删除成功!',
            'data': res.data
        })
