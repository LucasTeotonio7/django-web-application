from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.users_registration, name='users-registration'),
    path('login/', views.users_login, name='users-login'),
    path('logout/', views.users_logout, name='users-logout'),
    path('dashboard/', views.dashboard, name='users-dashboard')
]
