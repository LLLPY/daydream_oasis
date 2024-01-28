"""
WSGI settings for daydream_oasis_backend project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 暂时使用dev
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daydream_oasis_backend.settings.settings_dev')
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'daydream_oasis_backend.settings.settings_pro')

application = get_wsgi_application()
