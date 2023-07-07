from django.shortcuts import render
from .models import Movies as MovieModel
from .models import SeriesModel
from tmdbv3api import TMDb, Movie, TV, Trending
import requests
import json


# Create your views here.
def MainHome(request):
    tmdb = TMDb()
    tmdb.api_key = "982811b8e8117b13fabfcf15a2ebfce3"
    movie = Movie()

    """m = movie.details(36668)
    print(m.title)
    print(m.overview)
    print(m.popularity)"""

    mobjten = MovieModel.objects.all()[:20]
    tmvobjten = []
    for i in mobjten:
        m = movie.details(i.tmvdbid)
        tmvobjten.append(m)

    popular = movie.popular()
    pplrobj = []
    for p in popular:
        pplrobj.append(p)

    mobjfft = MovieModel.objects.all()[20:50]
    tmvobjfft = []
    for i in mobjfft:
        m = movie.details(i.tmvdbid)
        tmvobjfft.append(m)

    toprated = movie.top_rated()
    tprobj = []
    for p in toprated:
        tprobj.append(p)

    user = request.user
    context = {
        "tmvobjten": tmvobjten,
        "pplrobj": pplrobj,
        "mobjfft": tmvobjfft,
        "tprobj": tprobj,
    }

    url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ODI4MTFiOGU4MTE3YjEzZmFiZmNmMTVhMmViZmNlMyIsInN1YiI6IjY0OTI5NzcyYzI4MjNhMDBmZmEwNzJjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KlUxLqciegDaMNjCfQIuQDBPFQui5rHrtGdL9eyjQEo",
    }

    response = requests.get(url, headers=headers)

    print(response.text)
    context = {"apiresult": response.json()["results"][0:12], "data": "this is test"}

    print(context)
    return render(request, "movies/final/base.html", context)


# def detail_view(request):
#     url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1"

#     headers = {
#         "accept": "application/json",
#         "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ODI4MTFiOGU4MTE3YjEzZmFiZmNmMTVhMmViZmNlMyIsInN1YiI6IjY0OTI5NzcyYzI4MjNhMDBmZmEwNzJjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KlUxLqciegDaMNjCfQIuQDBPFQui5rHrtGdL9eyjQEo",
#     }

#     response = requests.get(url, headers=headers)

#     print(response.text)
#     context = {"apiresult": response.json()["results"][0:12], "data": "this is test"}

#     print(context)
#     # return render(request, "movies/final/movie_description.html", context)
#     return render(request, "movies/final/movie_detail2.html", context)


def movie_detail(request, movie_id):
    url = "https://api.themoviedb.org/3/movie/" + movie_id + "?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ODI4MTFiOGU4MTE3YjEzZmFiZmNmMTVhMmViZmNlMyIsInN1YiI6IjY0OTI5NzcyYzI4MjNhMDBmZmEwNzJjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KlUxLqciegDaMNjCfQIuQDBPFQui5rHrtGdL9eyjQEo",
    }
    response = requests.get(url, headers=headers)

    print(response.text)
    movie_detail = response.json()

    url = "https://api.themoviedb.org/3/movie/" + movie_id + "/images"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ODI4MTFiOGU4MTE3YjEzZmFiZmNmMTVhMmViZmNlMyIsInN1YiI6IjY0OTI5NzcyYzI4MjNhMDBmZmEwNzJjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KlUxLqciegDaMNjCfQIuQDBPFQui5rHrtGdL9eyjQEo",
    }

    response = requests.get(url, headers=headers)
    imagedetail = response.json()

    context = {
        "moviedetail": movie_detail,
        "imagedetail": imagedetail["backdrops"][0:15],
    }

    print(context)
    # return render(request, "movies/final/movie_description.html", context)
    return render(request, "movies/final/movie_detail2.html", context)
