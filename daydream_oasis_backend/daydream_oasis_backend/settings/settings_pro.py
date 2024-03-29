# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/1/10 0:39
import os

from .base import *

DEBUG = False

# 从环境变量中获取数据库的配置
db_NAME = os.environ.get('db_NAME')
db_HOST = os.environ.get('db_HOST')
db_PORT = os.environ.get('db_PORT')
db_USER = os.environ.get('db_USER')
db_PASSWORD = os.environ.get('db_PASSWORD')

if not all((db_NAME, db_HOST, db_PORT, db_USER)):
    raise Exception('数据库配置错误')

# 数据库
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_NAME,
        'HOST': db_HOST,
        'PORT': db_PORT,
        'USER': db_USER,
        "PASSWORD": db_PASSWORD,
        'OPTIONS': {
            'charset': 'utf8mb4',
            "init_command": "SET foreign_key_checks = 0;",
        },
    }
}

# 收集后的所有静态文件存放的位置
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
