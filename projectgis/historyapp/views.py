# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.serializers import serialize
from .forms import LoginForm, RegisterForm
from .models import WojnaTrzydziestoletnia

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def Login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Zalogowano pomyślnie!')
            else:
                messages.warning(request, 'Wprowadzono błędne dane')
    if request.user.is_authenticated:
        return redirect('/')
    else:
        form = LoginForm()
        return render(request, 'login.html', {'form' : form})

def Register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = request.POST['login']
            email = request.POST['email']
            password = request.POST['password']
            user, created = User.objects.get_or_create(username=username, email=email)
            if (created):
                user.set_password(password)
                user.save()
                return redirect('/login/')
            else:
                messages.warning(request, 'Użytkownik instnieje w bazie')
    if not request.user.is_authenticated:
        form = RegisterForm()
        return render(request, 'register.html', {'form' : form})
    else:
        return redirect('/login/')

def wojna_trzydziestoletnia(request):
    zdarzenie = WojnaTrzydziestoletnia.objects.all()
    
    return render(request, 'wojna_trzydziestoletnia.html', {'zdarzenie': zdarzenie})

def geojson(request, table):
    if table == 'wojna_trzydziestoletnia':
        model = WojnaTrzydziestoletnia
    else:
        return HttpResponse('Brak tabeli {}'.format( table ), status=404)
    data = serialize('geojson', model.objects.all(), geometry_field='geometry')
    return HttpResponse(data, content_type = 'application/geo+json')