# users/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .models import User
from .forms import LoginForm
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data['usuario']
            senha = form.cleaned_data['senha']
            try:
                user = User.objects.get(usuario=usuario, senha=senha)
                if user.cargo == 1:
                    return redirect('professor_home')
                elif user.cargo == 2:
                    return redirect('aluno_home')
            except User.DoesNotExist:
                messages.error(request, 'Usuário ou senha incorretos.')
                return redirect('login') 
    else:
        form = LoginForm()
        
    return render(request, 'login.html', {'form': form})
