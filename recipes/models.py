from django.db import models
from datetime import datetime
from users.models import User

# Create your models here.

class Recipe(models.Model):
    name = models.CharField(verbose_name='Nome', max_length=200)
    ingredients = models.TextField(verbose_name='Ingredientes')
    method_preparation = models.TextField(verbose_name='Modo de preparo')
    cooking_time = models.IntegerField(verbose_name='Tempo de preparo')
    recipe_yield  = models.CharField(verbose_name='Rendimento', max_length=100)
    category  = models.CharField(verbose_name='Categoria', max_length=100)
    published = models.BooleanField(verbose_name='Publicada', default=False)
    created_at = models.DateTimeField(verbose_name='Criado em', default=datetime.now, blank=True)
    created_by = models.ForeignKey(User, verbose_name='Criado por', on_delete=models.CASCADE)
