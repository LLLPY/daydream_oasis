import re
import hashlib
from typing import Union
from urllib.parse import urlparse

import orjson

from daydream_oasis_backend.settings.base import HOST


# 获取ip相关的信息,
def get_ip_info(ip: str):
    # r = get(url=f'http://ip-api.com/json/{ip}?lang=zh-CN')
    country, region, city, latitude, longitude, timezone, isp = 'None', 'None', 'None', 'None', 'None', 'None', 'None'
    # try:
    #     r_json = r.json()
    #     country = r_json.get('country', 'None')
    #     region = r_json.get('regionName', 'None')
    #     city = r_json.get('city', 'None')
    #     latitude = r_json.get('latitude', 'None')
    #     longitude = r_json.get('longitude', 'None')
    #     timezone = r_json.get('timezone', 'None')
    #     isp = r_json.get('isp', 'None')
    # except:
    #     pass
    return (country, region, city, latitude, longitude, timezone, isp)


# def get_address(ip):
#     api_url = f'https://freeapi.ipip.net/{ip}'
#     try:
#         # 先从缓存中获取，如果没有就再请求接口
#         location = cache.get(f'{ip}-address', None)
#         if not location:
#             res = requests.get(api_url)
#             location = res.json()[:3]
#             cache.set(f'{ip}-address', location, 60 *
#                       60 * 24 * 7)  # 假设一个用户7天之内不会更换位置
#         return location
#     except Exception as e:
#         return ['', '', '']
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
    delete_cookie_list = delete_cookie_list or ['auth_token', 'username']
    for delete_cookie_key in delete_cookie_list:
        response.delete_cookie(delete_cookie_key)


def get_full_media_url(media_url):
    '''获取完整的媒体文件的链接'''
    result = urlparse(media_url)
    if not all([result.scheme, result.netloc]):
        media_url = media_url.strip('/')
        media_url = f'{HOST}media/{media_url}'
    return media_url


if __name__ == '__main__':
    ...
