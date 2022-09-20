from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import home, user_logout, register, user_login
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView, 
)

urlpatterns = [
    path('', home, name='home'),
    path('logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),

    path('post_list/', PostListView.as_view(), name="post_list"),
    path('post_create/', PostCreateView.as_view(), name="post_create"),
    path('detail/<int:pk>', PostDetailView.as_view(), name="post_detail"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)