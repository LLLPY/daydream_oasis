import datetime
import os

from common.models import BaseModel
from django.db import models
from PIL import Image
from user.models import User


# 文件上传的位置
def upload_to(o, filename):
    root_dir = list(o.type_size_dict.keys())[o.type]
    now = datetime.datetime.now()
    path = os.path.join(
        root_dir, f'{now.year}', f'{str(now.month).zfill(2)}', f'{str(now.day).zfill(2)}', filename)
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
        'image': (2, IMAGE),
        'video': (200, VIDEO),
        'audio': (50, AUDIO),
        'text': (20, TEXT),
        'other': (200, OTHER),
    }

    # 上传者
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='上传者', help_text='上传者')

    # 类型 图片 视频 音频 文档  其他
    type = models.PositiveIntegerField(
        default=IMAGE, choices=TYPE_CHOICES, verbose_name='类型', help_text='类型')

    # 路径
    path = models.FileField(upload_to=upload_to, verbose_name='路径', help_text='路径')

    class Meta:
        db_table = 'file'
        verbose_name_plural = verbose_name = '文件'

    @classmethod
    def create(cls, user, _type, path):
        obj = cls()
        obj.user = user
        obj.type = _type
        obj.path = path

        obj.save()
        return obj

    @classmethod
    def resize_image(cls, input_path, output_path, new_size=50):
        '''
        将图片缩放到指定的大小，new_size指定了新的大小，长度和宽度都是该值。
        '''
        # 打开传入的图片
        input_image = Image.open(input_path)

        # 计算裁剪的位置
        width, height = input_image.size
        left = (width - min(width, height)) / 2
        top = (height - min(width, height)) / 2
        right = (width + min(width, height)) / 2
        bottom = (height + min(width, height)) / 2

        # 裁剪图片
        input_image = input_image.crop((left, top, right, bottom))

        # 缩放图片
        input_image = input_image.resize((new_size, new_size))

        # 保存处理后的图片
        input_image.save(output_path)
