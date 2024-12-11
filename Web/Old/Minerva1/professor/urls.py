# app_professor/urls.py
from django.urls import path
from .views import professor_home, ProjetoIntegrador_4DSN, ProjInt_4DSN_Atividades, ProjInt_4DSN_Alunos
from . import views

urlpatterns = [
    path('', professor_home, name='professor_home'),
    path('ProjetoIntegrador_4DSN.html', ProjetoIntegrador_4DSN, name='ProjetoIntegrador_4DSN'),
    path('ProjInt_4DSN_Atividades.html', ProjInt_4DSN_Atividades, name='ProjInt_4DSN_Atividades'),
    path('ProjInt_4DSN_Alunos.html', ProjInt_4DSN_Alunos, name='ProjInt_4DSN_Alunos'),
    path('enviar_mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]
