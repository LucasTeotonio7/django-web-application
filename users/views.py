from django.shortcuts import render

# Create your views here.


def users_registration(request):
    return render(request, 'users/registration.html')

def users_login(request):
    return render(request, 'users/login.html')

def users_logout(request):
    pass

def dashboard(request):
    pass
