# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/18 10:36  
from rest_framework import serializers
from .models import Category, Tag, Blog, Comment, Collection, Search, Recommend, Like


# 博客分类
class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# 标签
class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


# 文章
class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


# 评论
class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# 收藏
class CollectionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = '__all__'


# 点赞
class LikeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
