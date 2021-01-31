from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import ModelPost

class LatestPostsFeed(Feed):
    title = 'Blog'
    link = '/post/'
    description = 'Latest posts'

    def items(self):
        return ModelPost.issued.all()

    def item_title(self, obj):
        return obj.title

    def item_description(self, obj):
        return truncatewords(obj.text, 30)