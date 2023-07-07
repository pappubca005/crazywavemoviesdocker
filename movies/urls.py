from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.MainHome, name="MainHome"),
    # path("detail", views.detail_view, name="detailview"),
    path("movie_detail/<movie_id>", views.movie_detail, name="movie_detail"),
    # path("movie_details/<movie_id>", views.movie_details, name="movie_details"),
    # path("add_movie/", views.add_movie, name="add_movie"),
    # path("search_details/", views.search_details, name="search_details"),
]
