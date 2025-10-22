from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib import messages

def registrar(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso! Faça login para continuar.")
            return redirect('/contas/login/')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
    else:
        form = UserCreationForm()
    return render(request, 'registration/registrar.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f"Bem-vindo, {user.username}! Você entrou com sucesso.")
            return redirect('/estoque/')
        else:
            messages.error(request, "Login inválido. Verifique seu usuário e senha.")
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
