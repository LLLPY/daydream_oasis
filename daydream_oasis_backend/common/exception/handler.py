# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/9/8 23:02  
import logging
import re
import common.exception.exception as exceptions
import common.exception.service_code as service_code
import orjson
from common.drf.response import ErrResponse
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ProgrammingError
from rest_framework import exceptions as rest_exceptions
from rest_framework import status
from rest_framework.exceptions import MethodNotAllowed
from rest_framework.renderers import JSONRenderer
from rest_framework.views import exception_handler

logger = logging.getLogger(__name__)


def custom_exception_handler(exc, context):
    """
        Returns the response that should be used for any given exception.

        By default we handle the REST framework `APIException`, and also
        Django's built-in `Http404` and `PermissionDenied` exceptions.

        Any unhandled exceptions may return `None`, which will cause a 500
        error to be raised.
    """

    # 这里统一打印异常的详细信息
    print(111111111111111111111111111)
    logger.error(exc, exc_info=True)

    # 自定义的异常
    if isinstance(exc, exceptions.CustomValidationError):
        return exc.response
    elif isinstance(exc, rest_exceptions.AuthenticationFailed):
        _, data = exceptions.error_message(
            error_code=service_code.AUTHENTICATION_ERROR,
            msg=str(exc.detail),
        )
        return ErrResponse(**data, status=status.HTTP_401_UNAUTHORIZED)
    elif isinstance(exc, NameError):
        _, data = exceptions.error_message(
            error_code=service_code.VERIFICATION_ERROR,
            msg=exc.__str__(),
        )
        return ErrResponse(**data)
    elif isinstance(exc, MethodNotAllowed):
        _, data = exceptions.error_message(
            error_code=service_code.THIRD_PARTY_API_ERROR,
            msg=str(exc.detail),
        )
        return ErrResponse(**data)
    elif isinstance(exc, exceptions.CallApiError):
        _, data = exceptions.error_message(
            error_code=service_code.THIRD_PARTY_API_ERROR,
            msg=str(exc.message.get("msg")),
        )
        return ErrResponse(**data)
    elif isinstance(exc, ProgrammingError):
        rst = re.search(r"^.*Table '(.*)' doesn't exist", str(exc))
        if rst:
            _, data = exceptions.error_message(error_code=service_code.MYSQL_OPERATE_ERROR, msg="未找到数据")
            return ErrResponse(**data)
    elif isinstance(exc, ObjectDoesNotExist):
        _, data = exceptions.error_message(error_code=service_code.OBJ_NOT_EXIST, msg="未找到数据")
        return ErrResponse(**data)
    else:
        response = exception_handler(exc, context)  # 调用默认的异常处理方法，获取默认的响应对象

        er = ErrResponse('服务异常，请联系管理员')
        er.accepted_renderer = JSONRenderer()
        er.accepted_media_type = "application/json"
        er.renderer_context = {}
        er.render()

        if not response:
            return er

        status_code = getattr(response, 'status_code', 500)
        if status.is_server_error(status_code):
            logger.error(response.text)
            return er

        elif status.is_client_error(status_code):
            try:
                response_str = response.content.decode()
                msg = orjson.loads(response_str)
            except Exception as e:
                logger.error(str(e))
                msg = '请求异常，请联系管理员'
            er.message = msg

            return er
        msg = getattr(exc, "message", "服务异常，请联系管理员") or str(exc)
        _, data = exceptions.error_message(error_code=service_code.SERVICE_ERROR, msg=msg)
        return ErrResponse(**data)
