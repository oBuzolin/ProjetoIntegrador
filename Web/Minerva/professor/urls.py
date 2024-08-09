# app_professor/urls.py
from django.urls import path
from .views import professor_home, ProjetoIntegrador_4DSN

urlpatterns = [
    path('', professor_home, name='professor_home'),
    path('ProjetoIntegrador_4DSN.html', ProjetoIntegrador_4DSN, name='ProjetoIntegrador_4DSN'),
]
