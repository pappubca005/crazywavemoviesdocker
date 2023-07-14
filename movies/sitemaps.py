from typing import Any, Dict, List, Optional, Union
from django.contrib.sitemaps import Sitemap
from django.contrib.sites.models import Site
from django.contrib.sites.requests import RequestSite
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
    protocol = "https"

    # def get_urls(self, site=None, **kwargs):
    #     site = Site(domain="https://oyemovies.shop", name="oyemovies.shop")
    #     return super(MovieViewSitemap, self).get_urls(site=site, **kwargs)

    def items(self):
        return PopularMovies.objects.all()
