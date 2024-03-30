from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


class SucResponse(Response):
    CODE = "0"

    def __init__(self, message='请求成功', data=None, error_code="", status=None, headers=None, content_type=None,
                 **kwargs):
        dic = {'code': self.CODE, 'message': message, 'data': {}, 'errorCode': error_code}
        if data is not None:
            dic['data'] = data

        dic.update(kwargs)
        super().__init__(data=dic, status=status, template_name=None,
                         headers=headers, exception=False, content_type=content_type)
        self.accepted_renderer = JSONRenderer()
        self.accepted_media_type = "application/json"
        self.renderer_context = {}
        self.render()


class ErrResponse(Response):
    CODE = "1"

    def __init__(self, message='fail', data=None, error_code="", status=None, headers=None, content_type=None,
                 **kwargs):
        dic = {'code': self.CODE, 'message': message, 'data': {}, 'errorCode': error_code}
        if data is not None:
            dic['data'] = data

        dic.update(kwargs)
        super().__init__(data=dic, status=status, template_name=None,
                         headers=headers, exception=False, content_type=content_type)
        self.accepted_renderer = JSONRenderer()
        self.accepted_media_type = "application/json"
        self.renderer_context = {}
        self.render()
