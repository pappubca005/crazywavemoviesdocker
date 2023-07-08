from django.shortcuts import render
from .models import Movies as MovieModel
from .models import SeriesModel
from tmdbv3api import TMDb, Movie, TV, Trending
import requests
import json

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ODI4MTFiOGU4MTE3YjEzZmFiZmNmMTVhMmViZmNlMyIsInN1YiI6IjY0OTI5NzcyYzI4MjNhMDBmZmEwNzJjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KlUxLqciegDaMNjCfQIuQDBPFQui5rHrtGdL9eyjQEo",
}
nowplaying_url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"
popular_url = "https://api.themoviedb.org/3/movie/popular?language=en-US&page=1"
toprated_url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1"
upcoming_url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1"


# Create your views here.
def MainHome(request):
    response = requests.get(nowplaying_url, headers=headers)
    nowplayingmovies = response.json()["results"][0:23]

    response = requests.get(popular_url, headers=headers)
    popularmovies = response.json()["results"][0:19]

    response = requests.get(toprated_url, headers=headers)
    topmovies = response.json()["results"][0:19]

    response = requests.get(upcoming_url, headers=headers)
    upcomingmovies = response.json()["results"][0:19]

    context = {
        "nowplayingmovies": nowplayingmovies,
        "popularmovies": popularmovies,
        "topmovies": topmovies,
        "upcomingmovies": upcomingmovies,
    }
    return render(request, "movies/final/index.html", context)


def movie_detail(request, movie_id):
    url = "https://api.themoviedb.org/3/movie/" + movie_id + "?language=en-US"

    response = requests.get(url, headers=headers)

    print(response.text)
    movie_detail = response.json()

    url = "https://api.themoviedb.org/3/movie/" + movie_id + "/images"

    response = requests.get(url, headers=headers)
    imagedetail = response.json()

    context = {
        "moviedetail": movie_detail,
        "imagedetail": imagedetail["backdrops"][0:15],
    }

    # print(context)
    # return render(request, "movies/final/movie_description.html", context)
    return render(request, "movies/final/movie_detail.html", context)
