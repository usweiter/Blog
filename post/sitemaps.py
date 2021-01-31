from django.contrib.sitemaps import Sitemap
from .models import ModelPost

class PostSitemap(Sitemap):
    changefreq = 'never'
    priority = 0.5

    def items(self):
        return ModelPost.issued.all()

    def lastmod(self, obj):
        return obj.updated