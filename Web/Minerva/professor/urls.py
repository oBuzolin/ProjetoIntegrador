# app_professor/urls.py
from django.urls import path
from .views import professor_home, ProjInt_4DSN_Atividades, sala_detalhes, alunos_detalhes
from . import views

urlpatterns = [
    path('<int:matricula>/', professor_home, name='professor_home'),
    path('<int:matricula>/Sala_De_Aula/<int:id_Turma>/', sala_detalhes, name='sala_detalhes'),
    path('<int:matricula>/Sala_De_Aula/<int:id_Turma>/Alunos', alunos_detalhes, name='alunos'),
    path('<int:matricula>/ProjInt_4DSN_Atividades.html', ProjInt_4DSN_Atividades, name='ProjInt_4DSN_Atividades'),
    # path('<int:matricula>/ranking/<int:id_Turma>/', ranking_view, name='ranking'),
    path('enviar_mensagem/', views.enviar_mensagem, name='enviar_mensagem'),
]
