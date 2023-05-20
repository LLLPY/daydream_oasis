from typing import List, Dict
import jieba
from django.db import models
from MyBlog.config.base import MEDIA_URL
from common.my_cache import my_cache
from PIL.Image import open as imgOpen, ANTIALIAS
from os.path import isfile


class BaseModel:
    fields = []

    # 将对象转成字典
    def to_dict(self, fields: List[str] = fields, exclude_list: List[str] = [], extra_map: Dict = {}) -> Dict:
        '''
        fields:需要转换的字段列表
        exclude_list:不需要转换的字段列表
        extra_map:需要二次to_dict的对象的配置表
        例如：
            blog:(title,author)--->author需要再次to_dict
            对于author的fields和exclude_list配置，可以写在extra_map中
            extra_map={
                'author':{
                    'fields':[],
                    'exclude_list':[],
                    }
            }
        '''
        con = {}
        for k in fields:
            if k not in exclude_list and hasattr(self, k):

                obj_v = getattr(self, k)
                # 需要再次to_dict
                if isinstance(obj_v, models.Model):
                    k_extra_map = extra_map.get(k, {})
                    _fields = k_extra_map.get('fields', None)
                    _exclude_list = extra_map.get('exclude_list', exclude_list)

                    if _fields:
                        con[k] = obj_v.to_dict(fields=_fields, exclude_list=_exclude_list,
                                               extra_map=extra_map)
                    else:
                        con[k] = obj_v.to_dict(exclude_list=_exclude_list, extra_map=extra_map)

                # 时间
                elif k in ['create_time', 'update_time', 'time']:
                    con[k] = str(obj_v).split('.')[0]

                # 阅读时长
                elif k in ['read_time']:
                    minute = int(obj_v) // 60
                    seconds = int(obj_v) % 60
                    con[k] = f'{minute}分{seconds}秒'

                # 多对多关系的
                elif k in ['tags', 'blog_list']:
                    con[k] = [str(tag.to_dict(exclude_list=exclude_list, extra_map=extra_map)) for tag in
                              obj_v.all()]
                # 文件
                elif k in ['avatar', 'path']:

                    v = str(obj_v).strip('/')
                    if not v.startswith('http'):
                        if 'media' not in v:
                            v = f'..{MEDIA_URL}{v}'
                    con[k] = v
                # 一般字段
                else:
                    con[k] = obj_v

        return con

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
    @my_cache(timeout=60 * 60)
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
class BackgroundMusic(models.Model, BaseModel):
    # 歌名
    title = models.CharField(max_length=50, db_column='歌名', verbose_name='歌名', help_text='歌名')

    # 歌手
    singer = models.CharField(max_length=30, db_column='歌手', verbose_name='歌手', help_text='歌手')

    # 歌曲图片
    avatar = models.ImageField(upload_to='image/%Y/%m/%d', db_column='图片', verbose_name='图片', help_text='图片')

    # 歌曲地址
    path = models.FileField(upload_to='audio/%Y/%m/%d', db_column='地址', verbose_name='地址', help_text='地址')

    class Meta:
        db_table = '背景音乐'
        verbose_name = verbose_name_plural = db_table

    fields = ['id', 'title', 'singer', 'avatar', 'path']

    def to_dict(self, fields=fields, exclude_list=[], extra_map={}) -> dict:
        return super().to_dict(fields, exclude_list, extra_map)

    @classmethod
    @my_cache(60)
    def get_all(cls, fields=fields):
        return [music.to_dict(fields=fields) for music in cls.objects.all()]
