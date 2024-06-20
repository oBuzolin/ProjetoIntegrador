# app_professor/urls.py
from django.urls import path
from .views import professor_home

urlpatterns = [
    path('', professor_home, name='professor_home'),
]
