import re
from datetime import datetime, timedelta
from typing import List
from django.core.cache import cache
from django.db import models
from django.db.models import Q
from common.models import BaseModel
from blog.models import Blog
from utils.my_cache import my_cache
from user.models import User


# 请求记录表
class RequestRecord(BaseModel):
    PAGE = 0
    MEDIA = 1
    API = 2
    OTHER = 3

    PATH_TYPE_CHOICES = [
        (PAGE, '页面'),
        (MEDIA, '媒体文件'),
        (API, 'API接口'),
        (OTHER, '其他'),

    ]

    path = models.TextField(max_length=1000, default='/', verbose_name='请求路径', help_text='请求路径')
    path_type = models.PositiveIntegerField(default=PAGE, choices=PATH_TYPE_CHOICES, verbose_name='请求路径类型',
                                            help_text='请求路径类型')
    method = models.CharField(max_length=100, default='GET', verbose_name='请求方式', help_text='请求方式')
    user_agent = models.CharField(max_length=500, verbose_name='请求头', help_text='请求头')
    http_refer = models.URLField(verbose_name='跳转的网页', help_text='跳转的网页')
    os = models.CharField(default='', max_length=100, verbose_name='操作系统', help_text='操作系统')
    country = models.CharField(max_length=50, default='', verbose_name='国家', help_text='国家')
    province = models.CharField(max_length=50, default='', verbose_name='省份', help_text='省份')
    city = models.CharField(max_length=50, default='', verbose_name='城市', help_text='城市')
    computer_name = models.CharField(max_length=50, default='', verbose_name='计算机名', help_text='计算机名')
    username = models.CharField(max_length=50, default='', verbose_name='用户名', help_text='用户名')

    class Meta:
        db_table = '请求日志'
        verbose_name = verbose_name_plural = db_table

    def __str__(self):
        return self.path

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    # 获取某天或某月或某年的访问量
    @classmethod
    @my_cache(timeout=60 * 60)
    def get_pv(cls, year=None, moth=None, day=None):
        request_li = cls.objects.filter(path_type=cls.PAGE)
        if year: request_li = request_li.filter(time__year=year)
        if moth: request_li = request_li.filter(time__month=moth)
        if day: request_li = request_li.filter(time__day=day)
        # request_li = request_li.values_list('ip').distinct()
        return request_li.count()

    @classmethod
    def create_request_record(cls, path, method, ip, user_agent, http_refer, os, country, province, city, computer_name,
                              username):
        request_record = cls()
        request_record.path = path
        if path.startswith('/user/api') or path.startswith('/blog/api'):
            request_record.path_type = cls.API
        elif path.startswith('/media'):
            request_record.path_type = cls.MEDIA
        elif path.startswith('/blog') or path.startswith('/login') or path.startswith(
                '/user/register') or path.startswith('/user/forgetPassword') or path == '/':
            request_record.path_type = cls.PAGE
        else:
            request_record.path_type = cls.OTHER
        request_record.method = method
        request_record.ip = ip
        request_record.user_agent = user_agent
        request_record.http_refer = http_refer
        request_record.os = os
        request_record.country = country
        request_record.province = province
        request_record.city = city
        request_record.computer_name = computer_name
        request_record.username = username
        request_record.save()
        return request_record

    # 统计热门排行榜
    @classmethod
    def stat_top(cls):
        # 热门推荐 日热门/周热门/月热门 前5条数据
        _now = datetime.now()

        # 一个月以内的记录
        month_ago = _now - timedelta(days=30)
        week_ago = _now - timedelta(days=7)
        day_ago = _now - timedelta(days=1)

        request_list = cls.objects.filter(
            Q(time__gte=month_ago) & Q(path__regex='^/blog/\d+$'))
        blog_month_list = []
        for request_record in request_list:
            blog_id = re.search(r'\d+', request_record.path).group()
            blog_month_list.append(
                (blog_id, request_record.time)
            )

        # 周热榜 直接利用月热榜的结果 搜索时间
        blog_week_list = [
            blog for blog in blog_month_list if blog[1] >= week_ago]

        # 日热榜
        blog_day_list = [blog for blog in blog_week_list if blog[1] >= day_ago]

        # 统计排序
        def get_top(blog_list: List, k=8):
            blog_con = {}
            for blog in blog_list:
                blog_id = blog[0]
                blog_con[blog_id] = blog_con.get(blog_id, 0) + 1
            top_list = sorted(blog_con.items(), key=lambda a: -a[1])
            return top_list[:k]

        month_top_list = get_top(blog_month_list)
        week_top_list = get_top(blog_week_list)
        day_top_list = get_top(blog_day_list)

        # 写入缓存
        cache.set('month_top_list', month_top_list, 2 * 60 * 60)
        cache.set('week_top_list', week_top_list, 2 * 60 * 60)
        cache.set('day_top_list', day_top_list, 2 * 60 * 60)


