from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
User = get_user_model()


def users_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if not name.strip():
            print('o campo nome não pode ser nulo')
            return redirect('users_registration')

        if not last_name.strip():
            print('o campo sobrenome não pode ser nulo')
            return redirect('users_registration')

        if not email.strip():
            print('o campo email não pode ser nulo')
            return redirect('users_registration')

        if password != password2:
            print('As senhas não são iguais')
            return redirect('users_registration')
        
        if User.objects.filter(email=email).exists():
             print('Email já cadastrado')
             return redirect('users_registration')
        
        user = User.objects.create_user(
            username=username, 
            name=name, 
            last_name=last_name, 
            email=email, 
            password=password
        )
        user.save()
        print('Usuário cadastrado com sucesso!')

        return redirect('users_login')
    return render(request, 'users/registration.html')

def users_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if email == '' or password == '':
            print('Os campos email e senha não podem ficar em branco')
            return redirect('users_login')
        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).first()
            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                print('usuário logado')
            else:
                return redirect('users_login')
        return redirect('users_dashboard')

    
    return render(request, 'users/login.html')

def users_logout(request):
    auth.logout(request)
    return redirect('index')

def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'users/dashboard.html')
    return redirect('index')

def create_recipe(request):
    if request.user.is_authenticated:
        return render(request, 'users/create_recipe.html')
    return redirect('index')
