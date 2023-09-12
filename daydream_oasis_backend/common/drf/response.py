import orjson
from django.http import JsonResponse


class SucResponse(JsonResponse):
    pass


class ErrResponse(JsonResponse):
    pass