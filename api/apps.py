from django.apps import AppConfig


class ApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'


INSTALLED_APPS = [
    # Tutorials application 
    'api.apps.ApiConfig',
]