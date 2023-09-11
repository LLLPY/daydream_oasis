from django.contrib import admin
from django.contrib.admin.models import LogEntry
from django.contrib.auth.hashers import make_password
from MyBlog.admin_site import my_site
from common.admin import MyBaseAdmin
from user.models import (User, ChatRecord, Message)


@admin.register(User, site=my_site)
class UserAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'username', 'avatar', 'mobile', 'job', 'desc', 'date_joined']
    search_fields = ['username', 'mobile']
    list_filter = ['date_joined']

    # 保存用户
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.password = make_password(obj.password)
        obj.resize(obj.avatar.path, 50, 50)
        super().save_model(request, obj, form, change)


# 聊天记录
@admin.register(ChatRecord, site=my_site)
class ChatRecordAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'sender', 'receiver', 'content', 'create_time', 'is_read']
    search_fields = ['sender', 'content']
    list_filter = ['sender', 'receiver', 'is_read', 'create_time']


# 操作日志
@admin.register(LogEntry, site=my_site)
class LogEntryAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'object_repr', 'object_id', 'action_flag', 'user', 'change_message']
    list_display_links = list_display[:1]  # 默认的链接是id
    search_fields = list_display  # 搜索的字段同list_display
    list_filter = list_display[1:3]  # 过滤字段为前3个字段


# 留言(对整个站点的留言)
@admin.register(Message, site=my_site)
class MessageAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'user', 'content', 'create_time', 'weight']
    search_fields = ['user', 'content']
    list_filter = ['user', 'weight', 'create_time']
