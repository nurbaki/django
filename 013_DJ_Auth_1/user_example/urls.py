from django.urls import path
from .views import (
    home,
    special,
    register,
)
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home, name="home"),
    path('special/', special, name="special"),
    path('register/', register, name='register'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout')
]