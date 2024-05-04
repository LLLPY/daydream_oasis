import datetime
import json
import time
import uuid

import requests
from blog.models import (Blog, Category, Collection, Comment, Like, Section,
                         Share, Tag)
from blog.serializers import (BlogCreateSerializers, BlogSerializers,
                              CategorySerializers, CollectionSerializers,
                              CommentSerializers, LikeSerializers,
                              SearchSerializers, SectionSerializers,
                              TagSerializers)
from common.drf.decorators import login_required, rate_lock
from common.drf.mixin import InstanceMixin
from common.drf.pagination import CustomPagination
from common.drf.response import SucResponse
from common.exception import exception
from common.views import BaseViewSet
from django.db.models import Q
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from log.models import Action
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from user.models import User
from utils import tools


class BlogViewSet(BaseViewSet):
    serializer_class = BlogSerializers
    pagination_class = CustomPagination
    queryset = Blog.objects.all()

    def get_queryset(self):

        if self.action == 'list':
            queryset = self.queryset.filter(is_draft=False, is_nav=False)
            queryset = self.filter_search(queryset, self.request.query_params)
            return queryset
        elif self.action == 'get_draft_list':
            queryset = self.queryset.filter(is_draft=True, author=self.request.user)
            return queryset
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'search':
            return SearchSerializers
        elif self.action == 'create':
            return BlogCreateSerializers

        return self.serializer_class

    # 新增博客
    @login_required
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user
        title = serializer.data.get('title')
        avatar = serializer.data.get('avatar')
        category = serializer.data.get('category')
        tag_list = serializer.data.get('tag_list')
        content = serializer.data.get('content')
        section = serializer.data.get('section')
        is_draft = serializer.data.get('is_draft')
        blog_id = serializer.data.get('id')
        new_blog_id = Blog.create_or_update(
            blog_id, title, avatar, user, category, tag_list, content, section, is_draft)
        if is_draft and not blog_id and new_blog_id:
            data = {'blog_id': new_blog_id}
        else:
            data = {}
        return SucResponse(message='新增博客成功!', data=data)

    # 博客列表
    @method_decorator(cache_page(timeout=5*60, key_prefix='daydream_oasis:list'))
    def list(self, request, *args, **kwargs):
        detail = self.request.query_params.get('detail', 'false')
        detail = detail.lower() == 'true'
        res = super().list(request, *args, **kwargs)
        data = res.data['data']
        if not detail:
            results = data['results']
            for blog_dict in results:
                del blog_dict['content']
                blog_dict['create_time'] = blog_dict['create_time'].split(' ')[0]
                blog_dict['update_time'] = blog_dict['update_time'].split(' ')[0]
        return SucResponse(data=data)

    @action(methods=['get'], detail=False)
    @login_required
    def get_draft_list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), include_fields=['id', 'title'], many=True)
        return SucResponse(data=serializer.data)

    # 博客详情
    def retrieve(self, request, *args, **kwargs):

        blog = self.get_object()
        serializer = self.get_serializer(blog,
                                         include_fields=[
                                             'id',
                                             'title',
                                             'author',
                                             'avatar',
                                             'category',
                                             'section',
                                             'tag_list',
                                             'pv',
                                             'read_times',
                                             'read_time',
                                             'create_time',
                                             'update_time',
                                             'content'
                                         ])
        # 一天之内一台设备只算一次浏览量
        uuid = request.COOKIES.get('uuid', '-')
        key = f'view:{uuid}:{blog.id}'
        if self.redis_conn.setnx(key, 'viewed'):
            Action.create(blog.id, Action.CLICK, 0, request)
            now = datetime.datetime.now()
            expired = (datetime.timedelta(hours=24, minutes=0, seconds=0) - datetime.timedelta(hours=now.hour, minutes=now.minute,
                                                                                               seconds=now.second)).seconds
            self.redis_conn.expire(key, expired)

        return SucResponse(data=serializer.data)

    # 更新博客
    @login_required
    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        user = self.request.user
        if obj.author_id != user.id:
            raise exception.CustomValidationError('无权限编辑!')
        obj.is_draft = True
        obj.save()
        return SucResponse()

    # 删除博客
    @login_required
    def destroy(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author_id != request.user.id:
            raise exception.CustomValidationError('无权限编辑!')
        obj.delete()
        return SucResponse('删除成功!')

    @action(methods=['get'], detail=True)
    def action_info(self, request, *args, **kwargs):
        '''点赞，收藏，分享等行为信息'''
        blog = self.get_object()
        user = self.request.user

        # 获取点赞次数和当前的点赞状态
        liked_count = Like.get_count(blog=blog)
        _, has_liked = Like.status(blog=blog, user=user)

        # 获取收藏次数和当前的收藏状态
        collected_count = Collection.get_count(blog=blog)
        _, has_collected = Collection.status(blog=blog, user=user)

        # 获取分享次数
        shared_count = Share.get_count(blog=blog)

        data = {
            'liked_count': liked_count,
            'has_liked': has_liked,
            'collected_count': collected_count,
            'has_collected': has_collected,
            'shared_count': shared_count
        }

        return SucResponse(data=data)

    @action(methods=['post'], detail=True)
    @login_required
    @rate_lock()
    def like(self, request, *args, **kwargs):
        '''点赞'''

        user = self.request.user
        blog = self.get_object()
        _, has_liked = Like.status(blog=blog, user=user)
        if has_liked:
            raise exception.CustomValidationError('已经点过赞啦!')
        Like.create(blog, user)

        # 行为记录
        Action.create(blog.id, Action.DOCALL, 0, request)

        # 邮件通知
        tools.send_email(
            subject="博客点赞通知！",
            message='',
            blog_title=blog.title,
            blog_id=blog.id,
            operator_username=user.username,
            recipient_list=[blog.author.email],
            action='like'
        )

        return SucResponse('点赞成功!')

    @action(methods=['post'], detail=True)
    @login_required
    @rate_lock()
    def cancel_like(self, request, *args, **kwargs):
        '''取消点赞'''

        user = self.request.user
        blog = self.get_object()
        like_obj, has_liked = Like.status(blog=blog, user=user)
        if has_liked:
            like_obj.delete()
        else:
            raise exception.CustomValidationError('还未点赞!')
        # 行为记录
        Action.create(blog.id, Action.CANCEL_DOCALL, 0, request)
        return SucResponse('取消点赞成功!')

    @action(methods=['post'], detail=True)
    @login_required
    @rate_lock()
    def collect(self, request, *args, **kwargs):
        '''收藏'''
        user = self.request.user
        blog = self.get_object()
        _, has_collected = Collection.status(blog=blog, user=user)
        if has_collected:
            raise exception.CustomValidationError('已经收藏啦!')
        Collection.create(blog, user)

        # 行为记录
        Action.create(blog.id, Action.COLLECT, 0, request)

        # 邮件通知
        tools.send_email(
            subject="博客收藏通知！",
            message='',
            blog_title=blog.title,
            blog_id=blog.id,
            operator_username=user.username,
            recipient_list=[blog.author.email],
            action='collect'
        )
        return SucResponse('收藏成功!')

    @action(methods=['post'], detail=True)
    @login_required
    @rate_lock()
    def cancel_collect(self, request, *args, **kwargs):
        '''取消收藏'''

        user = self.request.user
        blog = self.get_object()
        collect_obj, has_collected = Collection.status(blog=blog, user=user)
        if has_collected:
            collect_obj.delete()
        else:
            raise exception.CustomValidationError('还未收藏!')
        # 行为记录
        Action.create(blog.id, Action.CANCEL_COLLECT, 0, request)
        return SucResponse('取消收藏成功!')

    @action(methods=['get'], detail=False)
    @login_required
    def get_draft(self, request, *args, **kwargs):
        '''获取最后一次编辑但未提交的草稿'''
        user = self.request.user
        blog_id = self.request.query_params.get('id')
        draft = self.queryset.filter(id=blog_id, author_id=user.id).first()
        if draft:
            serializer = self.get_serializer(draft, include_fields=['id', 'title', 'avatar', 'category', 'section', 'tag_list',
                                                                    'content'])
            data = serializer.data
        else:
            data = {}
        return SucResponse(data=data)

    def filter_search(self, queryset, params):
        filter_dict = {}
        # 分类
        category = params.get('category')
        if category:
            filter_dict.update(category__title=category)
        section = params.get('section')
        # 专栏
        if section:
            filter_dict.update(section__title=section)
        # 标签
        tag = params.get('tag')
        if tag:
            tag = Tag.objects.filter(title=tag).first()
            filter_dict.update(tag_list=tag)
        # 作者
        author = params.get('author')
        if author:
            filter_dict.update(author__username=author)

        queryset = queryset.filter(**filter_dict)

        # 关键字
        keyword = params.get('keyword')
        if keyword:
            title_query = Q(title__icontains=keyword)
            category_query = Q(category__title__icontains=keyword)
            content_query = Q(content__icontains=keyword)
            queryset = queryset.filter(title_query | category_query | content_query)
        return queryset

    @method_decorator(cache_page(timeout=60, key_prefix='daydream_oasis:search'))
    @action(methods=['get'], detail=False)
    def search(self, request, *args, **kwargs):
        '''根据条件搜索'''
        serializer = self.get_serializer(data=self.request.query_params,
                                         include_fields=['category', 'tag', 'author', 'keyword'])
        serializer.is_valid(raise_exception=True)
        # 分类 标签 作者 关键字
        queryset = self.get_queryset()
        queryset = self.filter_search(queryset, serializer.data)

        serializer = BlogSerializers(queryset, many=True, exclude_fields=['content'])
        return SucResponse(data=serializer.data)


class CategoryViewSet(BaseViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def get_queryset(self):
        if self.action in ['list']:
            title = self.request.query_params.get('title')
            k = self.request.query_params.get('k')
            queryset = self.queryset
            if title:
                queryset = self.queryset.filter(title__contains=title)
            # 限制数量
            if k and k.isnumeric():
                k = int(k)
                queryset = queryset[:k]
            return queryset
        return self.queryset

    def list(self, request, *args, **kwargs):
        '''分类列表'''
        serializer = self.get_serializer(
            data=self.request.query_params, include_fields=['id', 'title'])
        serializer.is_valid()
        res = super().list(request, *args, **kwargs)
        return res


class TagViewSet(CategoryViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


class SectionViewSet(CategoryViewSet):
    serializer_class = SectionSerializers
    queryset = Section.objects.all()

    def get_queryset(self):
        if self.action in ['list']:
            # 只能选择自己的专栏
            queryset = self.queryset.filter(creator=self.request.user)
            title = self.request.query_params.get('title')
            k = self.request.query_params.get('k')
            if title:
                queryset = self.queryset.filter(title__contains=title)
            # 限制数量
            if k and k.isnumeric():
                k = int(k)
                queryset = queryset[:k]
            return queryset
        return self.queryset


# XMLParser 默认media_type='application/xml'
class TextXMLParser(JSONParser):
    media_type = 'text/plain'

# 评论


class CommentViewSet(viewsets.ModelViewSet, InstanceMixin):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()
    parser_classes = (TextXMLParser,)

    def create(self, request, *args, **kwargs):
        data = self.request.data
        _type = data.get('type')
        # 如果是提交评论，就走django的接口；否则就走discuss的接口
        if _type == 'COMMIT_COMMENT':
            obj = Comment()
            obj.content = data['content']
            obj.mail = data['mail']
            obj.nick = data['nick']
            obj.path = data['path']
            obj.pid = data['pid']
            obj.rid = data['rid']
            obj.site = data['site']
            obj.id = uuid.uuid4().hex[:24]
            obj.created = time.time_ns()//1000000
            obj.updated = obj.created
            obj.ip = request.META.get('REMOTE_ADDR', '')
            obj.ua = request.META.get('HTTP_USER_AGENT')
            obj.avatar = User.get_avatar_by_email(obj.mail)
            obj.save()
            serializer = self.get_serializer(obj)
            data = {'msg': 'success', 'data': [serializer.data]}

            # 邮件通知
            blog_id = obj.path.split('?')[1].replace('id=', '')
            blog = Blog.objects.filter(id=blog_id).first()
            tools.send_email(
                subject="新的评论通知！",
                message=obj.content,
                blog_title=blog.title,
                blog_id=blog_id,
                operator_username=obj.nick,
                recipient_list=[blog.author.email],
                action='comment'
            )

        else:
            res = requests.post(url='http://127.0.0.1:6870', data=json.dumps(data))
            data = res.json()

        return SucResponse(**data)


# 收藏
class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializers
    queryset = Collection.objects.all()


# 点赞
class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializers
    queryset = Like.objects.all()
