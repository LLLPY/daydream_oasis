from functools import wraps

from common.exception import exception
from utils import tools


def login_required(func):
    '''要求登录才能访问'''

    @wraps(func)
    def inner(self, *args, **kwargs):

        if not hasattr(self.request,
                       'user') or not self.request.user.is_authenticated:
            raise exception.LoginRequired('请先登录!')

        res = func(self, *args, **kwargs)

        return res

    return inner


def rate_lock(timeout=3):
    '''频率限制锁，指定时间段内只能操作1次'''

    def make_key(func_name, request):
        user = request.user
        data = request.data or request.query_params
        key = f'{func_name}:{user.id}:{tools.md5(data)}'
        return tools.md5(key)

    def outer(func):

        @wraps(func)
        def inner(self, *args, **kwargs):

            key = make_key(func.__name__, self.request)
            success = self.redis_conn.setnx(key, 'liked')
            if not success:
                raise exception.CustomValidationError(f'{timeout}秒内不能重复操作哟!')

            # 3秒内只能点一次赞
            self.redis_conn.expire(key, timeout)

            res = func(self, *args, **kwargs)

            return res

        return inner

    return outer
