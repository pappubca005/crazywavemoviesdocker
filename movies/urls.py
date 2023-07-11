from django.contrib import admin
from django.urls import path, include
from . import views
from .sitemaps import StaticViewSitemap, MovieViewSitemap
from django.contrib.sitemaps.views import sitemap

sitemaps = {"static": StaticViewSitemap, "movie_detail": MovieViewSitemap}


urlpatterns = [
    path("", views.MainHome, name="MainHome"),
    # path("detail", views.detail_view, name="detailview"),
    path(
        "movie_detail/<movie_id>/<movie_name>/", views.movie_detail, name="movie_detail"
    ),
    # path("movie_detail/<movie_id>", views.movie_detail, name="movie_detail_2"),
    path("movie_update", views.movie_update, name="movie_update"),
    path("about", views.about, name="about"),
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    # path("movie_details/<movie_id>", views.movie_details, name="movie_details"),
    # path("add_movie/", views.add_movie, name="add_movie"),
    # path("search_details/", views.search_details, name="search_details"),
]
