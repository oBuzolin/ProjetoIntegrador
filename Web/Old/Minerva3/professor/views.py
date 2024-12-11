from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import SalaAula, Mensagem
from .models import Minerva_Professor
from django.shortcuts import render, get_object_or_404
from django.conf import settings

def professor_home(request, matricula):
        # Busca o professor com o ID passado na URL
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    context = {
        'professor': professor,
        'matricula': matricula  # Passar matricula para o contexto
    }
    return render(request, 'professor_home.html', context)

def ProjetoIntegrador_4DSN(request, matricula):
    professor = get_object_or_404(Minerva_Professor, matricula=matricula)
    context = {
        'professor': professor,
        'matricula': matricula  # Passar matricula para o contexto
    }
    return render(request, 'ProjetoIntegrador_4DSN.html', context)

def ProjInt_4DSN_Atividades(request):
    return render(request, 'ProjInt_4DSN_Atividades.html')

def ProjInt_4DSN_DER(request):
    return render(request, 'ProjInt_4DSN_DER.html')

def ProjInt_4DSN_Alunos(request):
    return render(request, 'ProjInt_4DSN_Alunos.html')


    

@login_required
def enviar_mensagem(request):
    if request.method == 'POST':
        sala_id = request.POST.get('sala_id')
        mensagem_texto = request.POST.get('mensagem')
        try:
            sala = SalaAula.objects.get(id=sala_id)
            mensagem = Mensagem.objects.create(
                sala=sala,
                usuario=request.user,
                texto=mensagem_texto
            )
            return JsonResponse({'status': 'success', 'mensagem_id': mensagem.id})
        except SalaAula.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Sala de aula não encontrada'})
    return JsonResponse({'status': 'error', 'message': 'Método não permitido'})
