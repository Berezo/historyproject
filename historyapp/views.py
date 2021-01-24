# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LoginForm, RegisterForm, WojnaTrzydziestoletniaForm, PowstanieStycznioweForm, PowstanieListopadoweForm, RewolucjaAmerykanskaForm
from .models import WojnaTrzydziestoletnia, PowstanieStyczniowe, PowstanieListopadowe, RewolucjaAmerykanska

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

def powstanie_styczniowe(request):
    zdarzenie = PowstanieStyczniowe.objects.all()
    return render(request, 'powstanie_styczniowe.html', {'zdarzenie': zdarzenie})

def powstanie_listopadowe(request):
    zdarzenie = PowstanieListopadowe.objects.all()
    return render(request, 'powstanie_listopadowe.html', {'zdarzenie': zdarzenie})

def rewolucja_amerykanska(request):
    zdarzenie = RewolucjaAmerykanska.objects.all()
    return render(request, 'rewolucja_amerykanska.html', {'zdarzenie': zdarzenie})

def geojson(request, table):
    if table == 'wojna_trzydziestoletnia':
        model = WojnaTrzydziestoletnia
    elif table == 'powstanie_styczniowe':
        model = PowstanieStyczniowe
    elif table == 'powstanie_listopadowe':
        model = PowstanieListopadowe
    elif table == 'rewolucja_amerykanska':
        model = RewolucjaAmerykanska
    else:
        return HttpResponse('Brak tabeli {}'.format(table), status=404)
    data = serialize('geojson', model.objects.all(), geometry_field='geometry')
    return HttpResponse(data, content_type = 'application/geo+json')

class WojnaTrzydziestoletniaCreate(CreateView):
    model = WojnaTrzydziestoletnia
    form_class = WojnaTrzydziestoletniaForm
    success_url = reverse_lazy('wojna30letnia')

class WojnaTrzydziestoletniaUpdate(UpdateView):
    model = WojnaTrzydziestoletnia
    form_class = WojnaTrzydziestoletniaForm
    success_url = reverse_lazy('wojna30letnia')

class WojnaTrzydziestoletniaDelete(DeleteView):
    model = WojnaTrzydziestoletnia
    success_url = reverse_lazy('wojna30letnia')

class PowstanieStycznioweCreate(CreateView):
    model = PowstanieStyczniowe
    form_class = PowstanieStycznioweForm
    success_url = reverse_lazy('powstanieStyczniowe')

class PowstanieStycznioweUpdate(UpdateView):
    model = PowstanieStyczniowe
    form_class = PowstanieStycznioweForm
    success_url = reverse_lazy('powstanieStyczniowe')

class PowstanieStycznioweDelete(DeleteView):
    model = PowstanieStyczniowe
    success_url = reverse_lazy('powstanieStyczniowe')

class PowstanieListopadoweCreate(CreateView):
    model = PowstanieListopadowe
    form_class = PowstanieListopadoweForm
    success_url = reverse_lazy('powstanieListopadowe')
    
class PowstanieListopadoweUpdate(UpdateView):
    model = PowstanieListopadowe
    form_class = PowstanieListopadoweForm
    success_url = reverse_lazy('powstanieListopadowe')

class PowstanieListopadoweDelete(DeleteView):
    model = PowstanieListopadowe
    success_url = reverse_lazy('powstanieListopadowe')

class RewolucjaAmerykanskaCreate(CreateView):
    model = RewolucjaAmerykanska
    form_class = RewolucjaAmerykanskaForm
    success_url = reverse_lazy('rewolucjaAmerykanska')

class RewolucjaAmerykanskaUpdate(UpdateView):
    model = RewolucjaAmerykanska
    form_class = RewolucjaAmerykanskaForm
    success_url = reverse_lazy('rewolucjaAmerykanska')

class RewolucjaAmerykanskaDelete(DeleteView):
    model = RewolucjaAmerykanska
    success_url = reverse_lazy('rewolucjaAmerykanska')

    # def get_initial(self):
    #     initial = super(WojnaTrzydziestoletniaUpdate, self).get_initial()
    #     print('initial data', initial)

    #     # retrieve current object
    #     wojnaTrzydziestoletnia_object = self.get_object()

    #     initial['nazwa'] = wojnaTrzydziestoletnia_object.nazwa
    #     initial['typ'] = wojnaTrzydziestoletnia_object.typ
    #     initial['data'] = wojnaTrzydziestoletnia_object.data
    #     initial['okres'] = wojnaTrzydziestoletnia_object.okres
    #     initial['opis'] = wojnaTrzydziestoletnia_object.opis
    #     initial['str_kon_1'] = wojnaTrzydziestoletnia_object.str_kon_1
    #     initial['str_kon_2'] = wojnaTrzydziestoletnia_object.str_kon_2
    #     initial['dowod_1'] = wojnaTrzydziestoletnia_object.dowod_1
    #     initial['dowod_2'] = wojnaTrzydziestoletnia_object.dowod_2
    #     initial['zwyciestwo'] = wojnaTrzydziestoletnia_object.zwyciestwo
    #     initial['geometry'] = wojnaTrzydziestoletnia_object.geometry
        
    #     return initial
  
    # def get_object(self, *args, **kwargs):
    #     wojnaTrzydziestoletnia = get_object_or_404(WojnaTrzydziestoletnia, pk=self.kwargs['pk'])
    #     print(wojnaTrzydziestoletnia)
    #     return wojnaTrzydziestoletnia
