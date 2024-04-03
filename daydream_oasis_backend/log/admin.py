from django.contrib import admin

from common.admin import MyBaseAdmin
from daydream_oasis_backend.admin_site import my_site
from log.models import Action, RequestRecord


# 请求记录
@admin.register(RequestRecord, site=my_site)
class RequestRecordAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'path', 'ip', 'user_agent', 'http_refer', 'create_time', 'status']
    search_fields = ['path', 'ip']
    list_filter = ['path', 'create_time', 'status']


# 用户行为记录
@admin.register(Action, site=my_site)
class ActionAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'user', 'uuid', 'blog', 'action', 'cost_time', 'score', 'create_time']
    search_fields = ['user__username', 'uuid']
    list_filter = ['user__username', 'uuid', 'action']
