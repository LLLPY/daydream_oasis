from django.contrib.syndication.views import Feed
from django.urls import reverse
from django.utils.feedgenerator import Rss201rev2Feed
from blog.models import Blog


class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler,item)
        handler.addQuickElement('content:html',item['content_html'])


class LatestBlogFeed(Feed):
    feed_type = Rss201rev2Feed
    title='0318-SPACE Blog System'
    link='/rss/'
    description='0318-SPACE is a blog system power by django'

    def items(self):
        return Blog.get_all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.summary

    def item_link(self, item):
        return reverse('learningPlanet:index',args=[item.pk,])
