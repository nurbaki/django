from django.urls import path
from .views import (index, student_add, student_detail, student_list, student_update, student_delete
)

urlpatterns = [
    path('', index, name='home'),
    path('list/', student_list, name='list'),
    path('add/', student_add, name='add'),
    path('update/<int:id>/', student_update, name='update'),
    path('delete/<int:id>',student_delete , name='delete'),
    path('student/<int:id>',student_detail , name='detail'),
]