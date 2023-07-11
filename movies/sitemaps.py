from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse

from .models import PopularMovies


class StaticViewSitemap(Sitemap):
    changefreq = "always"
    priority = 0.9

    def items(self):
        return ["about"]
        # return PopularMovies.objects.all()

    def location(self, item):
        return reverse(item)
        # return item.updated


class MovieViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return PopularMovies.objects.all()
