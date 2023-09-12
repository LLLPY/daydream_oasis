from rest_framework.response import Response


class SucResponse(Response):
    CODE = "0"

    def __init__(self, message='请求成功', data=None, error_code="", status=None, headers=None, content_type=None, **kwargs):
        dic = {'code': self.CODE, 'message': message, 'data': {}, 'errorCode': error_code}
        if data is not None:
            dic['data'] = data

        dic.update(kwargs)
        super().__init__(data=dic, status=status, template_name=None,
                         headers=headers, exception=False, content_type=content_type)


class ErrResponse(Response):
    CODE = "1"

    def __init__(self, message='fail', data=None, error_code="", status=None, headers=None, content_type=None, **kwargs):
        dic = {'code': self.CODE, 'message': message, 'data': {}, 'errorCode': error_code}
        if data is not None:
            dic['data'] = data

        dic.update(kwargs)
        super().__init__(data=dic, status=status, template_name=None,
                         headers=headers, exception=False, content_type=content_type)
