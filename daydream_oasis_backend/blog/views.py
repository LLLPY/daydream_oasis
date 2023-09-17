from datetime import datetime, timedelta
from django.core.cache import cache
from django.shortcuts import render
from blog.serializers import BlogSerializers, CategorySerializers,TagSerializers
from blog.models import Comment, Collection, Blog, Search, Like, Category, Tag
from log.models import Action
from rest_framework import viewsets
from rest_framework.decorators import action


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializers
    queryset = Blog.objects.all()

    # 新增博客
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user

    # 博客列表
    def list(self, request, *args, **kwargs):
        pass

    # 博客详情
    def retrieve(self, request, *args, **kwargs):
        pass

    # 更新博客
    def update(self, request, *args, **kwargs):
        ...

    # 删除博客
    def destroy(self, request, *args, **kwargs):
        serizliser = self.get_serializer(data=self.request.data, include_fields=['id'])
        serizliser.is_valid(raise_exception=True)
        blog = Blog.objects.filter(id=id).first()
        blog.delete()
        return
    @action(methods=['get'], detail=False)
    def top_list(self, request, *args, **kwargs):
        '''排行榜'''


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


    def list(self, request, *args, **kwargs):
        '分类列表'

class TagViewSet:
    serializer_class = TagSerializers
    queryset = Tag.objects.all()

class SectionViewSet:
    serializer_class = TagSerializers
    queryset = Tag.objects.all()
