from common.models import BaseModel
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import Q
from utils import tools


# 定义用户模型
class User(AbstractUser, BaseModel):  # 模型继承自django自带的User模型 并在其基础上添加另外的属性

    last_name = None
    first_name = None

    # 手机号
    mobile = models.CharField(max_length=11, unique=True,
                              verbose_name='手机', help_text='手机', null=True)

    # 头像信息 图片上传的逻辑走file应用，这里只用保存地址
    avatar = models.URLField(default='image/default_user_avatar.png',
                             verbose_name='头像', help_text='头像')

    # job
    job = models.CharField(max_length=20, default='打工的人儿~', verbose_name='职业', help_text='职业')

    class Meta:
        db_table = 'user'  # 修改表名
        verbose_name_plural = verbose_name = '用户'  # admin 后台显示

    def __str__(self):
        return self.username

    # 根据用户名/手机号查找用户
    @classmethod
    def get_by_username(cls, username: str):
        return cls.objects.filter(Q(username=username) | Q(mobile=username)).first()

    @classmethod
    def get_by_email(cls, email):
        return cls.objects.filter(email=email).first()

    # 创建一个新的用户,初始用户名和手机号相同
    @classmethod
    def create_user(cls, email: str, password: str) -> 'User':
        tmp_user = cls()
        tmp_user.username = email
        tmp_user.email = email
        tmp_user.password = make_password(password)
        tmp_user.save()
        return tmp_user

    def update_password(self, password):
        self.password = make_password(password)
        self.save()
        return self

    @classmethod
    def get_avatar_by_email(cls, email):
        obj = cls.objects.filter(email=email).first()
        if obj:
            avatar = obj.avatar
        else:
            avatar = 'image/default_user_avatar.png'

        return tools.get_full_media_url(avatar)


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

    # 是否已读
    is_read = models.BooleanField(default=False, verbose_name='是否已读', help_text='是否已读')

    class Meta:
        db_table = 'chat_record'
        verbose_name = verbose_name_plural = '聊天记录'
        ordering = ['create_time']

    @classmethod
    def create_record(cls, sender: User, receiver: User, content: str) -> object:
        tmp_record = cls()
        tmp_record.sender = sender
        tmp_record.receiver = receiver
        tmp_record.content = content
        tmp_record.save()
        return tmp_record
