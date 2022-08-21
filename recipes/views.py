from django.shortcuts import render, get_object_or_404, redirect
from .models import Recipe


def index(request):

    recipes = Recipe.objects.filter(published=True).order_by('-created_at')
    if 'search' in request.GET:
        recipes = recipes.filter(name__icontains=request.GET['search'])
    data = {'recipes' : recipes}

    return render(request, 'index.html', context=data)


def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    data = {'recipe' : recipe}
    return render(request, 'recipes.html', context=data)


def recipe_create(request):
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
        return render(request, 'users/recipe_form.html')
    return redirect('index')


def recipe_update(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    data = { "recipe" : recipe}
    if request.method == 'POST':
        recipe.name = request.POST['name']
        recipe.ingredients = request.POST['ingredients']
        recipe.method_preparation = request.POST['method_preparation']
        recipe.cooking_time = request.POST['cooking_time']
        recipe.recipe_yield = request.POST['recipe_yield']
        recipe.category = request.POST['category']
        if request.FILES.get('image'):
            recipe.image = request.FILES['image']
        recipe.save()
        return redirect('users_dashboard')
    if request.method == 'GET' and request.user.is_authenticated:
        return render(request, 'users/recipe_form.html', context=data)
    return redirect('index')


def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('users_dashboard')
