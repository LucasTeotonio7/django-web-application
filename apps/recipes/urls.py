from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('create/recipe/', recipe_create, name='recipe_create'),
    path('recipes/<int:pk>', recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/delete', recipe_delete, name='recipe_delete'),
    path('recipes/<int:pk>/update', recipe_update, name='recipe_update')
]
