
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('student/', StudentsApi.as_view()),
    path('products/', ProductApi.as_view()),
    path('register_user/', Register_user.as_view()),
    # path('add_student/', add_student),
    # path('delete_student/<id>/', delete_student),
    path('get_book/', get_book),
    path('', home),
]
