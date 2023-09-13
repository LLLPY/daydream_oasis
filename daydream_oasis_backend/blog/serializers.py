# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/18 10:36  
from common.drf.serializers import DynamicFieldsSerializer
from rest_framework import serializers


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
    title = serializers.CharField(required=True, max_length=20, help_text='标题')
    avatar = serializers.URLField(required=True, help_text='封面')
    category = serializers.CharField(required=True, help_text='分类')
    tag_list = serializers.ListField(required=True, help_text='标签列表')
    content = serializers.CharField(required=True, min_length=5, help_text='内容')


# 评论
class CommentSerializers(DynamicFieldsSerializer):
    ...


# 收藏
class CollectionSerializers(DynamicFieldsSerializer):
    ...


# 点赞
class LikeSerializers(DynamicFieldsSerializer):
    ...
