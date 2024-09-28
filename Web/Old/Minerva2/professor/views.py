from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import SalaAula, Mensagem
from .models import Minerva_Professor


# @login_required
# def professor_home(request):
#     print(f"Usuário autenticado: {request.user.is_authenticated}")
#     try:
#         professor = Minerva_Professor.objects.get(usuario=request.user.username)
#         print(f"Professor encontrado: {professor}")
#     except Minerva_Professor.DoesNotExist:
#         print("Usuário não é um professor")
#         return render(request, 'sem_permissao.html')  # Página de permissão negada

#     return render(request, 'professor_home.html', {'professor': professor})
def professor_home(request):
    return render(request, 'professor_home.html')

def ProjetoIntegrador_4DSN(request):
    return render(request, 'ProjetoIntegrador_4DSN.html')

def ProjInt_4DSN_Atividades(request):
    return render(request, 'ProjInt_4DSN_Atividades.html')

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
