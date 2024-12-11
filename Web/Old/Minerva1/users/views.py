# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import User
from .forms import LoginForm, PasswordResetForm
from django.contrib import messages
from django.db import connection


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            try:
                user = User.objects.get(usuario=usuario, senha=senha)
                if user.cargo == 2:
                    return redirect('professor_home')
                elif user.cargo == 3:
                    return redirect('aluno_home')
            except User.DoesNotExist:
                messages.error(request, 'Usuário ou senha incorretos.')
                return redirect('login') 
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})

def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            nova_senha = form.cleaned_data['nova_senha']
            
           # Verifica se o usuário existe
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT COUNT(*) FROM Minerva_Login WHERE usuario = %s
                """, [usuario])
                usuario_existe = cursor.fetchone()[0]
            
            if usuario_existe:
                # Atualiza a senha se o usuário existir
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE Minerva_Login
                        SET senha = %s 
                        WHERE usuario = %s
                    """, [nova_senha, usuario])
                
                messages.success(request, 'Senha alterada com sucesso! Você será redirecionado em breve.')
                return redirect('reset_sucess')
            else:
                messages.error(request, 'Usuário não encontrado.')
                return redirect('reset')
    else:
        form = PasswordResetForm()

    return render(request, 'reset.html', {'form': form})

def reset_password_success(request):
    messages.success(request, 'Senha alterada com sucesso! Você será redirecionado em breve.')
    return render(request, 'reset_sucess.html')