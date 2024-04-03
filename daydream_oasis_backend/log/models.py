from datetime import datetime, timedelta

from blog.models import Blog
from common.models import BaseModel
from django.db import models
from django.db.models import Count
from user.models import User


# 请求记录表
class RequestRecord(BaseModel):

    # 请求响应的状态
    PENDING = 0
    SUCCESS = 1
    FAIL = 2

    STATUS_CHOICES = (
        (PENDING, '响应中'),
        (SUCCESS, '成功'),
        (FAIL, '失败'),
    )

    path = models.TextField(max_length=1000, default='/', verbose_name='请求路径', help_text='请求路径')
    method = models.CharField(max_length=100, default='GET', verbose_name='请求方式', help_text='请求方式')
    user_agent = models.CharField(max_length=500, verbose_name='请求头', help_text='请求头')
    http_refer = models.URLField(verbose_name='跳转的网页', help_text='跳转的网页')
    os = models.CharField(default='', max_length=100, verbose_name='操作系统', help_text='操作系统')
    computer_name = models.CharField(max_length=50, default='', verbose_name='计算机名', help_text='计算机名')
    username = models.CharField(max_length=50, default='', verbose_name='用户名', help_text='用户名')
    status = models.PositiveIntegerField(default=PENDING, choices=STATUS_CHOICES, verbose_name='响应状态', help_text='响应状态')
    extra = models.JSONField(default=dict, verbose_name='其他信息', help_text='其他信息')
    class Meta:
        db_table = 'request_log'
        verbose_name = verbose_name_plural = '请求记录'

    def __str__(self):
        return self.path

    # 获取某天或某月或某年的访问量
    @classmethod
    def get_pv(cls, year=None, moth=None, day=None):
        request_li = cls.objects
        if year:
            request_li = request_li.filter(time__year=year)
        if moth:
            request_li = request_li.filter(time__month=moth)
        if day:
            request_li = request_li.filter(time__day=day)
        # request_li = request_li.values_list('ip').distinct()
        return request_li.count()

    @classmethod
    def create_request_record(cls, path, method, ip, user_agent, http_refer, os, computer_name, username):
        request_record = cls()
        request_record.path = path
        request_record.method = method
        request_record.ip = ip
        request_record.user_agent = user_agent
        request_record.http_refer = http_refer
        request_record.os = os
        request_record.computer_name = computer_name
        request_record.username = username
        request_record.save()
        return request_record

    # 统计热门排行榜
    @classmethod
    def stat_top(cls, days_ago=None, k=None):
        '''
        time_ago:多少天以内的数据
        k:前k条数据
        '''
        # 所有的博客请求记录
        blog_requests = cls.objects.filter(blog_id__isnull=False)

        # 确定到某个时间范围内
        if days_ago:
            now = datetime.now()
            blog_requests = blog_requests.filter(create_time__gte=now - timedelta(days=days_ago))

        res = blog_requests.values('id', 'blog__id', 'blog__title').annotate(visit_count=Count('blog__id')).order_by(
            '-visit_count')

        return res
        # 写入缓存


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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,
                             verbose_name='用户', help_text='用户')

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
        db_table = 'action_log'
        verbose_name = verbose_name_plural = '行为记录'

    @classmethod
    def create(cls, blog_id, action, cost_time, request=None):
        _self = cls()
        _self.user = request.user if request.user.is_authenticated else None
        _self.uuid = request.COOKIES.get('uuid', '-')
        _self.blog_id = blog_id
        _self.action = action

        if action == cls.READ:
            # 按阅读时间比例给分
            rate = cost_time / _self.blog.read_time
            score = min(
                float('%.2f' % (rate * cls.ACTION_SCORE_MAPPING[action])), cls.ACTION_SCORE_MAPPING[cls.READ])
        else:

            score = cls.ACTION_SCORE_MAPPING[action]
        _self.score = score
        _self.cost_time = float('%.2f' % cost_time)
        _self.save()
        return _self

    @classmethod
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


