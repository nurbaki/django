from django.urls import path
from .views import (
    home,
    special,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('special/', special, name="special"),
]