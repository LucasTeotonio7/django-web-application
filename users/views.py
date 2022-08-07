from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
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
    return render(request, 'users/login.html')

def users_logout(request):
    pass

def dashboard(request):
    pass
