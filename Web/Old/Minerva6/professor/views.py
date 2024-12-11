from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# from .models import SalaAula, Mensagem
from django.views.decorators.http import require_POST
from aluno.models import Minerva_Aluno
from .models import Minerva_Professor, Minerva_ProfessorTurma, Minerva_Turma, Minerva_Disciplina, Minerva_MuralMensagem, Minerva_MatriculaTurma
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import timezone
from django.db.models import Avg


def professor_home(request, matricula):
    # Busca o professor com a matrícula fornecida ou retorna um 404
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    # Busca as turmas associadas ao professor e carrega a turma relacionada usando select_related
    turmas = Minerva_ProfessorTurma.objects.filter(matricula=professor).select_related('id_Turma')
    # Monta os dados das turmas para passar ao template
    turmas_detalhes = [{
        'id_Turma': turma.id_Turma.id_Turma,  # Certifique-se que 'id_Turma' está correto no modelo
        'nome_turma': turma.id_Turma.nomeTurma,
        'disciplina': Minerva_Disciplina.objects.get(id_Turma=turma.id_Turma).nome_disciplina,
    } for turma in turmas]
    
    
    context = {
        'professor': professor,
        'matricula': matricula,
        'turmas': turmas_detalhes,  # Enviando lista de turmas para o template
    }

    return render(request, 'professor_home.html', context)

def sala_detalhes(request, matricula, id_Turma):
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    turmas = Minerva_ProfessorTurma.objects.filter(matricula=professor).select_related('id_Turma')

    # Obtenha as disciplinas associadas a cada turma
    turmas_detalhes = [{
        'id_Turma': turma.id_Turma.id_Turma,
        'nome_turma': turma.id_Turma.nomeTurma,
        'disciplina': Minerva_Disciplina.objects.get(id_Turma=turma.id_Turma).nome_disciplina,
    } for turma in turmas]

    
    context = {
        'professor': professor,
        'matricula': matricula,
        'turmas': turmas_detalhes,
        'id_Turma': id_Turma,
    }
    return render(request, 'sala_detalhes.html', context)

def alunos_detalhes(request, matricula, id_Turma):
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    turmas = Minerva_ProfessorTurma.objects.filter(matricula=professor).select_related('id_Turma')
    # Busca todos os alunos que estão matriculados na turma especificada
    alunos_matriculados = Minerva_MatriculaTurma.objects.filter(id_Turma=id_Turma).select_related('ra')
    turmas_detalhes = [{
        'id_Turma': turma.id_Turma.id_Turma,
        'nome_turma': turma.id_Turma.nomeTurma,
        'disciplina': Minerva_Disciplina.objects.get(id_Turma=turma.id_Turma).nome_disciplina,
    } for turma in turmas]
    context = {
        'professor': professor,
        'matricula': matricula,
        'turmas': turmas_detalhes,
        'id_Turma': id_Turma,
        'alunos': alunos_matriculados,  # Passa a lista de alunos para o template
    }
    return render(request, 'alunos.html', context)


def ProjInt_4DSN_Atividades(request, matricula, id_Turma):
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    turmas = Minerva_ProfessorTurma.objects.filter(matricula=professor).select_related('id_Turma')

    # Obtenha as disciplinas associadas a cada turma
    turmas_detalhes = [{
        'id_Turma': turma.id_Turma.id_Turma,
        'nome_turma': turma.id_Turma.nomeTurma,
        'disciplina': Minerva_Disciplina.objects.get(id_Turma=turma.id_Turma).nome_disciplina,
    } for turma in turmas]

    
    context = {
        'professor': professor,
        'matricula': matricula,
        'turmas': turmas_detalhes,
        'id_Turma': id_Turma,
    }
    return render(request, 'ProjInt_4DSN_Atividades.html', context)
    

def enviar_mensagem(request):
    mensagem_texto = request.POST.get('mensagem')
    sala_id = request.POST.get('sala_id')
    professor_id = getattr(request.user, 'professor', None)
    aluno_id = getattr(request.user, 'aluno', None)

    # Verifique se a mensagem não está vazia e se a turma existe
    if mensagem_texto and sala_id:
        try:
            turma = Minerva_Turma.objects.get(id_Turma=sala_id)  # Verifica se a turma existe
        except Minerva_Turma.DoesNotExist:
            return JsonResponse({'status': 'error', 'error': 'Turma não encontrada.'})

        if professor_id or aluno_id:
            # Salvar a mensagem no banco de dados
            mensagem = Minerva_MuralMensagem.objects.create(
                professor=professor_id,  # Salvando o objeto professor, não o ID
                aluno=aluno_id,  # Salvando o objeto aluno, não o ID
                mensagem=mensagem_texto,
                id_Turma=turma,  # Relacionando a turma existente
                data_publicacao=timezone.now()  # Define a data de publicação
            )
            
            # Determinar o autor da mensagem (professor ou aluno)
            if professor_id:
                autor = professor_id.nome  # Busca o nome do professor
            elif aluno_id:
                autor = aluno_id.nome  # Busca o nome do aluno
            else:
                autor = "Autor desconhecido"
            
            # Retornar o nome do autor e a mensagem para o frontend
            return JsonResponse({
                'status': 'success',
                'autor': autor,
                'mensagem': mensagem.mensagem,
                'data_publicacao': mensagem.data_publicacao.strftime("%d/%m/%Y %H:%M")
            })
        else:
            return JsonResponse({'status': 'error', 'error': 'A mensagem deve ter um autor (professor ou aluno).'})
    else:
        return JsonResponse({'status': 'error', 'error': 'Mensagem ou sala inválida.'})
