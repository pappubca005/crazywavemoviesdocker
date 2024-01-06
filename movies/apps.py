from django.apps import AppConfig


class MoviesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movies'


INSTALLED_APPS = [
    # Tutorials application 
    'movies.apps.MoviesConfig',
]