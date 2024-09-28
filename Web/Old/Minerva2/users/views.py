# users/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Minerva_Login, Minerva_Professor
from aluno.models import Minerva_Aluno
# from .utils import hash_password
from hashlib import sha256
import hashlib
from django.contrib.auth import authenticate, login as auth_login
from .forms import LoginForm, PasswordResetForm
from django.db import connection
# from django.contrib.auth.hashers import check_password, make_password
from django.core.mail import send_mail
from django.utils.html import format_html


def login_view(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        senha = request.POST.get('senha')
        senha_hash = sha256(senha.encode()).hexdigest()  # Criptografa a senha inserida

        try:
            professor = Minerva_Professor.objects.get(usuario=usuario)
            if professor.senha == senha_hash:  # Verifica a senha
                login_entry = Minerva_Login.objects.get(professor_matricula_id=professor.matricula)
                if login_entry.status == 'ativo':
                    return render(request,'professor_home.html')
                else:
                    messages.error(request, 'Conta inativa ou bloqueada.')
                    return render(request, 'login.html')
            else:
                messages.error(request, 'Senha incorreta para o professor.')
                return render(request, 'login.html')

        except Minerva_Professor.DoesNotExist:
            # Se não for professor, tenta buscar como aluno
            try:
                aluno = Minerva_Aluno.objects.get(usuario=usuario)
                if aluno.senha == senha_hash:  # Verifica a senha
                    login_entry = Minerva_Login.objects.get(aluno_ra_id=aluno.ra)
                    if login_entry.status == 'ativo':
                        next_url = request.GET.get('next', 'aluno_home')
                        return redirect(next_url)
                    else:
                        messages.error(request, 'Conta inativa ou bloqueada.')
                        return render(request, 'login.html')
                else:
                    messages.error(request, 'Senha incorreta para o aluno.')
                    return render(request, 'login.html')

            except Minerva_Aluno.DoesNotExist:
                messages.error(request, 'Usuário não encontrado.')
                return render(request, 'login.html')

    return render(request, 'login.html')


def reset_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            nova_senha = form.cleaned_data['nova_senha']
            
            # Verifica se o usuário existe na tabela de Professores
            with connection.cursor() as cursor:
                cursor.execute("""
                    SELECT nome, usuario FROM Minerva_Professor WHERE usuario = %s
                """, [usuario])
                resultado = cursor.fetchone()
            
            if resultado:
                nome = resultado[0]
                usuario = resultado[1]  # Captura o e-mail do resultado da consulta

                # Criptografa a senha usando SHA256
                hashed_password = hashlib.sha256(nova_senha.encode()).hexdigest()

                # Atualiza a senha no banco
                with connection.cursor() as cursor:
                    cursor.execute("""
                        UPDATE Minerva_Professor
                        SET senha = %s 
                        WHERE usuario = %s
                    """, [hashed_password, usuario])
                
               # Prepara a mensagem de e-mail em HTML
                html_message = format_html(
                    """
                    <html>
                    <body style="font-family: Arial, sans-serif; font-size: 14px; color: #333;">
                        <p>Olá <strong>{}</strong>,</p>
                        <p>Sua senha foi alterada com sucesso. Se você não solicitou essa alteração, por favor entre em contato com o suporte.</p>
                        <p>Atenciosamente,</p>
                        <p style="font-weight: bold;">Equipe Minerva Estudos</p>
                    </body>
                    </html>
                    """.format(nome)
                    # <p><a href="mailto:minervaembv@gmail.com">minervaembv@gmail.com</a></p>
                )

                # Envia o e-mail ao usuário com o conteúdo HTML
                send_mail(
                    'Alteração de senha realizada com sucesso.',
                    '',  # Deixe vazio, pois o corpo do e-mail será HTML
                    'minervaembv@gmail.com',  # O endereço de e-mail de envio
                    [usuario],  # O e-mail do destinatário
                    fail_silently=False,
                    html_message=html_message,  # Especifica o conteúdo HTML
                )

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
    