from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:pk>', views.recipe, name='recipes')
]
