from django.contrib import admin

from MyBlog.admin_site import my_site
from common.admin import MyBaseAdmin
from .models import File


@admin.register(File,site=my_site)
class FileAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'user', 'type', 'path', 'create_time']
    list_filter = ['user', 'type', 'path', 'create_time']
