# -*- coding: UTF-8 -*-
'''
   *****************LLL*********************
   * @Project ：daydream_oasis_backend
   * @File    ：admin_site.py
   * @IDE     ：PyCharm             
   * @Author  ：LLL                         
   * @Date    ：2022/5/20 21:18             
   *****************************************
'''
from django.contrib import admin


# 博主自己的管理台
class MySite(admin.AdminSite):
    site_header = '0318-SPACE博客系统后台'
    site_title = '0318-SPACE博客系统后台'
    index_title = '首页'


my_site = MySite()


# 普通用户的管理台
class CustomSite(admin.AdminSite):
    site_header = '博客系统后台'
    site_title = '博客系统后台'
    index_title = '首页'


custom_site = CustomSite()
