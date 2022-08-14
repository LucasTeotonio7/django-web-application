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

def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    return redirect('users_dashboard')
