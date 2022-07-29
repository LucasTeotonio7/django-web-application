from django.shortcuts import render, get_object_or_404
from .models import Recipe


def index(request):
    recipes = Recipe.objects.filter(published=True).order_by('-created_at')
    data = {'recipes' : recipes}

    return render(request, 'index.html', context=data)


def recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    data = {'recipe' : recipe}
    return render(request, 'recipes.html', context=data)
