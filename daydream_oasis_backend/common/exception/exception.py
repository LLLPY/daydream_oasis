# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/9/8 23:03  


import orjson

from common.drf.response import ErrResponse
from common.exception.service_code import (AUTHENTICATION_ERROR, INFO_CODE, INIT_ERROR,
                           NETWORK_ERROR, OBJ_NOT_EXIST, PASSWORD_WRONG,
                           PERMISSIONE_RROR, SEARCH_NO_FOUND,
                           THIRD_PARTY_API_ERROR, TOO_MANY_LINES,
                           USER_NOT_FOUND, VERIFICATION_ERROR)

err_msg = {
    'invalid': '此字段类型错误，无效的参数',
    'invalid_choice': '参数超出可选范围',
    'phone': "手机号不合法",
    'blank': '此字段不能为空字符串',
    'max_length': '此字段超出最大长度: {max_length}',
    'min_length': '此字段不足最少长度: {min_length}',
    'max_value': '确保此值小于或等于{max_value}',
    'min_value': '确保此值大于或等于{min_value}',
    'max_string_length': '此字段字符串值太大',
    'required': '此字段必填',
    'null': '此字段不能为空。',
    'not_a_dict': '此字段需要是字典类型，但获得类型“{input_type}”',
    'empty': '该字典可能不是空的',
    'date': '此字段需要datetime类型得到了date类型',
    'make_aware': '此字段时区“{timezone}”的日期时间无效',
    'overflow': '此字段日期时间值超出范围',
    'max_digits': '确保此字段总共不超过{max_digits}位',
    'max_decimal_places': '确保此字段小数位数不超过{max_decimal_places}',
    'max_whole_digits': '确保此字段小数点前的位数不超过{max_整位数}。',
    'not_a_list': '此字段需要是列表类型，但获得类型“{input_type}”',
}


def error_message(error_code=INFO_CODE, msg="", data="", **kwargs):
    """错误响应信息"""
    data = {"code": 1, "errorCode": error_code, "data": data, "message": msg}
    # 401表示未登录 其他状态码均用200
    status_code = 401 if error_code == AUTHENTICATION_ERROR else 200

    # 0代表成功，非0代表失败
    return status_code, data  # "msg_show": msg_show,**kwargs


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


class AuthenticationError(CustomValidationError):
    def __init__(self, msg_show):
        super(AuthenticationError, self).__init__(
            "authentication error",
            error_code=AUTHENTICATION_ERROR,
            msg_show=msg_show,
        )


class UserNotFound(CustomValidationError):
    def __init__(self):
        super(UserNotFound, self).__init__(
            "user not found",
            error_code=USER_NOT_FOUND,
            msg_show="用户不存在",
        )


class PasswordWrong(CustomValidationError):
    def __init__(self):
        super(PasswordWrong, self).__init__(
            "password wrong",
            error_code=PASSWORD_WRONG,
            msg_show="密码错误",
        )


class ValidationError(CustomValidationError):
    def __init__(self, msg, msg_show=None):
        super(ValidationError, self).__init__(
            msg=msg,
            error_code=VERIFICATION_ERROR,
            msg_show=msg_show,
        )


class NoPermissionError(CustomValidationError):
    def __init__(self, msg_show=None):
        if not msg_show:
            msg_show = "无操作权限"
        super(NoPermissionError, self).__init__(
            msg_show,
            error_code=PERMISSIONE_RROR,
            msg_show=msg_show,
        )


class TooManyLinesRecv(CustomValidationError):
    def __init__(self, msg_show=None):
        if not msg_show:
            msg_show = "返回数据超过阈值，请批量查询或丰富模糊查询内容"
        super(TooManyLinesRecv, self).__init__(
            "too many lines recv",
            error_code=TOO_MANY_LINES,
            msg_show=msg_show,
        )


class SearchNoFound(CustomValidationError):
    def __init__(self, msg_show=None):
        if not msg_show:
            msg_show = "没有查到相关内容"
        super(SearchNoFound, self).__init__(
            "search no found",
            error_code=SEARCH_NO_FOUND,
            msg_show=msg_show,
        )


class NetWorkError(CustomValidationError):
    def __init__(self, msg_show=None):
        if not msg_show:
            msg_show = "操作失败，请检查您的网络"
        super(NetWorkError, self).__init__(
            "search no found",
            error_code=NETWORK_ERROR,
            msg_show=msg_show,
        )


class ApiException(CustomValidationError):
    def __init__(self, msg=None, msg_show=None):
        if not msg_show:
            msg_show = "接口调用失败"
        if not msg:
            msg = "call api error"
        super(ApiException, self).__init__(
            msg,
            error_code=THIRD_PARTY_API_ERROR,
            msg_show=msg_show,
        )


class ApiAuthenticationError(Exception):
    def __init__(self, *args, **kwargs):
        pass


class CallApiError(CustomValidationError):
    def __init__(self, msg, code=NETWORK_ERROR, url=None, method=None, res=None):
        super(CallApiError, self).__init__(msg, code)
        self.message = {
            "msg": msg,
            "code": code,
            "url": url,
            "method": method,
            "body": (res.json() if res else None),
        }

    def __str__(self):
        return orjson.dumps(self.message)


class AuthorizationError(CallApiError):
    def __init__(self):
        super(AuthorizationError, self).__init__("Authorization Error", 401)


class SeerflowError(CustomValidationError):
    pass


class CeleryAppError(CustomValidationError):
    pass


class ObjectNotFound(CustomValidationError):
    def __init__(self, msg=None, error_code=OBJ_NOT_EXIST, **kwargs):
        super(ObjectNotFound, self).__init__(msg or '对象不存在', error_code=error_code, **kwargs)


class PMMLRequiredAttribError(CustomValidationError):
    def __init__(self, msg=None, error_code=INIT_ERROR, **kwargs):
        super(PMMLRequiredAttribError, self).__init__(msg or '节点文件缺少必要的属性', error_code=error_code, **kwargs)
