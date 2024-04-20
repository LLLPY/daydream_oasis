# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/1/10 0:39
import logging
import os
from pathlib import Path

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
    # 'task',  # 任务
    'frontconfig',  # 前端配置
    'corsheaders',  # CORS跨域问题
    'mdeditor'

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
    'common.middleware.response_process.ResponseMiddleware',  # 响应中间件
    'common.middleware.request_process.RequestMiddleWare',  # 请求处理
    'common.middleware.rate_limit.RateLimitMixin',  # 限流

]

# 解决跨域
CORS_ALLOW_CREDENTIALS = True  # 允许携带Cookie
CORS_ORIGIN_ALLOW_ALL = True

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

# 指定现有的静态文件的目录 参考：https://www.qikqiak.com/post/django-staticroot-staticfilesdirs-function/
STATICFILES_DIRS = []

# 共享文件的目录（媒体文件）
SHARE_DIR = '/share/daydream_oasis'

# 静态文件收集后存放的目录
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'  # 指定静态文件的路由

# 媒体文件的存放
MEDIA_ROOT = os.path.join(SHARE_DIR, 'media')  # 存储路径
MEDIA_URL = '/media/'

# 修改默认的文件存储为自定义的
DEFAULT_FILE_STORAGE = 'daydream_oasis_backend.storage.WatermarkStorage'

# 隐藏右侧SimpleUI广告链接和使用分析
SIMPLEUI_HOME_INFO = False
SIMPLEUI_ANALYSIS = False

# 解决警告
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
REST_FRAMEWORK = {
    # 自定义异常捕获
    'EXCEPTION_HANDLER': 'common.exception.handler.custom_exception_handler',
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}

# host
HOST = 'http://www.lll.plus/'

# 后台的logo
# SIMPLEUI_LOGO = f'{HOST}media/image/default_blog_avatar.jpg'

# 日志的配置
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'daydream_oasis': {
            'format': '{name} {levelname} {asctime} {message}; pid:{process:d} tid:{thread:d} {pathname}:{lineno}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': [],
            'class': 'logging.StreamHandler',
            'formatter': 'daydream_oasis',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': [],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'daydream_oasis',
        }
    },
    'loggers': {
        'daydream_oasis': {
            'handlers': ['console', 'mail_admins'],
            'level': 'INFO',
        }
    }
}

logger = logging.getLogger('daydream_oasis')

# cookie默认过期时间
SESSION_COOKIE_AGE = 3600 * 24 * 7  # 设置Cookie的过期时间为7天
