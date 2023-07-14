from django.contrib import admin

# Register your models here.
from .models import Movies, NewTrailer, SeriesModel, season, PopularMovies, AdLinks

# Register your models here.

admin.site.register(Movies)
admin.site.register(NewTrailer)
admin.site.register(SeriesModel)
admin.site.register(season)
admin.site.register(PopularMovies)
admin.site.register(AdLinks)
