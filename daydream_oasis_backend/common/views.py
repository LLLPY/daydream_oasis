from django_redis import get_redis_connection
from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from common.drf.mixin import InstanceMixin
from common.drf.response import SucResponse
from daydream_oasis_backend.settings.base import logger


class BaseViewSet(InstanceMixin, viewsets.ModelViewSet):
    # redis连接对象
    redis_conn = get_redis_connection('default')
    logger = logger
    permission_classes = (AllowAny,)

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        return SucResponse(data=res.data, status=res.status_code, headers=res.headers, content_type=res.content_type,
                           **kwargs)
