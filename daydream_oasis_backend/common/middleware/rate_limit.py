# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/10/10 23:49
from django.core.cache import cache
import time
from log.logger import logger
from common.drf.response import SucResponse
from django.utils.deprecation import MiddlewareMixin


class RateLimitMixin(MiddlewareMixin):
    '''流量限制'''

    def process_request(self, request):
        ip = request.META.get('REMOTE_ADDR', '')  # 客户端的ip地址
        msg = None
        # 实现限制某个时间段内的访问次数(例:1分钟内只能访问200次)
        ip_list = cache.get(ip, [])
        # 时间限制在1分钟 (比较最新的请求和最早的请求的时间差，如果大于60秒，则踢出最早的请求)
        # 如果ip列表的长度大于200，就处于封禁状态，就不能进行pop操作
        while ip_list and time.time() - ip_list[-1] > 60 and len(ip_list) < 200:
            ip_list.pop()

        # # 最新的请求添加到请求列表的头部，那么最早的请求就在列表的尾部
        ip_list.insert(0, time.time())
        # 将请求列表保存在缓存中
        if len(ip_list) <= 200:
            cache.set(ip, ip_list, timeout=60)

        elif len(ip_list) <= 300:
            cache.set(ip, ip_list, timeout=60 * 30)  # 封禁30分钟
            msg = '喝杯茶休息一下吧!'
            logger.warning(f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden for 0.5 hours...')

        elif len(ip_list) <= 500:
            cache.set(ip, ip_list, timeout=60 * 60 * 2)  # 封禁两个小时
            msg = '看个电影再来吧!'
            logger.warning(
                f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden for 2 hours...')

        elif len(ip_list) <= 800:
            cache.set(ip, ip_list, timeout=60 * 60 * 24)  # 封禁一天
            msg = '不早了，睡觉觉吧!'
            logger.warning(f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden for 1 day...')

        else:
            cache.set(ip, ip_list)  # 永久封禁
            msg = '对不起,是我们缘分不够!'
            logger.warning(f'{request.user}[{request.META.get("REMOTE_ADDR")}] was forbidden forever...')
        return SucResponse(message=msg) if msg else None
