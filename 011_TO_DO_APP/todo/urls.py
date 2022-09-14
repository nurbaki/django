from django.urls import path
from .views import todo_delete, TodoCreate, TodoHome, TodoUpdate

urlpatterns = [
    # path("", home, name="home"),
    path("", TodoHome.as_view(), name="home"),
    # path("add/", todo_create, name="add" ),
    path("add/", TodoCreate.as_view(), name="add" ),
    # path("update/<int:id>/", todo_update, name="update" ),
    path("update/<int:id>/", TodoUpdate.as_view(), name="update" ),
    path("delete/<int:id>/", todo_delete, name="delete" ),
   
]