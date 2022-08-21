from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.users_registration, name='users_registration'),
    path('login/', views.users_login, name='users_login'),
    path('logout/', views.users_logout, name='users_logout'),
    path('dashboard/', views.dashboard, name='users_dashboard')
]
