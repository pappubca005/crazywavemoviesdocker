from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,Http404
from .models import Movies as MovieModel, PopularMovies,BlockedMovies
from .models import SeriesModel
from tmdbv3api import TMDb, Movie, TV, Trending
from .serializers import MoviesSerializer, PopularMoviesSerializer,BlockedMoviesSerializer
import requests
import datetime
import json
from decimal import Decimal
from django.core.serializers.json import DjangoJSONEncoder
import re
from rest_framework.decorators import api_view
from django.http import HttpResponse

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
movie = Movie()

tmdb = TMDb()
tmdb.api_key = "982811b8e8117b13fabfcf15a2ebfce3"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5ODI4MTFiOGU4MTE3YjEzZmFiZmNmMTVhMmViZmNlMyIsInN1YiI6IjY0OTI5NzcyYzI4MjNhMDBmZmEwNzJjNyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.KlUxLqciegDaMNjCfQIuQDBPFQui5rHrtGdL9eyjQEo",
}
nowplaying_url = "https://api.themoviedb.org/3/movie/now_playing?language=en-US"
popular_url = "https://api.themoviedb.org/3/movie/popular?language=en-US"
toprated_url = "https://api.themoviedb.org/3/movie/top_rated?language=en-US"
upcoming_url = "https://api.themoviedb.org/3/movie/upcoming?language=en-US"


def about(request):
    # return "this is about page"
    return HttpResponse("this is about page")




