from rest_framework import serializers

from .models import Movies, PopularMovies,BlockedMovies


class MoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movies
        fields = "__all__"
        # fields = [
        # "name",
        # "slug",
        # "premium",
        # "discription",
        # "image",
        # "thumbnail_link",
        # "background_image_link",
        # "screen_shot",
        # "screen_shot_link",
        # "movie_length",
        # "release_date",
        # "movie_rate",
        # "imdb_rating",
        # "movie_director",
        # "movie_actor",
        # "movie_language",
        # "movie_subtitle",
        # "movie_type",
        # "movie_category",
        # "link_4k",
        # "link_1920",
        # "link_720",
        # "size_4k",
        # "size_1920",
        # "size_720",
        # "movie_link",
        # "movie_online",
        # "torent_link_4k",
        # "torent_link_1920",
        # "torent_link_720",
        # "torent_file_link",
        # "tmvdbid",
        # "date",
        # ]


class PopularMoviesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularMovies
        fields = "__all__"
        # fields = [
        #     "adult",
        #     "backdrop_path",
        #     "genre_ids",
        #     "id",
        #     "original_language",
        #     "original_title",
        #     "overview",
        #     "popularity",
        #     "poster_path",
        #     "release_date",
        #     "title",
        #     "video",
        #     "vote_average",
        #     "vote_count",
        # ]
class BlockedMoviesSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = BlockedMovies
        fields = "__all__"