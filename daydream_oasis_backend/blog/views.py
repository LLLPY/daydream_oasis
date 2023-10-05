from blog.serializers import BlogSerializers, CategorySerializers, TagSerializers, CommentSerializers, \
    CollectionSerializers, LikeSerializers
from blog.models import Comment, Collection, Blog, Like, Category, Tag, Share
from rest_framework import viewsets
from rest_framework.decorators import action
from common.drf.response import SucResponse
from common.drf.mixin import InstanceMixin
from common.views import BaseViewSet
from common.exception import exception
from log.views import action_log


@action_log()
class BlogViewSet(BaseViewSet):
    serializer_class = BlogSerializers
    queryset = Blog.objects.all()

    # 新增博客
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user

        title = serializer.data.get('title')
        category = serializer.data.get('category')
        tag_list = serializer.data.get('tag_list')
        content = serializer.data.get('content')
        section = serializer.data.get('section')

        blog = Blog()
        blog.title = title
        blog.author = user
        blog.category = category
        blog.tags = tag_list
        blog.content = content
        blog.section = section
        blog.save()

        return SucResponse('新增博客成功!')

    # 博客列表
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        detail = self.request.query_params.get('detail', 'false')
        detail = True if detail.lower() == 'true' else False

        if detail:
            serializer = self.get_serializer(queryset, many=True)
        else:
            serializer = self.get_serializer(queryset, many=True,
                                             include_fields=['id', 'title', 'author', 'category', 'tags', 'summary',
                                                             'section'])

        data = serializer.data
        return SucResponse(data=data)

    # 博客详情
    def retrieve(self, request, *args, **kwargs):

        blog = self.get_object()

        serializer = self.get_serializer(blog)

        return SucResponse(data=serializer.data)

    # 更新博客
    def update(self, request, *args, **kwargs):
        ...

    # 删除博客
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
        liked_status = Like.status(blog=blog, user=user)

        # 获取收藏次数和当前的收藏状态
        collected_count = Collection.get_count(blog=blog)
        collected_status = Collection.status(blog=blog, user=user)

        # 获取分享次数
        shared_count = Share.get_count(blog=blog)

        data = {
            'liked_count': liked_count,
            'liked_status': liked_status,
            'collected_count': collected_count,
            'collected_status': collected_status,
            'shared_count': shared_count
        }

        return SucResponse(data=data)

    @action(methods=['get', 'post'], detail=True)
    def like(self, request, *args, **kwargs):
        '''点赞'''

        blog = self.get_object()

        key = f'like:{self.request.user.id}:{blog.id}'
        success = self.redis_conn.setnx(key, 'liked')
        if not success:
            return exception.CustomValidationError('3秒内不能重复点赞哟!')

        # 3秒内只能点一次赞
        self.redis_conn.expire(key, 3)

        like_obj = Like()
        like_obj.user = self.request.user
        like_obj.blog = blog
        like_obj.save()

        return SucResponse('点赞成功!')


class CategoryViewSet(BaseViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        '分类列表'


class TagViewSet(BaseViewSet):
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
