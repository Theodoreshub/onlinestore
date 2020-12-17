from django.shortcuts import render, redirect
from . import models


# Create your views here.
def home(request):
    pass
    return render(request, 'z_user/home.html')


def login(request):
    pass
    return render(request, 'z_user/login.html')


def register(request):
    pass
    return render(request, 'z_user/register.html')


def logout(request):
    pass
    return redirect('/home/')
