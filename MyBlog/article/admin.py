from django.contrib import admin
from MyBlog.admin_site import my_site
from user.admin import MyBaseAdmin
from article.adminforms import BlogAdminForm
from article.models import Comment, Collection, Tag, Blog, Category, Search, Recommend, Like
from user.models import User


# 分类
@admin.register(Category, site=my_site)
class CategoryAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'title', 'time', 'creator']
    search_fields = ['title', 'creator__username']  # 搜索的字段同list_display
    list_filter = ['title', 'creator__username', 'time']  # 过滤字段为前3个字段

    def used_count(self, obj):
        # 统计每个分类下的文章数量
        count = Blog.get_count_by_category_id(obj.id)
        return f'{count}'

    used_count.short_description = '文章数量'


# 标签
@admin.register(Tag, site=my_site)
class TagAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'title', 'time', 'creator']
    search_fields = ['title', 'creator__username']  # 搜索的字段同list_display
    list_filter = ['title', 'creator__username', 'time']  # 过滤字段为前3个字段


# 文章
@admin.register(Blog, site=my_site)
class BlogAdmin(admin.ModelAdmin, MyBaseAdmin):
    form = BlogAdminForm
    list_display = ['id','title', 'author', 'category', 'dpv', 'duv', 'pv', 'uv', 'likes',
                    'collections', 'comments', 'create_time', 'update_time', 'is_deleted', 'is_top', 'abstract']
    search_fields = ['id','title', 'author__username', 'category__title', 'abstract']
    list_filter = ['author__username', 'category__title', 'update_time', 'is_deleted']
    fieldsets = [
        ('基本信息', {
            'fields': ['title', 'avatar', 'author', 'category', 'tags'],
        }),
        ('数据', {
            'fields': ['create_time', 'update_time', 'dpv', 'duv', 'pv', 'uv'],
        }),
        ('状态', {
            'fields': ['is_deleted', 'is_top'],
        }),
        ('内容', {
            'fields': ['abstract', 'content'],
        }),
    ]

    # custom
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        # 非博主只能查看自己的文章
        if request.user != User.get_by_id('1'):
            queryset = queryset.filter(author=request.user)
        return queryset

    def likes(self, obj):
        return Like.get_count_by_blog(obj)

    likes.short_description = '点赞量'

    def collections(self, obj):
        return Collection.get_count_by_blog(obj)

    collections.short_description = '收藏量'

    def comments(self, obj):
        return Comment.get_count_by_blog(obj)

    comments.short_description = '评论量'


# 评论
@admin.register(Comment, site=my_site)
class CommentAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'user', 'blog', 'content', 'time', 'is_deleted']
    search_fields = ['user__username', 'content']
    list_filter = ['user__username', 'blog__title', 'time', 'is_deleted']


# 收藏
@admin.register(Collection, site=my_site)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'blog', 'is_canceled', 'time']
    search_fields = ['user', 'blog']
    list_filter = ['user', 'blog', 'is_canceled', 'time']


# 点赞
@admin.register(Like, site=my_site)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'blog', 'is_canceled', 'time']
    search_fields = ['user', 'blog']
    list_filter = ['user', 'blog', 'is_canceled', 'time']


# 搜索记录
@admin.register(Search, site=my_site)
class SearchAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'keyword', 'user', 'time']
    search_fields = ['keyword', 'user']
    list_filter = 'keyword', 'user', 'time'


# 相关推荐
@admin.register(Recommend, site=my_site)
class RecommendAdmin(admin.ModelAdmin, MyBaseAdmin):
    list_display = ['id', 'user']
