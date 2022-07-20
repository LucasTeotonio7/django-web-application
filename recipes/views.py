from django.shortcuts import render

from django.http import HttpResponse


def index(request):
    recipes = {
        1: 'lasanha',
        2: 'sopa de legumes',
        3: 'sorvete',
        4: 'bolo de morango ^^'
    }

    data = {
        'recipes_name' : recipes
    }
    return render(request, 'index.html', context=data)


def recipe(request):
    return render(request, 'recipes.html')
