from django.urls import re_path

from log import views

urlpatterns = [
    re_path(r'^returnPicture$', views.returnPicture, name='returnPicture'),  # 返回可视化的代码
    re_path(r'^action_log$', views.action_log, name='action_log'),  #用户行为记录

]
