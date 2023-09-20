from blog.serializers import BlogSerializers, CategorySerializers, TagSerializers, CommentSerializers, \
    CollectionSerializers, LikeSerializers
from blog.models import Comment, Collection, Blog, Like, Category, Tag
from log.models import Action
from rest_framework import viewsets
from rest_framework.decorators import action
from user.models import User
from common.drf.response import SucResponse
from common.drf.mixin import InstanceMixin

class BlogViewSet(viewsets.ModelViewSet,InstanceMixin):
    serializer_class = BlogSerializers
    queryset = Blog.objects.all()

    # 新增博客
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = self.request.user

    # 博客列表
    def list(self, request, *args, **kwargs):
        pass

    # 博客详情
    def retrieve(self, request, *args, **kwargs):
        pass

    # 更新博客
    def update(self, request, *args, **kwargs):
        ...

    # 删除博客
    def destroy(self, request, *args, **kwargs):
        serizliser = self.get_serializer(data=self.request.data, include_fields=['id'])
        serizliser.is_valid(raise_exception=True)
        blog = Blog.objects.filter(id=id).first()
        blog.delete()
        return

    @action(methods=['get'], detail=False)
    def top_list(self, request, *args, **kwargs):
        '''排行榜'''


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs):
        '分类列表'


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


class SectionViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


# 评论
class CommentViewSet(viewsets.ModelViewSet,InstanceMixin):
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

        comment = self.get_object(raise_on_not_found=True)

        # 用户行为记录
        user = request.user if request.user.is_authenticated else None
        _uuid = request.COOKIES.get('uuid', '-')
        Action.create(user, _uuid, comment.blog, Action.CANCEL_COMMENT, 0)

        return SucResponse()

    def create(self, request, *args, **kwargs):

        res = super().create(request, *args, **kwargs)

        # 用户行为记录
        user = request.user if request.user.is_authenticated else None
        _uuid = request.COOKIES.get('uuid', '-')
        blog = Blog.get_by_id(request.data.get('blog'))
        Action.create(user, _uuid, blog, Action.COMMENT, 0)

        return res


# 收藏
class CollectionViewSet(viewsets.ModelViewSet):
    serializer_class = CollectionSerializers
    queryset = Collection.objects.all()

    def update(self, request, pk=None, *args, **kwargs):
        collection = Collection.get_by_id(pk)
        if not collection:
            collection = Collection()
            user_id = request.data.get('user')
            blog_id = request.data.get('blog')
            blog = Blog.get_by_id(blog_id)
            user = User.get_by_id(user_id)
            collection.user = user
            collection.blog = blog
            collection.is_canceled = False

        collection.is_canceled = int(request.data.get('is_canceled'))
        collection.save()

        # 用户行为记录
        user = request.user if request.user.is_authenticated else None
        _uuid = request.COOKIES.get('uuid', '-')
        action = Action.COLLECT if not collection.is_canceled else Action.CANCEL_COLLECT
        Action.create(user, _uuid, collection.blog, action, 0)

        return SucResponse()


# 点赞
class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializers
    queryset = Like.objects.all()

    def update(self, request, pk=None, *args, **kwargs):
        like = Like.get_by_id(pk)
        if not like:
            like = Like()
            user_id = request.data.get('user')
            blog_id = request.data.get('blog')
            user = User.get_by_id(user_id)
            blog = Blog.get_by_id(blog_id)
            like.user = user
            like.blog = blog
            like.is_canceled = False

        like.is_canceled = int(request.data.get('is_canceled'))
        like.save()

        # 用户行为记录
        user = request.user if request.user.is_authenticated else None
        _uuid = request.COOKIES.get('uuid', '-')
        action = Action.DOCALL if not like.is_canceled else Action.CANCEL_DOCALL
        Action.create(user, _uuid, like.blog, action, 0)

        return SucResponse()
