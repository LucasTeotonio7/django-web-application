from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('recipes/<int:pk>', views.recipe_detail, name='recipe_detail'),
    path('recipes/<int:pk>/delete', views.recipe_delete, name='recipe_delete')
]
