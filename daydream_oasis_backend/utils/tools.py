import hashlib
import re
from typing import Union
from urllib.parse import urlparse

import orjson
import requests

from daydream_oasis_backend.settings.base import HOST


def get_address(ip):
    api_url = 'https://api.ip2location.io'
    try:
        return requests.get(api_url, data={'ip': ip}).json()
    except Exception as e:
        return {}
# 信息摘要


def md5(content: Union[str, bytes, dict]):
    # 字符串
    if isinstance(content, str):
        content = content.encode('utf8')

    # 字典
    elif isinstance(content, dict):
        content = orjson.dumps(content, option=orjson.OPT_SORT_KEYS)

    md = hashlib.sha256(content)
    return md.hexdigest()


def limit_str(s: str, max_len=9, suffix='...'):
    '''限制字符串的长度'''

    # 替换掉开头的序号
    s = re.sub(r'^\d+.', '', s)
    cur_len = 0
    end = 0
    for i in range(len(s)):
        '''2汉字=3字母 这里一个字母/空格长度设置为2/3'''
        step = 2 / 3 if s[i].isalpha() or s[i] == ' ' else 1
        cur_len += step
        if cur_len >= max_len:
            end = i
            break
    return s[:end or max_len] + (suffix if end != 0 else '')


def delete_cookie(response, delete_cookie_list=[]):
    '''删除cookie'''
    delete_cookie_list = delete_cookie_list or ['auth_token', 'username', 'user_id', 'avatar']
    for delete_cookie_key in delete_cookie_list:
        response.delete_cookie(delete_cookie_key)


def get_full_media_url(media_url):
    '''获取完整的媒体文件的链接'''
    media_url = str(media_url)
    result = urlparse(media_url)
    if not all([result.scheme, result.netloc]):
        media_url = media_url.strip('/')
        media_url = f'{HOST}media/{media_url}'
    return media_url


def char2ord(s):
    """字符转成对应的字码，方便前端解析"""
    res = ''
    for c in str(s):
        res += f'{ord(c)} '
    return res.strip()


if __name__ == '__main__':
    ...
