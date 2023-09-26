# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/3/15 11:54  

from collections import OrderedDict
import time
from functools import wraps
from django_redis import get_redis_connection
from utils import tools

redis_conn = get_redis_connection('default')


# lru_cache
def lru_cache(size=128, expires_check=False, expires=60 * 60 * 24):
    '''
    在lru的基础上增加了过期淘汰规则,防止脏读（数据库中的数据发生改变，而缓存还是旧数据）

    size:缓存的大小
    expires_check:默认不淘汰过期的
    expires:过期时间,默认为1天过期,如果expires_check为True,会淘汰过期的
    '''

    cache = OrderedDict()

    # 生成唯一标识
    def make_key(*args, **kwargs):

        key = ','.join(map(str, args))
        if kwargs:
            sorted_kwargs = sorted(kwargs)
            for k in sorted_kwargs:
                key += '{}={};'.format(k, kwargs[k])
        # 在一次程序生命周期中，相同字符串，它们的hash值是一样的
        return hash(key)

    def wrapper(func):

        @wraps(func)
        def inner(self, *args, **kwargs):

            # 兼容普通的方法和类方法，静态方法不推荐使用
            try:
                cls_name = self.__name__  # 如果是普通的方法或则静态方法就会获取失败
            except AttributeError as e:
                cls_name = self.__class__.__name__
            func_name = func.__name__
            start = time.time()
            key = make_key(self, cls_name, func_name, *args, **kwargs)

            # 淘汰过期的
            if expires_check:
                for k in cache.keys():
                    if time.time() - cache[k][1] > expires:
                        del cache[k]

            # k在缓存中
            if key in cache:

                end = time.time()
                # logging.warning('缓存中获取,耗时:{}s...'.format(end-start))

                # 刚刚使用的移到最后面
                cache.move_to_end(key)  # python2中无此方法:move_to_end,由以下方法来代替
                res = cache[key][0]

                # v = cache[key]
                # del cache[key]
                # cache[key] = v
                # res=cache[0]

            # k不在缓存中
            else:
                res = func(self, *args, **kwargs)
                create_time = time.time()
                cache[key] = (res, create_time)
                end = time.time()
                # logging.warning('函数中获取,耗时:{}s...'.format(end-start))

            # 淘汰最久未使用的
            if len(cache) > size:
                # 最前面的是最长时间没有使用的
                k, v = cache.popitem(last=False)
                # logging.info('{}长时间未使用已被淘汰...\nv:{}'.format(k, v[0]))
            return res

        # 获取整个缓存区的值
        def cache_dict():
            return {k: cache[k][0] for k in cache.keys()}

        inner.cache_dict = cache_dict

        return inner

    return wrapper


# 基于django提供的缓存开发一个缓存装饰器
def cache(timeout=60 * 60):
    # 生成唯一标识
    def make_key(*args, **kwargs):
        key = ','.join(map(str, args))
        if kwargs:
            sorted_kwargs = sorted(kwargs)
            for k in sorted_kwargs:
                key += '{}={};'.format(k, kwargs[k])
        # 在一次程序生命周期中，相同字符串，它们的hash值是一样的
        return tools.md5(key)

    def outer(func):
        @wraps(func)
        def inner(*args, **kwargs):

            # 先尝试从缓存中获取
            key = make_key(func.__name__, args, kwargs)

            res = redis_conn.get(key)
            if res is not None:
                return res
            # 否者执行函数获取返回值
            else:
                res = func(*args, **kwargs)
                redis_conn.set(key, res)
                redis_conn.expire(key, timeout)
                return res

        return inner

    return outer


@lru_cache()
def fun():
    print('hello world')


if __name__ == '__main__':
    fun()
