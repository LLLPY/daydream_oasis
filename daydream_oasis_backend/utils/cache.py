# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/3/15 11:54  

from functools import wraps
from django_redis import get_redis_connection
from utils import tools
import pickle

redis_conn = get_redis_connection('default')


def my_cache(timeout=60 * 60):
    # 生成唯一标识
    def make_key(*args, **kwargs):
        key = ','.join(map(str, args))
        if kwargs:
            sorted_kwargs = sorted(kwargs)
            for k in sorted_kwargs:
                key += '{}={};'.format(k, kwargs[k])
        return tools.md5(key)

    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):

            # 先尝试从缓存中获取
            key = make_key(func.__name__, args, kwargs)

            res = redis_conn.get(key)
            if res is not None:
                return pickle.loads(res)
            # 否者执行函数获取返回值
            else:
                res = func(*args, **kwargs)
                redis_conn.set(key, pickle.dumps(res))
                redis_conn.expire(key, timeout)
                return res

        return inner

    return outer


if __name__ == '__main__':
    ...
