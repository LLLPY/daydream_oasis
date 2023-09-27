from django.contrib import admin
from daydream_oasis_backend.admin_site import my_site
from common.admin import MyBaseAdmin
from log.models import RequestRecord, Action, Error


# 请求记录
@admin.register(RequestRecord, site=my_site)
class RequestRecordAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'path', 'path_type', 'ip', 'user_agent', 'http_refer', 'create_time', 'country', 'province', 'city']
    search_fields = ['path', 'ip', 'user_agent', 'http_refer']
    list_filter = ['path', 'path_type','country', 'province', 'city', 'create_time']


# 用户行为记录
@admin.register(Action, site=my_site)
class ActionAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'user', 'uuid', 'blog', 'action', 'cost_time', 'score', 'create_time']
    search_fields = ['user__username', 'uuid']
    list_filter = ['user__username', 'uuid', 'action']


# 错误日志
@admin.register(Error, site=my_site)
class ErrorAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'request_log', 'reason', 'create_time']
    search_fields = ['reason']
    list_filter = ['reason']
