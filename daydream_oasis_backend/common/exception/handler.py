# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/9/8 23:02
import common.exception.exception as exceptions
from common.drf.response import ErrResponse
from rest_framework.exceptions import APIException

from daydream_oasis_backend.settings.base import logger


def custom_exception_handler(exc, context=None):
    """
        Returns the response that should be used for any given exception.

        By default we handle the REST framework `APIException`, and also
        Django's built-in `Http404` and `PermissionDenied` exceptions.

        Any unhandled exceptions may return `None`, which will cause a 500
        error to be raised.
    """

    # 这里统一打印异常的详细信息
    logger.error(exc, exc_info=True)
    # 自定义的异常
    if isinstance(exc, exceptions.CustomValidationError):
        return exc.response
    elif isinstance(exc, APIException):
        return ErrResponse(message=str(exc.detail))
    else:
        return ErrResponse(message='服务异常，请联系管理员')
