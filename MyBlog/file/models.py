import os
from django.db import models
from common.models import BaseModel
from user.models import User
import datetime


# 文件上传的位置
def upload_to(o, filename):
    root_dir = list(o.type_size_dict.keys())[o.type]
    now = datetime.datetime.now()
    path = os.path.join(root_dir, f'{now.year}', f'{str(now.month).zfill(2)}', f'{str(now.day).zfill(2)}', filename)
    return path


class File(BaseModel):
    IMAGE = 0
    VIDEO = 1
    AUDIO = 2
    TEXT = 3
    OTHER = 4
    TYPE_CHOICES = (
        (IMAGE, 'image'),
        (VIDEO, 'video'),
        (AUDIO, 'audio'),
        (TEXT, 'text'),
        (OTHER, 'other'),
    )
    # 文件大小的限制
    MB = 1024 * 1024
    type_size_dict = {
        'image': (2 * MB, IMAGE),
        'video': (200 * MB, VIDEO),
        'audio': (50 * MB, AUDIO),
        'text': (20 * MB, TEXT),
        'other': (200 * MB, OTHER),
    }

    # 上传者
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='上传者', help_text='上传者')

    # 类型 图片 视频 音频 文档  其他
    type = models.PositiveIntegerField(default=IMAGE, choices=TYPE_CHOICES, verbose_name='类型', help_text='类型')

    # 路径
    path = models.ImageField(upload_to=upload_to,verbose_name='路径', help_text='路径')

    fields = ['id', 'user', 'type', 'path', 'create_time']

    class Meta:
        db_table = '文件'
        verbose_name_plural = verbose_name = db_table

    @classmethod
    def create(cls, user, _type, path):
        obj = cls()
        obj.user = user
        obj.type = _type
        obj.path = path

        obj.save()
        return obj