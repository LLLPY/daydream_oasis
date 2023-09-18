# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/18 10:43
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from log.models import Action
from user.models import User
from .serializers import CategorySerializers, TagSerializers, CommentSerializers, \
    CollectionSerializers, LikeSerializers
from .models import Category, Tag, Blog, Comment, Collection, Like
from common.apis import MyBaseViewSet


# 分类
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs) -> JsonResponse:
        category_list = []
        keyword = request.GET.get('keyword', '').lower()

        for item in Category.get_all().items():
            category = item[0].lower()
            if category.find(keyword) != -1 or keyword.find(category) != -1:
                category_list.append((item[0], item[1]['times']))

        category_list.sort(key=lambda a: -a[1])

        category_list = [item[0] for item in category_list[:10]]

        return JsonResponse({
            'code': '200',
            'msg': '响应成功!',
            'data': {
                'category_list': category_list[:8]
            }

        })


# 标签
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()

    def list(self, request, *args, **kwargs) -> JsonResponse:
        tag_list = []
        keyword = request.GET.get('keyword', '').lower()

        for item in Tag.get_all().items():
            tag = item[0].lower()
            if tag.find(keyword) != -1 or keyword.find(tag) != -1:
                tag_list.append((item[0], item[1]['times']))

        tag_list.sort(key=lambda a: -a[1])

        tag_list = [item[0] for item in tag_list[:10]]

        return JsonResponse({
            'code': '200',
            'msg': '响应成功!',
            'data': {
                'tag_list': tag_list[:8]
            }

        })



