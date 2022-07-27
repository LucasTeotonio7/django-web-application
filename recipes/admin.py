from django.contrib import admin
from .models import Recipe

class RecipeList(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'cooking_time')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'category')
    list_filter = ('category', )
    list_per_page = 10


admin.site.register(Recipe, RecipeList)
