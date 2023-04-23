import datetime
from typing import List, Dict
from django.db import models
from common.models import BaseModel
from common.my_cache import my_cache


# 友链
class FriendLink(models.Model, BaseModel):
    title = models.CharField(
        max_length=100, db_column='网站', verbose_name='网站', help_text='网站')

    avatar = models.ImageField(blank=True, upload_to='image/%Y/%m/%d',
                               db_column='avatar', verbose_name='avatar', help_text='avatar')

    url = models.URLField(db_column='地址', verbose_name='地址', help_text='地址')

    desc = models.CharField(max_length=100, db_column='描述',
                            verbose_name='描述', default='', help_text='描述')

    weight = models.PositiveIntegerField(
        default=1, db_column='权重', verbose_name='权重', help_text='权重越高越靠前')

    time = models.DateTimeField(
        default=datetime.datetime.now, db_column='时间', verbose_name='时间', help_text='时间')

    fields = ['id', 'title', 'avatar', 'url', 'desc', 'weight', 'time']

    class Meta:
        db_table = '友链'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-weight']

    # 返回所有的友链信息
    @classmethod
    def get_all(cls):
        return cls.objects.all()

    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        return super().to_dict(fields, exclude_list, extra_map)

    @classmethod
    @my_cache(timeout=60)
    def get_friend_link(cls, fields=fields):
        return cls.objects.values(*fields)
