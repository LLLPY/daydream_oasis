from blog.views import (BlogViewSet, CategoryViewSet, CollectionViewSet,
                        CommentViewSet, LikeViewSet, SectionViewSet,
                        TagViewSet)
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps import views as sitemap_views
from django.urls import include, re_path
from django.views.decorators.cache import cache_page
from django.views.static import serve
from file.views import FileViewSet
from frontconfig.views import FrontConfigViewSet
from log.views import ActionViewSet
from rest_framework.routers import DefaultRouter
from user.views import UserViewSet

from daydream_oasis_backend.admin_site import my_site
from daydream_oasis_backend.rss import LatestBlogFeed
from daydream_oasis_backend.settings.base import MEDIA_ROOT
from daydream_oasis_backend.sitemap import BlogSitemap

# 路由注册
router = DefaultRouter()
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'section', SectionViewSet, basename='section')
router.register(r'blog', BlogViewSet, basename='blog')
router.register(r'tag', TagViewSet, basename='tag')
router.register(r'comment', CommentViewSet, basename='comment')
router.register(r'collection', CollectionViewSet, basename='collection')
router.register(r'like', LikeViewSet, basename='like')
router.register(r'action_log', ActionViewSet, basename='action_log')
router.register(r'user', UserViewSet, basename='user')
router.register(r'file', FileViewSet, basename='file')
router.register(r'frontconfig', FrontConfigViewSet, basename='frontconfig')

urlpatterns = [
    re_path(r'^api/', include((router.urls, 'api'), namespace='api')),  # 接口地址

    re_path(r'^api/admin/', my_site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),  # 访问media文件
    re_path(r'^api/rss|feed$', cache_page(60 * 60, key_prefix='rss_cache')
            (LatestBlogFeed()), name='rss'),  # rss
    re_path(r'^api/sitemap$', cache_page(60 * 60, key_prefix='sitemap_cache')(sitemap_views.sitemap),
            {'sitemaps': {'posts': BlogSitemap}}),  # sitemap 使用缓存
    # re_path(r'^api/docs/', include_docs_urls(title='blog apis')),  # restful api接口文档

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
