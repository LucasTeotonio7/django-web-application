from django.shortcuts import render
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    data = {'recipes' : recipes}

    return render(request, 'index.html', context=data)


def recipe(request):
    return render(request, 'recipes.html')
