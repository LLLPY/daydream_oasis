# -*- coding: UTF-8 -*-                            
# @Author  ：LLL                         
# @Date    ：2023/1/18 10:43
from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.response import Response
from log.models import Action
from user.models import User
from .serializers import CategorySerializers, TagSerializers, ArticleSerializers, CommentSerializers, \
    CollectionSerializers, LikeSerializers
from .models import Category, Tag, Blog, Comment, Collection, Like
from common.apis import MyBaseViewSet, require_login


# 分类
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()

    def list(self, request, *args, **kwargs) -> JsonResponse:
        category_list = []
        keyword = request.GET.get('keyword', '').lower()

        for item in Category.get_all().items():
            category = item[0].lower()
            if category.find(keyword) != -1 or keyword.find(category) != -1:
                category_list.append((item[0], item[1]['times']))

        category_list.sort(key=lambda a: -a[1])

        category_list = [item[0] for item in category_list[:10]]

        return JsonResponse({
            'code': '200',
            'msg': '响应成功!',
            'data': {
                'category_list': category_list[:8]
            }

        })


# 标签
class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializers
    queryset = Tag.objects.all()

    def list(self, request, *args, **kwargs) -> JsonResponse:
        tag_list = []
        keyword = request.GET.get('keyword', '').lower()

        for item in Tag.get_all().items():
            tag = item[0].lower()
            if tag.find(keyword) != -1 or keyword.find(tag) != -1:
                tag_list.append((item[0], item[1]['times']))

        tag_list.sort(key=lambda a: -a[1])

        tag_list = [item[0] for item in tag_list[:10]]

        return JsonResponse({
            'code': '200',
            'msg': '响应成功!',
            'data': {
                'tag_list': tag_list[:8]
            }

        })

# 文章
class ArticleViewSet(MyBaseViewSet):
    serializer_class = ArticleSerializers
    queryset = Blog.objects.all()

    @require_login(require_self=True)
    def destroy(self, request, pk=None) -> JsonResponse:
        blog = Blog.get_by_id(pk)
        if not blog:
            return JsonResponse({
                'code': '400',
                'msg': '删除失败,未找到相应博客!'
            })

        blog.is_deleted = True
        blog.save()
        return JsonResponse({
            'code': '200',
            'msg': '删除成功!'
        })

    @require_login(require_self=True)
    def create(self, request, *args, **kwargs) -> JsonResponse:
        user = request.user
        blog_id = request.data.get('blog_id', '-1') or '-1'
        title = request.data.get('title', '')
        if not title:
            return JsonResponse({
                'code': '400',
                'msg': '标题不能为空!'
            })

        category = request.data.get('category', '')
        if not category:
            return JsonResponse({
                'code': '400',
                'msg': '分类不能为空!'
            })

        category = Category.get_or_create(category, creator=user)
        content = request.data.get('content', '')
        if not content:
            return JsonResponse({
                'code': '400',
                'msg': '内容不能为空!'
            })

        tag_list = request.data.get('tag_list', [])
        avatar = request.data.get('avatar')
        blog = Blog.create_or_update(blog_id, title, avatar, category, tag_list, content, user)
        return JsonResponse({
            'code': '200',
            'msg': '响应成功!',
            'data': {
                'id': blog.id,
            }
        })


# 评论
class CommentViewSet(MyBaseViewSet):
    serializer_class = CommentSerializers
    queryset = Comment.objects.all()

    def list(self, request, *args, **kwargs) -> Response:
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
    @require_login(require_self=True)
    def destroy(self, request, pk=None) -> JsonResponse:
        comment = Comment.get_by_id(pk)

        if comment:
            comment.is_deleted = True
            comment.save()

            # 用户行为记录
            user = request.user if request.user.is_authenticated else None
            _uuid = request.COOKIES.get('uuid', '-')
            Action.create(user, _uuid, comment.blog, Action.CANCEL_COMMENT, 0)

            return JsonResponse({
                'code': '200',
                'msg': '删除成功!'
            })

    @require_login(require_self=True)
    def create(self, request, *args, **kwargs) -> Response:

        res = super().create(request, *args, **kwargs)

        # 用户行为记录
        user = request.user if request.user.is_authenticated else None
        _uuid = request.COOKIES.get('uuid', '-')
        blog = Blog.get_by_id(request.data.get('blog'))
        Action.create(user, _uuid, blog, Action.COMMENT, 0)

        return res


# 收藏
class CollectionViewSet(MyBaseViewSet):
    serializer_class = CollectionSerializers
    queryset = Collection.objects.all()

    @require_login(require_self=True)
    def update(self, request, pk=None, *args, **kwargs) -> JsonResponse:
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

        return JsonResponse({
            'code': '200',
            'msg': '更新成功!',
            'data': {
                'id': collection.id
            }
        })


# 点赞
class LikeViewSet(MyBaseViewSet):
    serializer_class = LikeSerializers
    queryset = Like.objects.all()

    @require_login()
    def update(self, request, pk=None, *args, **kwargs) -> JsonResponse:
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

        return JsonResponse({
            'code': '200',
            'msg': '更新成功!',
            'data': {
                'id': like.id
            }
        })
