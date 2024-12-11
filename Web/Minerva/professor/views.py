from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib import messages
from datetime import datetime
from django.views.decorators.http import require_POST
from aluno.models import Minerva_Aluno
from .models import Minerva_Professor, Minerva_ProfessorTurma, Minerva_Turma, Minerva_Disciplina, Minerva_MuralMensagem, Minerva_MatriculaTurma, Minerva_Atividades
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from django.utils import timezone
from django.db.models import Avg
import json
from django.utils.timezone import make_aware
from django.http import JsonResponse


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
    # Verifique se o professor existe com a matrícula fornecida
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    
    # Carregar as turmas associadas ao professor
    turmas = Minerva_ProfessorTurma.objects.filter(matricula=professor).select_related('id_Turma')

    # Obtenha detalhes das turmas
    turmas_detalhes = [{
        'id_Turma': turma.id_Turma.id_Turma,
        'nome_turma': turma.id_Turma.nomeTurma,
        'disciplina': Minerva_Disciplina.objects.get(id_Turma=turma.id_Turma).nome_disciplina,
    } for turma in turmas]

    # Verifique se é uma requisição AJAX POST
    if request.method == 'POST' and request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        sala_id = request.POST.get('sala_id')
        mensagem = request.POST.get('mensagem')

        if sala_id and mensagem:
            # Salvar a nova mensagem no banco de dados
            nova_mensagem = Minerva_MuralMensagem(
                professor=professor,  # Associa ao professor atual
                mensagem=mensagem,
                data_publicacao=timezone.now(),
                turma_id=sala_id
            )
            nova_mensagem.save()

            # Retornar uma resposta JSON com os detalhes da mensagem
            return JsonResponse({
                'status': 'success',
                'autor': professor.nome,
                'mensagem': nova_mensagem.mensagem,
                'data_publicacao': nova_mensagem.data_publicacao.strftime('%d/%m/%Y %H:%M')
            })
        else:
            return JsonResponse({'status': 'error', 'error': 'Dados incompletos'})

    # Carregar as mensagens da turma especificada
    mensagens = Minerva_MuralMensagem.objects.filter(turma_id=id_Turma).order_by('-data_publicacao')

    context = {
        'professor': professor,
        'matricula': matricula,
        'turmas': turmas_detalhes,
        'id_Turma': id_Turma,
        'mensagens': mensagens,
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

def listar_atividades(request, matricula, id_Turma):
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    turmas = Minerva_ProfessorTurma.objects.filter(matricula=professor).select_related('id_Turma')
    atividades = Minerva_Atividades.objects.filter(turma__id_Turma=id_Turma)

    turmas_detalhes = []
    for turma in turmas:
        disciplina = Minerva_Disciplina.objects.filter(id_Turma=turma.id_Turma).first()
        turmas_detalhes.append({
            'id_Turma': turma.id_Turma.id_Turma,
            'nome_turma': turma.id_Turma.nomeTurma,
            'disciplina': disciplina.nome_disciplina if disciplina else 'Sem Disciplina',
        })
    
    context = {
        'professor': professor,
        'matricula': matricula,
        'turmas': turmas_detalhes,
        'id_Turma': id_Turma,
        'atividades': atividades,
    }

    if request.method == 'POST':
        titulo = request.POST.get('titulo')
        escopo = request.POST.get('escopo')
        envio = request.POST.get('envio')
        entrega = request.POST.get('entrega')
        nota = request.POST.get('nota')
        caminho_arquivo = request.POST.get('caminho_arquivo')

        try:
            # Definir 'envio' como a data e hora atual
            envio = timezone.now()  # Define a data de envio como o momento atual

            # Converte a data de entrega, se fornecida
            entrega = make_aware(datetime.strptime(entrega, '%Y-%m-%dT%H:%M')) if entrega else None
            turma = get_object_or_404(Minerva_Turma, id_Turma=id_Turma)
            atividade = Minerva_Atividades.objects.create(
                titulo=titulo,
                escopo=escopo,
                matricula=professor,  # Salve o objeto professor
                turma=turma,
                envio=envio,
                entrega=entrega,
                nota=nota if nota else None,
                caminho_arquivo=caminho_arquivo
            )
            messages.success(request, 'Atividade cadastrada com sucesso!')
            return redirect('listar_atividades')
        except ValueError as ve:
            messages.error(request, f'Erro de formatação de data: {ve}')
            print(f"Erro de formatação de data: {ve}")
        except Exception as e:
            messages.error(request, f'Erro ao cadastrar atividade: {e}')
            print(f"Erro ao cadastrar atividade: {e}")
    
    return render(request, 'listar_atividades.html', context)

def detalhar_atividade(request, id, matricula, id_Turma):
    atividade = get_object_or_404(Minerva_Atividades, id=id)
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    turmas = Minerva_ProfessorTurma.objects.filter(matricula=professor).select_related('id_Turma')
    atividades = Minerva_Atividades.objects.filter(turma__id_Turma=id_Turma)

    turmas_detalhes = []
    for turma in turmas:
         disciplina = Minerva_Disciplina.objects.filter(id_Turma=turma.id_Turma).first()
         turmas_detalhes.append({
             'id_Turma': turma.id_Turma.id_Turma,
             'nome_turma': turma.id_Turma.nomeTurma,
             'disciplina': disciplina.nome_disciplina if disciplina else 'Sem Disciplina',
        })
    
    context = {
         'professor': professor,
         'matricula': matricula,
         'turmas': turmas_detalhes,
         'id_Turma': id_Turma,
         'atividades': atividades,
    }
    return render(request, 'detalhar_atividades.html', context)