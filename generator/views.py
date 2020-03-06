from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):
    charactors = list('abcdefghijklmnopqrstuvwxyz')

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        charactors.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if request.GET.get('specialcharactor'):
        charactors.extend(list('!@#$%^&*()_+-=;:'))
    if request.GET.get('numbers'):
        charactors.extend(list('0123456789'))


    thePassword = ''

    for i in range(length):
        thePassword += random.choice(charactors)

    return render(request, 'generator/password.html', {'password': thePassword,})


def about(request):
    return render(request, 'generator/about.html')