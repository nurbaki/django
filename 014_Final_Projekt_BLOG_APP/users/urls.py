from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import user_logout, register, user_login, profileUpdate, profileDetail
from .views import (
    PostListView,
    PostCreateView,
    PostDetailView,
    PostDeleteView,
    PostUpdateView,
    AboutView,
    MyPostsView,
    # ProfileCreate,
    # ProfileUpdate,
    # ProfileDetail, 
)

urlpatterns = [
    path('logout/', user_logout, name='user_logout'),
    path('register/', register, name='register'),
    path('login/', user_login, name='user_login'),

    path('home/', PostListView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('', PostListView.as_view(), name="home"),
    path('myposts/', MyPostsView.as_view(), name="myposts"),
    path('post_create/', PostCreateView.as_view(), name="post_create"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('update/<int:pk>/', PostUpdateView.as_view(), name="post_update"),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name="post_delete"),

    # path('profile/', ProfileDetail.as_view(), name="profile"),
    # path('profile_add/', ProfileCreate.as_view(), name="profile_add"),
    # path('profile_update/<int:pk>/', ProfileUpdate.as_view(), name="profile_update"),
    path('profile_update/', profileUpdate, name="profile_update"),
    path('profile/', profileDetail, name="profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)