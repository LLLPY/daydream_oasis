# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/1/10 0:39
from .base import *

DEBUG = False
# 数据库
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

# 收集后的所有静态文件存放的位置
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
