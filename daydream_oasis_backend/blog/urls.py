# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/9 23:45  
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from blog.apis import CategoryViewSet, TagViewSet, CommentViewSet, CollectionViewSet, LikeViewSet
from blog.views import BlogViewSet
# 路由注册
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'collection', CollectionViewSet, basename='collection')
router.register(r'like', LikeViewSet, basename='like')

urlpatterns = [
    re_path(r'^api/', include((router.urls, 'blog-api'), namespace='blog-api')),  # 接口地址

]
