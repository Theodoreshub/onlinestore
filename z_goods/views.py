from django.shortcuts import render,redirect
from . import models


def type_list(request):
    return render(request, 'type_list.html')
