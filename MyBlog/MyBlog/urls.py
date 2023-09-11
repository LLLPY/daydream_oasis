from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, re_path
from django.views.decorators.cache import cache_page
from django.views.static import serve
from MyBlog.admin_site import my_site
from MyBlog.rss import LatestBlogFeed
from MyBlog.config.base import MEDIA_ROOT
from django.contrib.sitemaps import views as sitemap_views
from MyBlog.sitemap import BlogSitemap
from rest_framework.documentation import include_docs_urls
from user.views import index

urlpatterns = [

    re_path(r'^admin/', my_site.urls),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),  # 访问media文件
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),  # 富文本
    re_path(r'^rss|feed$', cache_page(60 * 60, key_prefix='rss_cache')(LatestBlogFeed()), name='rss'),  # rss
    re_path(r'^sitemap$', cache_page(60 * 60, key_prefix='sitemap_cache')(sitemap_views.sitemap),
            {'sitemaps': {'posts': BlogSitemap}}),  # sitemap 使用缓存

    re_path(r'^api/docs/', include_docs_urls(title='blog apis')),  # restful api接口文档
    re_path(r'^blog/', include(('blog.urls', 'blog'), namespace='blog')),  # blog
    re_path(r'^log/', include(('log.urls', 'log'), namespace='log')),  # 请求日志
    re_path(r'^user/', include(('user.urls', 'user'), namespace='user')),  # 用户相关
    re_path(r'^file/', include(('file.urls', 'file'), namespace='file')),  # 文件相关
    re_path(r'^$', index, name='index'),  # 首页

]

if settings.DEBUG:
    import debug_toolbar
    from MyBlog.config import settings_dev

    urlpatterns = [
                      re_path(r'^__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
