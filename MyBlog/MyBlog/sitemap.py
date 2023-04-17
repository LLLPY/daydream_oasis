from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from article.models import Blog

class BlogSitemap(Sitemap):
    changefreq='always'
    priority=1.0
    protocol = 'http'

    #返回所有正常状态的文章
    def items(self):
        return Blog.get_all()

    #返回每篇文章的创建时间
    def lastmod(self,obj):
        return obj.createdTime

    #返回每篇文章的url
    def location(self, obj):
        print(obj.pk)
        return reverse('learningPlanet:index',args=(obj.pk,))
