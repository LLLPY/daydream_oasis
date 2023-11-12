# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/1/18 10:36
from common.drf.serializers import DynamicFieldsSerializer
from rest_framework import serializers
from log.models import Action
import re

# 博客分类
class CategorySerializers(DynamicFieldsSerializer):
    title = serializers.CharField(required=True, help_text='分类名')


# 标签
class TagSerializers(DynamicFieldsSerializer):
    title = serializers.CharField(required=True, help_text='标签名')


# 专栏
class SectionSerializers(DynamicFieldsSerializer):
    title = serializers.CharField(required=True, help_text='专栏名')


# 文章
class BlogSerializers(DynamicFieldsSerializer):
    id = serializers.IntegerField(help_text='id')
    title = serializers.CharField(required=True, max_length=20, help_text='标题')
    author = serializers.SerializerMethodField()
    # author = serializers.CharField()
    avatar = serializers.URLField(required=True, help_text='封面')
    category = serializers.CharField(required=True, help_text='分类')
    tag_list = serializers.SerializerMethodField(help_text='标签列表')
    content = serializers.CharField(required=True,
                                    min_length=5,
                                    help_text='内容')
    abstract = serializers.SerializerMethodField()
    pv = serializers.SerializerMethodField()
    read_times = serializers.IntegerField()
    read_time = serializers.SerializerMethodField()
    create_time = serializers.DateTimeField(format='%Y.%m.%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y.%m.%d %H:%M:%S')

    def get_author(self, obj):
        return {'id': obj.author.id, 'username': obj.author.username}

    def get_read_time(self, obj):
        obj.update_read_time()
        return obj.transform_read_time()

    def get_tag_list(self, obj):
        return map(lambda item: item['title'],
                   obj.tag_list.all().values('title'))

    def get_pv(self, obj):
        return Action.objects.filter(blog=obj).values('id').count()

    def get_abstract(self, obj):
        abstract = obj.abstract
        if not abstract:
            content = obj.content
            content = re.sub(r'---.*---', '', content)
            content = re.sub(r'<BlogInfo.*?/>', '', content)
            content = re.sub(r'<ActionBox />', '', content)
            abstract = ''.join(re.findall(r'[\u4e00-\u9fa5a-zA-Z\s\n]+', content))[:150].replace('\n','')
        return abstract


# 评论
class CommentSerializers(DynamicFieldsSerializer):
    ...


# 收藏
class CollectionSerializers(DynamicFieldsSerializer):
    ...


# 点赞
class LikeSerializers(DynamicFieldsSerializer):
    ...
