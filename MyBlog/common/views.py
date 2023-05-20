from datetime import datetime
from random import randint, uniform
from time import time
from typing import List
from django.core.cache import cache
from django.core.paginator import Paginator
from article.models import Blog, Tag, Recommend, Category
from link.models import FriendLink
from log.models import RequestRecord
from user.models import Message
from utils.tools import str_to_timestamp
from .models import BackgroundMusic


# 根据出现频数计算字体大小，以及随机颜色
def add_size_and_color(k_times_dict, min_size=12, max_size=20):
    times_list = [k_times_dict[tag]['times'] for tag in k_times_dict]
    max_times, min_times = (max(times_list), min(
        times_list)) if times_list else (0, 0)
    offset = max_times - min_times + 1
    res_list = []
    for tag in k_times_dict:
        font_size = min_size + \
                    (k_times_dict[tag]['times'] - min_times) / \
                    offset * (max_size - min_size)
        res_list.append(
            {'id': k_times_dict[tag]['id'],
             'title': tag,
             'font_size': int(font_size),
             'color': f'rgba{(randint(0, 256), randint(0, 256), randint(0, 256), uniform(0.5, 1))}',
             }
        )
    return res_list


# 排行榜 [(blog1,times1),(blog2,times2)...]
def trans_top_list(top_list: List):
    '''
    通过id获取文章对象后，将其转成字典再返回
    '''
    for i in range(len(top_list)):
        blog = Blog.get_by_id(top_list[i][0])
        if blog:
            top_list[i] = {
                'id': blog.id,
                'title': blog.title if len(blog.title) <= 12 else blog.title[:12] + '...',
                'hot': top_list[i][1],
            }
    return top_list


# 首页和学习星球的公共数据
def common_data(request):
    # 获取用户的登录状态和id
    is_login = 1 if request.user.is_authenticated else 0
    user_id = request.user.id if is_login else ''

    developer = 'LLL'  # 开发者
    blog_num = Blog.objects.count()  # 博客数量
    start_time = str_to_timestamp('2021-5-20 00:00:00')
    run_time = int((time() - start_time))  # 运行的天数
    now = datetime.now()
    pv = RequestRecord.get_pv()  # 访客量
    dpv = RequestRecord.get_pv(now.year, now.month, now.day)  # 今日访客量

    month_top_list = trans_top_list(cache.get('month_top_list') or [])
    week_top_list = trans_top_list(cache.get('week_top_list') or [])
    day_top_list = trans_top_list(cache.get('day_top_list') or [])

    # 友链
    friend_link_list = FriendLink.get_friend_link()

    # 获取背景音乐
    music_list = BackgroundMusic.get_all()
    # 获取标签
    tag_times_dict = Tag.get_all()
    tag_list = add_size_and_color(tag_times_dict)

    # 获取推荐
    recommend_blog_list = Recommend.get_by_user(request.user)

    # 获取分类
    category_times_list = Category.get_all()
    category_list = add_size_and_color(category_times_list)

    # 获取留言
    message_list = Message.get_all()

    return {
        'is_login': is_login,
        'user_id': user_id,
        'developer': developer,
        'blog_num': blog_num,
        'run_time': run_time,
        'pv': pv,
        'dpv': dpv,
        'month_top_list': month_top_list,
        'week_top_list': week_top_list,
        'day_top_list': day_top_list,
        'friend_link_list': friend_link_list,
        'music_list': music_list,
        'tag_list': tag_list,
        'recommend_blog_list': recommend_blog_list,
        'category_list': category_list,
        'message_list': message_list
    }


class MyPage:

    @classmethod
    def get_blog_list(cls, blog_obj_list, page='1', per_page=10):

        blog_list = []
        paginator = Paginator(blog_obj_list, per_page)  # 创建分页对象，每页10条数据
        try:
            page = paginator.page(page)  # 获取某一页的数据
        except Exception as e:
            page = paginator.page('1')  # 发生错误跳转到第一页

        for blog in page.object_list:
            extra_map = {
                'author': {'fields': ['username']},
                'category': {'fields': []},
            }
            fields=['id', 'title', 'author', 'avatar', 'category', 'abstract','create_time','pv','comments','likes','collections']
            blog = blog.to_dict(fields=fields, extra_map=extra_map)
            blog_title = blog['title'].strip('《').strip('》')
            blog_title = '《' + blog_title +'》'

            blog_list.append(blog)

        return page, blog_list

    @classmethod
    def to_dict(cls, page):
        has_previous = 1 if page.has_previous() else 0
        has_next = 1 if page.has_next() else 0
        page_dict = {
            'has_previous': has_previous,
            'has_next': has_next,
            'previous_page_number': page.previous_page_number() if has_previous else '',
            'next_page_number': page.next_page_number() if has_next else '',
        }

        return page_dict


# 基于django提供的缓存开发一个缓存装饰器
def my_cache(timeout=60):
    # 生成唯一标识
    def make_key(*args, **kwargs):
        key = ','.join(map(str, args))
        if kwargs:
            sorted_kwargs = sorted(kwargs)
            for k in sorted_kwargs:
                key += '{}={};'.format(k, kwargs[k])
        # 在一次程序生命周期中，相同字符串，它们的hash值是一样的
        return hash(key)

    def outer(func):
        def inner(*args, **kwargs):

            # 先尝试从缓存中获取
            key = make_key(func.__name__, args, kwargs)
            res = cache.get(key)
            if res:
                return res
            # 否者执行函数获取返回值
            else:
                res = func(*args, **kwargs)
                cache.set(key, res, timeout)
                return res

        return inner

    return outer
