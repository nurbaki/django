from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home, user_logout, register, user_login

urlpatterns = [
    path('', home, name='home'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)