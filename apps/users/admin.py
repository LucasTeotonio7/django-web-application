from django.contrib import admin
from .models import User
# Register your models here


class UserList(admin.ModelAdmin):
    list_display = ('id', 'username', 'full_name', 'email', 'is_active')
    list_display_links = ('id', 'username')
    search_fields = ('name', 'email')
    list_filter = ('is_active', )
    list_per_page = 10


admin.site.register(User, UserList)