@api_view(['GET', 'POST', 'DELETE'])
def blocked_list(request):
    if request.method == 'GET':
        blockedmovies = BlockedMovies.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            blockedmovies = blockedmovies.filter(title__icontains=title)
        
        blockedmovies_serializer = BlockedMoviesSerializer(blockedmovies, many=True)
        return JsonResponse(blockedmovies_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        blockedmovies_data = JSONParser().parse(request)
        blockedmovies_serializer = BlockedMoviesSerializer(data=blockedmovies_data)
        if blockedmovies_serializer.is_valid():
            blockedmovies_serializer.save()
            return JsonResponse(blockedmovies_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(blockedmovies_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = BlockedMovies.objects.all().delete()
        return JsonResponse({'message': '{} blockedmovies were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 

# Create your views here.
def MainHome(request):
    response = requests.get(nowplaying_url + "&page=1", headers=headers)
    nowplayingmovies = response.json()["results"]
    # nowplayingmovies1 = (
    #     PopularMovies.objects.filter(movie_category__contains="nowplaying")
    #     .filter(vote_average__gte=8)
    #     .values()
    #     .order_by("-release_date")
    # )

    # nowplayingmovies = list(nowplayingmovies1)[0:39]

    # popularmovies1 = (
    #     PopularMovies.objects.filter(movie_category__contains="popular")
    #     .values()
    #     .order_by("-release_date")
    # )
    # popularmovies = list(popularmovies1)[0:39]

    response = requests.get(toprated_url + "&page=1", headers=headers)
    popularmovies = response.json()["results"]

    # topmovies1 = (
    #     PopularMovies.objects.filter(movie_category__contains="top")
    #     .values()
    #     .order_by("-release_date")
    # )
    # topmovies = list(topmovies1)[0:39]
    response = requests.get(toprated_url + "&page=1", headers=headers)
    topmovies = response.json()["results"]

    # upcomingmovies1 = (
    #     PopularMovies.objects.filter(movie_category__contains="upcoming")
    #     .values()
    #     .order_by("-release_date")
    # )
    # upcomingmovies = list(upcomingmovies1)[0:39]
    response = requests.get(upcoming_url + "&page=1", headers=headers)
    upcomingmovies = response.json()["results"]

    context = {
        "nowplayingmovies": nowplayingmovies,
        "popularmovies": popularmovies,
        "topmovies": topmovies,
        "upcomingmovies": upcomingmovies,
    }
    return render(request, "movies/final/index.html", context)


def movie_detail(request, movie_id, movie_name):
    print(movie_name)

    bm=BlockedMovies.objects.all().filter(id=movie_id).count()
    # bm = get_object_or_404(BlockedMovies, id=movie_id)
    if bm >=1:
        # return HttpResponse("movies doesn't exit")
        raise Http404
    else:

        # id = get_object_or_404(PopularMovies, id=movie_id)
        url = "https://api.themoviedb.org/3/movie/" + movie_id + "?language=en-US"

        response = requests.get(url, headers=headers)

        # print(response.text)

        movie_detail = response.json()
        movie_detail["release_year"] = movie_detail["release_date"][:4]
        url = "https://api.themoviedb.org/3/movie/" + movie_id + "/images"

        response = requests.get(url, headers=headers)
        imagedetail = response.json()

        context = {
            "moviedetail": movie_detail,
            "imagedetail": imagedetail["backdrops"][0:15],
        }

        return render(request, "movies/final/movie_detail.html", context)


class DecimalEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return str(o)  # Convert Decimal to string
        return super().default(o)


def movie_category(request, movie_category):
    if movie_category.lower() == "bollywood":
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&page=1&primary_release_year=2023&region=in&sort_by=popularity.desc&with_original_language=hi"
        response = requests.get(url, headers=headers)
        movie_cat_list = response.json()["results"]
    elif movie_category.lower() == "webseries":
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&page=1&primary_release_year=2023&region=in&sort_by=popularity.desc&with_original_language=hi"
        response = requests.get(url, headers=headers)
        movie_cat_list = response.json()["results"]
    elif movie_category.lower() == "tv":
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&page=1&primary_release_year=2023&region=in&sort_by=popularity.desc&with_original_language=hi"
        response = requests.get(url, headers=headers)
        movie_cat_list = response.json()["results"]
    elif movie_category.lower() == "premium":
        url = "https://api.themoviedb.org/3/discover/movie?include_adult=true&include_video=true&page=1&primary_release_year=2023&region=in&sort_by=popularity.desc&with_original_language=hi"
        response = requests.get(url, headers=headers)
        movie_cat_list = response.json()["results"]

    else:
        genres = {
            "action": 28,
            "adventure": 12,
            "animation": 16,
            "science fiction": 878,
            "crime": 80,
            "comedy": 35,
            "romance": 10749,
            "drama": 18,
            "thriller": 53,
            "documentary": 99,
            "horror": 27,
            "fantasy": 14,
            "family": 10751,
            "history": 36,
            "music": 10402,
            "war": 10752,
            "western": 37,
            "mystery": 9648,
            "kids": 16,
        }
        gen = genres[movie_category.lower()]

        # url = (
        #     "https://api.themoviedb.org/3/discover/movie?language=en-US&page=1&with_genres="
        #     + str(gen)
        #     + "&sort_by=popularity.desc&include_video=true"
        # )
        # response = requests.get(url, headers=headers)
        # movie_cat_list = response.json()["results"]

        movie_cat_list1 = PopularMovies.objects.filter(genre_ids__contains=gen).values()

        movie_cat_list = list(movie_cat_list1)[:205]
        # movie_cat_list = json.dumps(data_list, cls=DecimalEncoder)

    context = {
        "topmovies": movie_cat_list,
        # "imagedetail": imagedetail["backdrops"][0:15],
    }
    return render(request, "movies/final/movie_by_category.html", context)


def movie_update(request):
    movies = Movie()

    popular = movies.popular()
    nowplaying = movies.now_playing()
    toprated = movies.top_rated()
    upcoming = movies.upcoming()

    pg = 1
    page_count = []
    response = requests.get(nowplaying_url + "&page=" + str(pg), headers=headers)
    nowplaying = response.json()["results"]
    page_count.append(response.json()["total_pages"])

    response = requests.get(popular_url + "&page=" + str(pg), headers=headers)
    popular = response.json()["results"]
    page_count.append(response.json()["total_pages"])

    response = requests.get(toprated_url + "&page=" + str(pg), headers=headers)
    toprated = response.json()["results"][0:19]
    page_count.append(response.json()["total_pages"])

    response = requests.get(upcoming_url + "&page=" + str(pg), headers=headers)
    upcoming = response.json()["results"]
    page_count.append(response.json()["total_pages"])

    # category = [popular, nowplaying, toprated, upcoming]
    category = {
        "popular": [popular_url, page_count[0]],
        "nowplaying": [nowplaying_url, page_count[1]],
        "toprated": [toprated_url, page_count[2]],
        "upcoming": [upcoming_url, page_count[3]],
    }

    i = 0
    category_name = ["popular", "nowplaying", "toprated", "upcoming"]

    for cat in category:
        x = 0
        for x in range(page_count[0] if page_count[0] < 499 else 499):
            result = requests.get(
                category[cat][0] + "&page=" + str(x + 1), headers=headers
            )
            if result.status_code != 200:
                continue
            moview_result = result.json()["results"]
            for item in moview_result:
                id_exit = PopularMovies.objects.all().filter(id=item["id"]).count()
                # id_exit = 1
                rel_date = datetime.datetime.now()
                try:
                    rel_date = item["release_date"]

                    if id_exit == 0:
                        mv = PopularMovies.objects.create(
                            id=item["id"],
                            adult=item["adult"],
                            backdrop_path=item["backdrop_path"],
                            genre_ids=item["genre_ids"],
                            original_language=item["original_language"],
                            original_title=item["original_title"],
                            overview=item["overview"],
                            popularity=item["popularity"],
                            poster_path=item["poster_path"],
                            release_date=rel_date,
                            title=re.sub("\W+", "", item["title"]),
                            video=item["video"],
                            vote_average=item["vote_average"],
                            vote_count=item["vote_count"],
                            movie_category=category_name[i],
                        )  # create a User object
                        mv.save()  # save it

                    else:
                        PopularMovies.objects.filter(
                            id=item["id"],
                        ).update(
                            adult=item["adult"],
                            backdrop_path=item["backdrop_path"],
                            genre_ids=item["genre_ids"],
                            original_language=item["original_language"],
                            original_title=item["original_title"],
                            overview=item["overview"],
                            popularity=item["popularity"],
                            poster_path=item["poster_path"],
                            release_date=rel_date,
                            title=re.sub("\W+", "", item["title"]),
                            video=item["video"],
                            vote_average=item["vote_average"],
                            vote_count=item["vote_count"],
                            movie_category=category_name[i],
                        )
                except Exception as ex:
                    print(ex)
                    rel_date = datetime.datetime.now()
        i += 1

    return HttpResponse("<h1>Update sucessful</h1>")


def updatelink(request):
    # movies = PopularMovies.objects.all()
    # movies = PopularMovies.objects.filter(id__gte=623492)
    # for movie in movies:
    #     result = requests.get(
    #         "https://api.themoviedb.org/3/movie/" + str(movie.id) + " /videos",
    #         headers=headers,
    #     )
    #     if result.status_code == 200 and len(result.json()["results"]) > 0:
    #         PopularMovies.objects.filter(
    #             id=movie.id,
    #         ).update(movie_trailer=result.json()["results"][0]["key"])

    movies = PopularMovies.objects.all()
    for movie in movies:
        result = requests.get(
            "https://api.themoviedb.org/3/movie/" + str(movie.id),
            headers=headers,
        )
        if result.status_code == 200 and len(result.json()) > 0:
            PopularMovies.objects.filter(
                id=movie.id,
            ).update(release_date=result.json()["release_date"])

    return HttpResponse("<h1>Update usuucessful</h1>")



 
@api_view(['GET', 'PUT', 'DELETE'])
def blocked_detail(request, pk):
    try: 
        blockedmovies = BlockedMovies.objects.get(pk=pk) 
    except BlockedMovies.DoesNotExist: 
        return JsonResponse({'message': 'The blockedmovies does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        blockedmovies_serializer = BlockedMoviesSerializer(blockedmovies) 
        return JsonResponse(blockedmovies_serializer.data) 
 
    elif request.method == 'PUT': 
        blockedmovies_data = JSONParser().parse(request) 
        blockedmovies_serializer = BlockedMoviesSerializer(blockedmovies, data=blockedmovies_data) 
        if blockedmovies_serializer.is_valid(): 
            blockedmovies_serializer.save() 
            return JsonResponse(blockedmovies_serializer.data) 
        return JsonResponse(blockedmovies_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        blockedmovies.delete() 
        return JsonResponse({'message': 'blocked movies was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
@api_view(['GET'])
def blocked_list_published(request):
    blockedmovies = BlockedMovies.objects.filter(published=True)
        
    if request.method == 'GET': 
        blockedmovies_serializer = BlockedMoviesSerializer(blockedmovies, many=True)
        return JsonResponse(blockedmovies_serializer.data, safe=False)