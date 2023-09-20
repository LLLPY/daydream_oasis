from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.cache import cache_page
from django.views.static import serve
from daydream_oasis_backend.admin_site import my_site
from daydream_oasis_backend.rss import LatestBlogFeed
from daydream_oasis_backend.config.base import MEDIA_ROOT
from django.contrib.sitemaps import views as sitemap_views
from daydream_oasis_backend.sitemap import BlogSitemap
from rest_framework.documentation import include_docs_urls
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from blog.views import CategoryViewSet, BlogViewSet, TagViewSet, CommentViewSet, CollectionViewSet, LikeViewSet
from frontconfig.views import FrontConfigViewSet
from file.views import FileViewSet
# from log.views import
from user.views import UserViewSet

# 路由注册
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'collection', CollectionViewSet, basename='collection')
router.register(r'like', LikeViewSet, basename='like')
# router.register(r'log', LikeViewSet, basename='log')
router.register(r'user', UserViewSet, basename='user')
router.register(r'file', FileViewSet, basename='file')
router.register(r'frontconfig', FrontConfigViewSet, basename='frontconfig')

urlpatterns = [
    re_path(r'^api/', include((router.urls, 'api'), namespace='api')),  # 接口地址

    re_path(r'^admin/', my_site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),  # 访问media文件
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # 富文本
    re_path(r'^rss|feed$', cache_page(60 * 60, key_prefix='rss_cache')(LatestBlogFeed()), name='rss'),  # rss
    re_path(r'^sitemap$', cache_page(60 * 60, key_prefix='sitemap_cache')(sitemap_views.sitemap),
            {'sitemaps': {'posts': BlogSitemap}}),  # sitemap 使用缓存
    re_path(r'^api/docs/', include_docs_urls(title='blog apis')),  # restful api接口文档

]

if settings.DEBUG: urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
