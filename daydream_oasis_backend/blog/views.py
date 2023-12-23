from django.db.models import Q
from blog.serializers import (BlogSerializers, CategorySerializers,
                              TagSerializers, CommentSerializers,
                              CollectionSerializers, LikeSerializers, SearchSerializers, BlogCreateSerializers)
from blog.models import Comment, Collection, Blog, Like, Category, Tag, Share
from rest_framework import viewsets
from rest_framework.decorators import action
from common.drf.response import SucResponse
from common.drf.mixin import InstanceMixin
from common.views import BaseViewSet
from common.exception import exception
from log.views import action_log
from common.drf.decorators import login_required, rate_lock
from common.drf.pagination import CustomPagination


class BlogViewSet(BaseViewSet):
    serializer_class = BlogSerializers
    pagination_class = CustomPagination
    queryset = Blog.objects.all()

    def get_queryset(self):

        if self.action == 'list':
            return self.queryset.filter(is_draft=False)

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
        category = serializer.data.get('category')
        tag_list = serializer.data.get('tag_list')
        content = serializer.data.get('content')
        section = serializer.data.get('section')
        is_draft = serializer.data.get('is_draft')
        blog_id = serializer.data.get('id')
        print(serializer.data)
        new_blog_id = Blog.create_or_update(blog_id, title, user, category, tag_list, content, section, is_draft)
        if is_draft and not blog_id and new_blog_id:
            data = {'blog_id': new_blog_id}
        else:
            data = {}
        return SucResponse(message='新增博客成功!', data=data)

    # 博客列表
    def list(self, request, *args, **kwargs):
        detail = self.request.query_params.get('detail', 'false')
        is_all = self.request.query_params.get('is_all', 'false')
        detail = True if detail.lower() == 'true' else False
        is_all = True if is_all.lower() == 'true' else False
        if is_all:
            data = self.get_queryset()
            serializer = self.get_serializer(data, many=True)
            data = {"results": serializer.data}
        else:
            res = super().list(request, *args, **kwargs)
            data = res.data['data']
            if not detail:
                results = data['results']
                for blog_dict in results:
                    del blog_dict['content']
                    blog_dict['create_time'] = blog_dict['create_time'].split(' ')[0]
                    blog_dict['update_time'] = blog_dict['update_time'].split(' ')[0]
        return SucResponse(data=data)

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
                                             'tag_list',
                                             'pv',
                                             'read_times',
                                             'read_time',
                                             'create_time',
                                             'update_time',
                                         ])

        return SucResponse(data=serializer.data)

    # 更新博客
    @login_required
    def update(self, request, *args, **kwargs):
        ...

    # 删除博客
    @login_required
    def destroy(self, request, *args, **kwargs):
        super().destroy(request, *args, **kwargs)
        return SucResponse('删除成功!')

    @action(methods=['get'], detail=False)
    def top_list(self, request, *args, **kwargs):
        '''排行榜'''

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
        return SucResponse('取消收藏成功!')

    @action(methods=['get'], detail=False)
    @login_required
    def get_draft(self, request, *args, **kwargs):
        '''获取最后一次编辑但为提交的草稿'''
        user = self.request.user
        draft = Blog.get_draft(user.id)
        if draft:
            serializer = self.get_serializer(draft, include_fields=['id', 'title', 'avatar', 'category', 'tag_list',
                                                                    'content'])
            data = serializer.data
        else:
            data = {}
        print(data)
        return SucResponse(data=data)

    @action(methods=['get'], detail=False)
    def search(self, request, *args, **kwargs):
        '''根据条件搜索'''
        serializer = self.get_serializer(data=self.request.query_params,
                                         include_fields=['category', 'tag', 'author', 'keyword'])
        serializer.is_valid(raise_exception=True)
        # 分类 标签 作者 关键字
        filter_dict = {}
        category = serializer.data.get('category')
        tag = serializer.data.get('tag')
        author = serializer.data.get('author')
        keyword = serializer.data.get('keyword')

        queryset = self.get_queryset()

        if category:
            filter_dict.update(category__title=category)
        if tag:
            tag = Tag.objects.filter(title=tag).first()
            filter_dict.update(tag_list=tag)
        if author:
            filter_dict.update(author=author)

        queryset = queryset.filter(**filter_dict)
        if keyword:
            title_query = Q(title__icontains=keyword)
            content_query = Q(content__icontains=keyword)
            category_query = Q(category__title__icontains=keyword)
            queryset = queryset.filter(title_query | category_query | content_query)

        serializer = self.get_serializer(queryset, many=True)
        return SucResponse(data=serializer.data)


class CategoryViewSet(BaseViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def get_queryset(self):
        if self.action in ['list']:
            title = self.request.query_params.get('title')
            k = self.request.query_params.get('k')
            if title:
                self.queryset = self.queryset.filter(title__contains=title)
            # 限制数量
            if k and k.isnumeric():
                k = int(k)
                self.queryset = self.queryset[:k]
        return self.queryset

    def list(self, request, *args, **kwargs):
        '''分类列表'''
        serializer = self.get_serializer(data=self.request.query_params, include_fields=['id', 'title'])
        serializer.is_valid()
        res = super().list(request, *args, **kwargs)
        return res


class TagViewSet(CategoryViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


# 评论
@action_log()
class CommentViewSet(viewsets.ModelViewSet, InstanceMixin):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        # 指定评论的文章
        blog_id = request.GET.get('blog')
        results = res.data['data']['results']
        if blog_id:
            results = filter(lambda a: str(a['blog']) == blog_id, results)
        else:
            results = []
        res.data['data']['results'] = results

        return res

    # 将状态改为已删除即可
    def destroy(self, request, pk=None):
        super().destroy(request, pk=pk)
        return SucResponse('删除成功!')

    def create(self, request, *args, **kwargs):
        super().create(request, *args, **kwargs)
        return SucResponse()


# 收藏
@action_log()
class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializers
    queryset = Collection.objects.all()


# 点赞
@action_log()
class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializers
    queryset = Like.objects.all()
