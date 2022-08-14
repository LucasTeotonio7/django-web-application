from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import auth, messages
User = get_user_model()

from recipes.models import Recipe


def users_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if empty_field(name):
            print('o campo nome não pode ser nulo')
            return redirect('users_registration')

        if empty_field(last_name):
            print('o campo sobrenome não pode ser nulo')
            return redirect('users_registration')

        if empty_field(email):
            print('o campo email não pode ser nulo')
            return redirect('users_registration')

        if password != password2:
            messages.error(request, 'As senhas não são iguais')
            return redirect('users_registration')

        if User.objects.filter(email=email).exists():
             messages.error(request, 'Email já cadastrado')
             return redirect('users_registration')

        if User.objects.filter(username=username).exists():
             messages.error(request, 'Nome de usuário já cadastrado')
             return redirect('users_registration')

        user = User.objects.create_user(
            username=username,
            name=name,
            last_name=last_name,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, 'Usuário cadastrado com sucesso!')

        return redirect('users_login')
    return render(request, 'users/registration.html')

def users_login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if empty_field(email) or empty_field(password):
            messages.error(request, 'Os campos email e senha não podem ficar em branco')
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
        recipes = Recipe.objects.filter(created_by=request.user).order_by('-created_at')
        return render(request, 'users/dashboard.html', context={"recipes": recipes})
    return redirect('index')

def create_recipe(request):
    if request.method == 'POST':
        name = request.POST['name']
        ingredients = request.POST['ingredients']
        method_preparation = request.POST['method_preparation']
        cooking_time = request.POST['cooking_time']
        recipe_yield = request.POST['recipe_yield']
        category = request.POST['category']
        image = request.FILES['image']
        Recipe.objects.create(
            name=name,
            ingredients=ingredients,
            method_preparation=method_preparation,
            cooking_time=cooking_time,
            recipe_yield=recipe_yield,
            category=category,
            image=image,
            created_by=request.user)
        redirect('users_dashboard')


    if request.method == 'GET' and request.user.is_authenticated:
        return render(request, 'users/create_recipe.html')
    return redirect('index')


def empty_field(field):
    return not field.strip()