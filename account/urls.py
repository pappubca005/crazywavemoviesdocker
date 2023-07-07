from . views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('register/', register_fun, name='register'),
    path('login/', login_fun, name='login'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
