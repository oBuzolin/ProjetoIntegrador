# app_aluno/urls.py
from django.urls import path
from .views import aluno_home

urlpatterns = [
    path('', aluno_home, name='aluno_home'),
]