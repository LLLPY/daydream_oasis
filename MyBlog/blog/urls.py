# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/9 23:45  
from django.urls import re_path, include
from blog import views
from rest_framework.routers import DefaultRouter
from blog.apis import CategoryViewSet, TagViewSet, ArticleViewSet, CommentViewSet, CollectionViewSet, LikeViewSet

# 路由注册
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'blog', ArticleViewSet, basename='blog')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'collection', CollectionViewSet, basename='collection')
router.register(r'like', LikeViewSet, basename='like')

urlpatterns = [
    re_path(r'^api/', include((router.urls, 'blog-api'), namespace='blog-api')),  # 接口地址
    re_path(r'^add$', views.add, name='add'),  # 写博客
    re_path(r'^update/(?P<blog_id>\d+)$', views.update, name='update'),  # 更新博客
    re_path(r'^search/', views.search, name='search'),  # 搜索功能
    re_path(r'^(?P<blog_id>\d+)$', views.index, name='index'),  # 文章页面

]
