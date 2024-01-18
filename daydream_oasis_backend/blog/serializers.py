# -*- coding: UTF-8 -*-
# @Author  ：LLL
# @Date    ：2023/1/18 10:36
from common.drf.serializers import DynamicFieldsSerializer
from rest_framework import serializers
from log.models import Action
import re


# 博客分类
class CategorySerializers(DynamicFieldsSerializer):
    id = serializers.IntegerField(required=False, allow_null=True)
    k = serializers.IntegerField(required=False, allow_null=True, help_text='数量')
    title = serializers.CharField(required=False, allow_null=True, help_text='分类名')


# 标签
class TagSerializers(CategorySerializers):
    ...


# 专栏
class SectionSerializers(DynamicFieldsSerializer):
    title = serializers.CharField(required=True, help_text='专栏名')


# 文章
class BlogSerializers(DynamicFieldsSerializer):
    id = serializers.IntegerField(help_text='id')
    title = serializers.CharField(required=True, max_length=30, help_text='标题')
    author = serializers.SerializerMethodField()
    # author = serializers.CharField()
    avatar = serializers.CharField(required=False, help_text='封面', allow_null=True)
    category = serializers.CharField(required=True, help_text='分类')
    tag_list = serializers.SerializerMethodField(help_text='标签列表')
    content = serializers.CharField(required=True,
                                    min_length=5,
                                    help_text='内容')
    abstract = serializers.SerializerMethodField()
    pv = serializers.SerializerMethodField()
    read_times = serializers.IntegerField()
    read_time = serializers.CharField()
    create_time = serializers.DateTimeField(format='%Y.%m.%d %H:%M:%S')
    update_time = serializers.DateTimeField(format='%Y.%m.%d %H:%M:%S')
    category_parent_list = serializers.SerializerMethodField()

    def get_author(self, obj):
        return {'id': obj.author.id, 'username': obj.author.username}

    def get_tag_list(self, obj):
        return list(map(lambda item: item['title'],
                        obj.tag_list.all().values('title')))

    def get_pv(self, obj):
        return Action.objects.filter(blog=obj).values('id').count()

    def get_abstract(self, obj):
        return obj.get_abstract()

    def get_category_parent_list(self, obj):
        return obj.category.get_parent_list()


class BlogCreateSerializers(DynamicFieldsSerializer):
    id = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    title = serializers.CharField(required=True, max_length=30, help_text='标题')
    avatar = serializers.CharField(required=False, allow_null=True, allow_blank=True, help_text='封面')
    category = serializers.CharField(required=True, help_text='分类')
    tag_list = serializers.ListField(help_text='标签列表')
    content = serializers.CharField(required=True,
                                    min_length=5,
                                    help_text='内容')
    is_draft = serializers.BooleanField()


# 评论
class CommentSerializers(DynamicFieldsSerializer):
    ...


# 收藏
class CollectionSerializers(DynamicFieldsSerializer):
    ...


# 点赞
class LikeSerializers(DynamicFieldsSerializer):
    ...


# 搜索
class SearchSerializers(BlogSerializers):
    keyword = serializers.CharField(required=False, allow_null=True, max_length=20, help_text='标题')
    author = serializers.CharField(required=False, allow_null=True, )
    category = serializers.CharField(required=False, allow_null=True, help_text='分类')
    tag = serializers.CharField(required=False, allow_null=True, help_text='标签')
    content = None
    # id = serializers.IntegerField(help_text='id')
    # title = serializers.CharField(required=True, max_length=20, help_text='标题')
    # avatar = serializers.URLField(required=True, help_text='封面')
    # tag_list = serializers.SerializerMethodField(help_text='标签列表')
    # abstract = serializers.SerializerMethodField()
    # pv = serializers.SerializerMethodField()
    # read_times = serializers.IntegerField()
    # read_time = serializers.SerializerMethodField()
    # create_time = serializers.DateTimeField(format='%Y.%m.%d %H:%M:%S')
    # update_time = serializers.DateTimeField(format='%Y.%m.%d %H:%M:%S')
    # category_parent_list = serializers.SerializerMethodField()
