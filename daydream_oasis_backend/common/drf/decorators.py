from common.exception import exception
from functools import wraps


def login_required(func):
    '''要求登录才能访问'''

    @wraps(func)
    def inner(self, *args, **kwargs):

        if not hasattr(self.request,
                       'user') or not self.request.user.is_authenticated:
            raise exception.CustomValidationError('请先登录!')

        res = func(self, *args, **kwargs)

        return res

    return inner
