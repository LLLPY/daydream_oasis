from rest_framework import viewsets
from common.drf.mixin import InstanceMixin
from common.drf.response import SucResponse


class BaseViewSet(viewsets.ModelViewSet, InstanceMixin):

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        print(res.headers)
        return SucResponse(data=res.data, status=res.status_code, headers=res.headers, content_type=res.content_type,**kwargs)
