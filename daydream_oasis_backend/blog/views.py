from datetime import datetime, timedelta
from django.core.cache import cache
from django.shortcuts import render
from blog.serializers import BlogSerializers, CategorySerializers,TagSerializers
from common.views import MyPage
from common.views import common_data
from blog.models import Comment, Collection, Blog, Search, Like, Category, Tag
from log.models import Action
from rest_framework import viewsets
from rest_framework.decorators import action


class BlogViewSet(viewsets.ModelViewSet):
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
    def serach(self, request, *args, **kwargs):
        # 关键词
        keyword = request.GET.get('keyword', '')[:20]
        category = request.GET.get('category', '')
        tag = request.GET.get('tag', '')

        # 保存搜索记录
        if keyword:
            Search.create(keyword, request.user)

        # 获取关键词
        keyword_list = Search.get_keyword_list(keyword)

        if not keyword_list:

            # 首页
            search_list = Blog.objects.filter(is_deleted=False).only('id', 'title', 'author', 'avatar', 'category',
                                                                     'abstract', 'create_time')
            placeholder = '请输入关键词'

            # 分类搜索
            if category:
                search_list = search_list.filter(category__title=category)
                placeholder = f'找到{len(search_list)}篇内容' if len(search_list) else '无相关内容'

            # 标签搜索
            if tag:
                search_list = search_list.filter(tags__title__contains=tag)
                placeholder = f'找到{len(search_list)}篇内容' if len(search_list) else '无相关内容'

            # 个性推荐
            user = request.user.id if request.user.is_authenticated else request.COOKIES.get('uuid', '-')

            # 通过缓存获取推荐列表，如果没有就不进行推荐
            recommend_list = cache.get(f'{user}_recommend_list')
            if recommend_list:
                search_list = recommend_list

        else:
            search_list = Blog.search(keyword_list)
            placeholder = f'找到{len(search_list)}篇内容' if len(search_list) else '无相关内容'
        # 分页
        page_num = request.GET.get('page', '1')  # 获取页码，如果没有获取到则默认为1
        # 分页
        page, blog_list = MyPage.get_blog_list(search_list, page=page_num, per_page=10)
        page_dict = MyPage.to_dict(page)

        return page, page_dict, blog_list, placeholder

    @action(methods=['get'], detail=False)
    def top_list(self, request, *args, **kwargs):
        '''排行榜'''


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializers
    queryset = Category.objects.all()


    def list(self, request, *args, **kwargs):
        '分类列表'

class TagViewSet:
    serializer_class = TagSerializers
    queryset = Tag.objects.all()

class SectionViewSet:
    serializer_class = TagSerializers
    queryset = Tag.objects.all()


# @cache_page(timeout=60)
def index(request, blog_id):
    # index页中的数据
    blog_list, page_dict = [], {}
    placeholder = '请输入关键词'

    if request.method == 'GET':

        # 判断该用户是否收藏了本文
        blog = Blog.get_by_id(blog_id)
        collection_id, is_collected = Collection.is_collected(request.user, blog)
        like_id, is_liked = Like.is_liked(request.user, blog)
        likes = Like.get_count_by_blog(blog)

        # 如果是本文作者就可以对本文进行编辑
        is_author = 1 if request.user.is_authenticated and request.user == blog.author and not blog.is_deleted else 0
        tags = blog.tags.all()

        # 计算当前距离明天的时间
        now = datetime.now()
        expired = (timedelta(hours=24, minutes=0, seconds=0) - timedelta(hours=now.hour, minutes=now.minute,
                                                                         seconds=now.second)).seconds
        # 数据统计
        blog_dpv = cache.get(f'blog_dpv_{blog_id}', 0) + 1  # 日浏览量
        blog_duv_set = cache.get(f'blog_duv_{blog_id}', set())  # 日访客量
        blog_uv_set = cache.get(f'blog_uv_{blog_id}', set())  # 访客量

        ip = request.META.get('REMOTE_ADDR')
        blog.pv += 1  # 浏览量加一
        blog_uv_set.add(ip)
        blog_duv_set.add(ip)
        cache.set(f'blog_dpv_{blog_id}', blog_dpv, expired)
        cache.set(f'blog_duv_{blog_id}', blog_duv_set, expired)
        cache.set(f'blog_uv_{blog_id}', blog_uv_set)

        blog.dpv = blog_dpv
        blog.uv = len(blog_uv_set)
        blog.duv = len(blog_duv_set)
        blog.save()

        # 判断原文是否被作者删除
        if blog.is_deleted: blog.content = '原文已被作者删除!'
        # 阅读时长
        blog.transform_read_time()
        # 评论列表
        comment_list = Comment.get_all_by_blog(blog_id)

        context = locals()
        context.update(common_data(request))

        # 用户行为记录
        user = request.user if request.user.is_authenticated else None
        _uuid = request.COOKIES.get('uuid', '-')
        Action.create(user, _uuid, blog, Action.CLICK, 0)

        return render(request, 'article.html', context=context)
