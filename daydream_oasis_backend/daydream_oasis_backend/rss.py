from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed

from blog.models import Blog


class ExtendedRSSFeed(Rss201rev2Feed):
    def add_item_elements(self, handler, item):
        super(ExtendedRSSFeed, self).add_item_elements(handler, item)
        handler.addQuickElement('content:html', item['content_html'])


class LatestBlogFeed(Feed):
    feed_type = Rss201rev2Feed
    title = 'daydream_oasis'
    link = '/rss/'
    description = 'daydream_oasis is a blog system powered by django'

    def items(self):
        return Blog.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.abstract

    def item_link(self, item):
        return f'/api/blog/{item.pk}'
