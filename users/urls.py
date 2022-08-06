from django.urls import path

from . import views


urlpatterns = [
    path('users/registration/', views.users_registration, name='users-registration'),
    path('users/login/', views.users_login, name='users-login'),
    path('users/logout/', views.users_logout, name='users-logout'),
    path('dashboard/', views.dashboard, name='users-dashboard')
]
