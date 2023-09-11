import datetime
import re
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from common.models import BaseModel


# 定义用户模型
class User(AbstractUser, BaseModel):  # 模型继承自django自带的User模型 并在其基础上添加另外的属性

    last_name = None
    first_name = None

    # 手机号
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机', help_text='手机')

    # 头像信息 头像的保存路径static/avatar/%Y%m%d
    avatar = models.ImageField(upload_to='image/%Y/%m/%d',
                               default='image/default_user_avatar.png', verbose_name='头像',
                               help_text='头像')

    # job
    job = models.CharField(max_length=20, default='打工的人儿~', verbose_name='职业', help_text='职业')

    # 简介
    desc = models.CharField(max_length=300, default='这个人很懒,ta什么都没写~', verbose_name='简介', help_text='简介')

    # 位置
    longitude = models.FloatField(default=0, verbose_name='经度', help_text='经度')
    latitude = models.FloatField(default=0, verbose_name='纬度', help_text='纬度')

    class Meta:
        db_table = '用户'  # 修改表名
        verbose_name_plural = verbose_name = db_table  # admin 后台显示

    def __str__(self):
        return self.username

    # 根据用户名/手机号查找用户
    @classmethod
    def get_by_username(cls, username: str):
        return cls.objects.filter(Q(username=username) | Q(mobile=username)).first()

    @classmethod
    def get_by_username_and_mobile(cls, username, mobile):
        return cls.objects.filter(Q(username=username) | Q(mobile=mobile)).first()

    @classmethod
    def get_by_mobile(cls, mobile):
        return cls.objects.filter(mobile=mobile).first()

    def update(self, mobile, username, password):
        self.mobile = mobile
        self.username = username
        self.password = make_password(password)
        self.save()
        return self

    # 创建一个新的用户,初始用户名和手机号相同
    @classmethod
    def create_user(cls, mobile: str, password: str) -> 'User':
        tmp_user = cls()
        tmp_user.username = mobile
        tmp_user.mobile = mobile
        tmp_user.password = make_password(password)
        tmp_user.save()
        return tmp_user

    # 监测手机号是否合法
    @classmethod
    def is_valid_mobile(cls, mobile: str) -> bool:
        return bool(re.match(r'^[1][345789][0-9]{9}$', mobile))

    # 监测验证码是否合法
    @classmethod
    def is_valid_code(cls, code):
        return bool(re.match(r'\d{4}', code))

    # 监测密码是否合法
    @classmethod
    def is_valid_password(cls, password):
        return bool(
            6 <= len(password) <= 20 and re.match(r'.*\d+.*', password) and re.match(r'.*[a-zA-Z]+.*', password))

    # 更新
    def update_location(self, longitude, latitude):
        self.longitude = longitude or self.longitude
        self.latitude = latitude or self.latitude
        self.save()

    # 保存
    def save(self, *args, **kwargs):
        avatar_path = self.avatar.path
        self.resize(avatar_path, 50, 50)
        res = super().save(*args, **kwargs)
        return res


# 聊天记录
class ChatRecord(BaseModel):
    # 发送人
    sender = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='发送人', help_text='发送人',
                               related_name='发送人')  # 发送人可以是匿名私信

    # 接收人
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='接收人', help_text='接收人',
                                 related_name='接收人')

    # 发送的内容
    content = models.CharField(max_length=1000, verbose_name='内容', help_text='内容')

    # 时间
    time = models.DateTimeField(default=datetime.datetime.now, verbose_name='时间', help_text='时间')

    # 是否已读
    is_read = models.BooleanField(default=False, verbose_name='是否已读', help_text='是否已读')

    fields = ['id', 'sender', 'receiver', 'content', 'create_time', 'is_read']

    class Meta:
        db_table = '信息'
        verbose_name = verbose_name_plural = db_table
        ordering = ['create_time']

    @classmethod
    def create_record(cls, sender: User, receiver: User, content: str) -> object:
        tmp_record = cls()
        tmp_record.sender = sender
        tmp_record.receiver = receiver
        tmp_record.content = content
        tmp_record.save()
        return tmp_record


# 留言(相对于整站的留言)
class Message(BaseModel):
    # 留言人
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='留言人', help_text='留言人')

    # 留言内容
    content = models.CharField(max_length=200, verbose_name='内容', help_text='内容')

    # 权重
    weight = models.PositiveIntegerField(default=0, verbose_name='权重', help_text='权重')

    class Meta:
        db_table = '留言'
        verbose_name_plural = verbose_name = db_table
        ordering = ['-weight', '-create_time']

    @classmethod
    def get_all(cls):
        data_list = []
        for message in cls.objects.all():
            data_list.append(
                message.to_dict()
            )
        return data_list
