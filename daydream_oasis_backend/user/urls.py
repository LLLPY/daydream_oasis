# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/10 0:16  
from django.urls import re_path,include
from user import views
from rest_framework.routers import DefaultRouter
from .apis import UserViewSet,MessageViewSet

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'message', MessageViewSet, basename='message')

urlpatterns = [

    re_path(r'^api/', include((router.urls, 'user-api'), namespace='user-api')),  # 接口地址
]
