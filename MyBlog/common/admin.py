from django.contrib import admin
from MyBlog.admin_site import my_site
from common.models import BackgroundMusic


# 构建一个公共基类，设置默认配置项
class MyBaseAdmin:
    save_on_top = True
    save_on_bottom = True
    list_select_related = True
    save_as = True
    list_display = ['id']


# 背景音乐
@admin.register(BackgroundMusic, site=my_site)
class BackgroundMusicAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'title', 'avatar', 'path']
    search_fields = ['title']
    list_filter = ['title']

    def save_model(self, request, obj, form, change):
        obj.resize(obj.avatar.path, 50, 50)
        super().save_model(request, obj, form, change)
