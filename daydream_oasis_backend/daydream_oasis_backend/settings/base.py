# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/10 0:39  

import os
from pathlib import Path
import sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(td!6u-jnj#fjg9zpigq^&x4iqtluw%mr_g(l880pbofp+8$&u'

# SECURITY WARNING: don't run with debug turned on in production!

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    'simpleui',  # 后台美化
    'ckeditor',  # 富文本编辑器
    'ckeditor_uploader',  # 富文本中图片的上传,
    'rest_framework',  # restful api
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user',  # user
    'blog',  # 学习星球
    'log',  # 访问日志
    'file',  # 文件
    'common',  # 公共部分
    'task',  # 任务
    'frontconfig',  # 前端配置
    'corsheaders',  # CORS跨域问题

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # 跨域请求
    'common.middleware.request_process.RequestMiddleWare',  # 请求处理
    'common.middleware.rate_limit.RateLimitMixin',  # 限流
    'common.middleware.response_process.ResponseMiddleware',  # 响应中间件
    # 'common.middleware.exception_process.ExceptionMiddleware' #异常处理
]

# 解决跨域
CORS_ALLOW_CREDENTIALS = True  # 允许携带Cookie
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    '*'
)
CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173'

]
CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
    '*'
)

CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

ROOT_URLCONF = 'daydream_oasis_backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },

    },
]

WSGI_APPLICATION = 'daydream_oasis_backend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# redis的配置
CACHES = {
    'default': {  # 默认
        "BACKEND": 'django_redis.cache.RedisCache',
        'LOCATION': f'redis://127.0.0.1:6379/0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

# 替换系统的User 来使用我们自己定义的User
AUTH_USER_MODEL = 'user.User'  # 子应用名.模型类名

# 修改上传文件的最大值
DATA_UPLOAD_MAX_MEMORY_SIZE = 524288000  # 默认设置为500M

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
        'height': 800,
        'width': '100%',
        'tabSpaces': 4,
        'extraPlugins': 'codesnippet',  # 配置代码插件
    }
}

# 静态文件的目录
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

STATIC_URL = '/static/'  # 指定静态文件的路由

# 媒体文件的存放
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # 存储路径
MEDIA_URL = '/media/'

# 富文本编辑器中图片的上传路径
CKEDITOR_UPLOAD_PATH = os.path.join(BASE_DIR, 'media', 'image')

# 修改默认的文件存储为自定义的
DEFAULT_FILE_STORAGE = 'daydream_oasis_backend.storage.WatermarkStorage'

# 后台的logo
SIMPLEUI_LOGO = f'../../static/image/favorite.png'

# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False
from common.exception.handler import custom_exception_handler

REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema',
    # 自定义异常捕获
    'EXCEPTION_HANDLER': 'common.exception.handler.custom_exception_handler'
}

# 解决警告
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
