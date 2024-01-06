from django.contrib import admin
from django.urls import path, include
from . import views
from .sitemaps import StaticViewSitemap, MovieViewSitemap
from django.contrib.sitemaps.views import sitemap
from django.views.generic import TemplateView

sitemaps = {"static": StaticViewSitemap, "movie_detail": MovieViewSitemap}


urlpatterns = [

    path('api/blocked', views.blocked_list, name="blockedlist" ),
    path('api/blocked/(?P<pk>[0-9]+)', views.blocked_detail, name="blockeddetail"),
    path('api/blocked/published', views.blocked_list_published, name="blockedpublished"),

    path("", views.MainHome, name="MainHome"),
    # path("detail", views.detail_view, name="detailview"),
    path(
        "movie_detail/<movie_id>/<movie_name>/", views.movie_detail, name="movie_detail"
    ),
    path(
        "movie_category/<movie_category>/",
        views.movie_category,
        name="movie_category",
    ),
    # path("movie_detail/<movie_id>", views.movie_detail, name="movie_detail_2"),
    path("movie_update", views.movie_update, name="movie_update"),
    path("update_link", views.updatelink, name="update_link"),
    path("about/", views.about, name="about"),
    
    path("sitemap.xml", sitemap, {"sitemaps": sitemaps}),
    # path("search_details/", views.search_details, name="search_details"),
    path(
        "robots.txt",
        TemplateView.as_view(
            template_name="movies/robots.txt", content_type="text/plain"
        ),
    ),
    path(
        "6e59aa9b995945ef8295d8e5c4528883.txt",
        TemplateView.as_view(
            template_name="movies/6e59aa9b995945ef8295d8e5c4528883.txt",
            content_type="text/plain",
        ),
    ),

]
