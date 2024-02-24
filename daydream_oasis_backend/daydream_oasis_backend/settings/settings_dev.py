# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/1/10 0:39


from daydream_oasis_backend.settings.base import *

DEBUG = True
# INSTALLED_APPS.append('utils')  # 工具包
# INSTALLED_APPS.append('debug_toolbar')  # 性能测试

# 数据库
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'daydream_oasis',
        'HOST': 'www.lll.plus',
        'PORT': '3306',
        'USER': "daydream_oasis",
        "PASSWORD": "daydream_oasis@lll",
        'OPTIONS': {
            'charset': 'utf8mb4',
            "init_command": "SET foreign_key_checks = 0;",
        },
    }
}
