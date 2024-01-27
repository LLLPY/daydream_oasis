# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/9/8 23:03  

from common.drf.response import ErrResponse
from common.exception.service_code import OBJ_NOT_EXIST, VERIFICATION_ERROR
from utils import tools


class CustomValidationError(Exception):
    def __init__(self, msg, error_code=VERIFICATION_ERROR, **kwargs):
        """
        :param msg: 错误信息(英文)
        :param msg_show: 错误信息(中文)
        :param error_code: 业务码
        """
        super(Exception, self).__init__(error_code, msg)
        self.error_code = error_code
        self.msg = msg

    @property
    def response(self):
        return ErrResponse(message=self.msg, error_code=self.error_code)


class ObjectNotFound(CustomValidationError):
    def __init__(self, msg=None, error_code=OBJ_NOT_EXIST, **kwargs):
        super(ObjectNotFound, self).__init__(msg or '对象不存在', error_code=error_code, **kwargs)


class LoginRequired(CustomValidationError):
    def __init__(self, msg=None, error_code=OBJ_NOT_EXIST, **kwargs):
        super(LoginRequired, self).__init__(msg or '请先登录!', error_code=error_code, **kwargs)

    @property
    def response(self):
        res = ErrResponse(message=self.msg, error_code=self.error_code)
        tools.delete_cookie(res)
        return res