# 用户操作记录
class Action(BaseModel):
    DOCALL = 0
    CANCEL_DOCALL = 1
    COLLECT = 2
    CANCEL_COLLECT = 3
    COMMENT = 4
    CANCEL_COMMENT = 5
    CLICK = 6
    READ = 7
    REWARD = 8
    SHARE = 9

    ACTTION_CHOICES = [
        (DOCALL, '点赞'),
        (CANCEL_DOCALL, '取消点赞'),
        (COLLECT, '收藏'),
        (CANCEL_COLLECT, '取消收藏'),
        (COMMENT, '评论'),
        (CANCEL_COMMENT, '删除评论'),
        (CLICK, '点击'),
        (READ, '阅读'),
        (REWARD, '打赏'),
        (SHARE, '分享'),
    ]

    # 行为-分值表
    ACTION_SCORE_MAPPING = {
        DOCALL: 3,
        CANCEL_DOCALL: -2,
        COLLECT: 4,
        CANCEL_COLLECT: -3,
        COMMENT: 2,
        CANCEL_COMMENT: -1,
        CLICK: 1,
        READ: 5,  # 满分5分 根据阅读完成度来给
        REWARD: 5
    }

    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name='用户', help_text='用户')

    # uuid
    uuid = models.CharField(max_length=200, null=False, verbose_name='uuid',
                            help_text='uuid,对于没有登录的用户的唯一标识')

    # 博客
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name='博客', help_text='博客')

    # action
    action = models.PositiveIntegerField(choices=ACTTION_CHOICES, verbose_name='行为', help_text='行为')

    # 耗时
    cost_time = models.FloatField(default=0, verbose_name='耗时', help_text='耗时')

    # 分值
    score = models.IntegerField(default=0, verbose_name='分值', help_text='分值')

    class Meta:
        db_table = '操作日志'
        verbose_name = verbose_name_plural = db_table

    @classmethod
    def create(cls, user, uuid, blog_id, action, cost_time):
        _self = cls()
        _self.user = user
        _self.uuid = uuid
        _self.blog = Blog.get_by_id(blog_id)
        _self.action = action

        if action == cls.READ:
            # 按阅读时间比例给分
            rate = cost_time / _self.blog.read_time
            score = min(float('%.2f' % (rate * cls.ACTION_SCORE_MAPPING[action])), cls.ACTION_SCORE_MAPPING[cls.READ])
        else:

            score = cls.ACTION_SCORE_MAPPING[action]
        _self.score = score
        _self.cost_time = float('%.2f' % cost_time)
        _self.save()
        return _self

    @classmethod
    @my_cache(60 * 60)
    def summary(cls):
        # 统计所有用户的行为累计对文章的打分
        data = {}
        '''
        data = {
            'user_id': {
                'blog_id': 'score',
            }
        }
        '''
        for item in cls.objects.all():
            blog_id = item.blog.id
            uuid = item.uuid
            # 统计用户的(登录后的)
            if item.user:
                user_id = item.user.id
                user_data = data.setdefault(user_id, {})
                score = user_data.setdefault(blog_id, 0) + item.score
                user_data[blog_id] = score
            # 统计uuid的(未登录的)
            uuid_data = data.setdefault(uuid, {})
            score = uuid_data.setdefault(blog_id, 0) + item.score
            uuid_data[blog_id] = score

        return data


# 错误
class Error(BaseModel):
    # 请求的ip
    request_log = models.ForeignKey(RequestRecord, on_delete=models.CASCADE, verbose_name='请求对象',
                                    help_text='请求对象')

    # 错误原因
    reason = models.CharField(max_length=500, verbose_name='错误原因', help_text='错误原因')
    # 时间
    time = models.DateTimeField(default=datetime.now, verbose_name='时间', help_text='时间')

    class Meta:
        db_table = '错误日志'
        verbose_name = verbose_name_plural = db_table
