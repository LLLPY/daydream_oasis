import datetime
import hashlib
import re
import threading
from typing import Union
from urllib.parse import urlparse

import orjson
import requests
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import get_template

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


def send_email(subject, message, blog_title, blog_id, operator_username, recipient_list, action, block=False):
    """发送邮件"""
    def get_action_name(action):
        if action == 'comment':
            name = '评论'
        elif action == 'like':
            name = '点赞'
        elif action == 'collect':
            name = '收藏'
        else:
            name = '操作'
    template = get_template('email.html')
    context = {
        'host': settings.HOST,
        'blog_title': blog_title,
        'blog_id': blog_id,
        'operator_username': operator_username,
        'message': message,
        'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'action': action,
        'action_name': get_action_name(action)
    }
    html = template.render(context)
    from_email = f'{settings.DEFAULT_FROM_EMAIL}'
    t = threading.Thread(
        target=send_mail,
        args=(
            subject,  # 邮件标题
            message,  # 邮件内容（文本），有html_message参数，这里配置失效
            from_email,  # 用于发送邮件的邮箱地址，配置授权码的邮箱
            recipient_list,  # 接收邮件的邮件地址，可以写多个
        ),
        # html_message中定义的字符串即HTML格式的信息，可以在一个html文件中写好复制出来放在该字符串中
        kwargs={
            'html_message': html
        })
    t.start()
    if block:
        t.join()


if __name__ == '__main__':
    ...
