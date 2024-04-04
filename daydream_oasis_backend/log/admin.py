from common.admin import MyBaseAdmin
from django.contrib import admin
from log.models import Action, RequestRecord

from daydream_oasis_backend.admin_site import my_site


# 请求记录
@admin.register(RequestRecord, site=my_site)
class RequestRecordAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'path', 'method', 'ip', 'status', 'create_time',
                    'os', 'computer_name', 'username', 'user_agent', 'http_refer', 'extra']
    search_fields = ['path', 'method', 'ip']
    list_filter = ['path', 'create_time', 'status']


# 用户行为记录
@admin.register(Action, site=my_site)
class ActionAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'user', 'uuid', 'blog', 'action', 'cost_time', 'score', 'create_time']
    search_fields = ['user__username', 'uuid']
    list_filter = ['user__username', 'uuid', 'action']
