import jieba
from django.db import models
from PIL.Image import open as imgOpen
from os.path import isfile
from log.logger import logger
from django_redis import get_redis_connection


class RealManager(models.Manager):
    def get_queryset(self):
        return super(RealManager, self).get_queryset().filter(has_deleted=0)


class BaseModel(models.Model):
    # 创建时间
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间', help_text='创建时间')

    # 文章最后修改的时间
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后修改时间',
                                       help_text='最后修改时间')

    # 是否删除
    has_deleted = models.BooleanField(default=False, verbose_name='是否已删除', help_text='是否已删除')

    # desc
    desc = models.CharField(max_length=300, blank=True, verbose_name='简介', help_text='简介')

    # ip地址
    ip = models.CharField(max_length=50, blank=True, verbose_name='IP地址', help_text='IP地址')

    logger = logger

    # redis连接对象
    redis_conn = get_redis_connection('default')

    class Meta:
        abstract = True
        ordering = ['-update_time']

    objects = RealManager()  # 逻辑删除后的
    objects_all = models.Manager()  # 所有的

    def __str__(self) -> str:
        return getattr(self, 'title', super().__str__())

    def delete(self):
        self.has_deleted = True
        self.save()


    @classmethod
    def get_by_id(cls, _id: int):
        return cls.objects.filter(id=_id).first()

    # 获取，没有就创建
    @classmethod
    def get_or_create(cls, title: str, **kwargs):
        _self = cls.objects.filter(title=title).first()
        if not _self:
            _self = cls(title=title, **kwargs)
            _self.save()
        return _self

    # 提取内容中的关键词
    @classmethod
    def get_keyword_list(cls, s: str):

        with open('tmp/stopwords.txt', 'r', encoding='utf8') as f:
            stop_words = set(f.read().split('\n'))
        words = jieba.lcut(s)
        keyword_list = list(set(word for word in words if word not in stop_words))
        return keyword_list

    @classmethod
    def resize(cls, img_path, target_width, target_height):
        if not isfile(img_path): return
        img = imgOpen(img_path)
        w, h = img.size
        k = max(target_width / w, target_height / h)
        # resize图片
        image = img.resize((int(w * k), int(h * k)), ANTIALIAS)
        if image.mode == 'P' or image.mode == 'RGBA':
            image = image.convert('RGB')
        # 将新图像保存
        image.save(img_path, 'JPEG')  # quality指定存储图片的质量


# 背景音乐
class BackgroundMusic(BaseModel):
    # 歌名
    title = models.CharField(max_length=50, verbose_name='歌名', help_text='歌名')

    # 歌手
    singer = models.CharField(max_length=30, verbose_name='歌手', help_text='歌手')

    # 歌曲图片
    avatar = models.URLField(verbose_name='图片', help_text='图片')

    # 歌曲地址
    url = models.FileField(verbose_name='地址', help_text='地址')

    class Meta:
        db_table = '背景音乐'
        verbose_name = verbose_name_plural = db_table


# 友链
class FriendLink(BaseModel):
    title = models.CharField(max_length=100, verbose_name='网站名', help_text='网站名')

    avatar = models.URLField(verbose_name='avatar', help_text='avatar')

    url = models.URLField(verbose_name='地址', help_text='地址')

    weight = models.PositiveIntegerField(default=1, verbose_name='权重', help_text='权重越高越靠前')

    class Meta:
        db_table = '友链'
        verbose_name = verbose_name_plural = db_table
        ordering = ['-weight']

    @classmethod
    def get_friend_link(cls, fields):
        return cls.objects.values(*fields)
