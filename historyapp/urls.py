"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name="welcome"),
    path('login/', views.Login, name='login'),
    path('register/', views.Register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('wojna_30_letnia/', views.wojna_trzydziestoletnia, name='wojna30letnia'),
    path('wojna_30_letnia/new', views.WojnaTrzydziestoletniaCreate.as_view(), name='wojna30letniaNew'), 
    path('wojna_30_letnia/edit/<pk>', views.WojnaTrzydziestoletniaUpdate.as_view(), name='wojna30letniaEdit'),
    path('wojna_30_letnia/delete/<pk>', views.WojnaTrzydziestoletniaDelete.as_view(), name='wojna30letniaDel'),
    path('powstanie_styczniowe/', views.powstanie_styczniowe, name='powstanieStyczniowe'),
    path('powstanie_styczniowe/new', views.PowstanieStycznioweCreate.as_view(), name='powstanieStycznioweNew'),
    path('powstanie_styczniowe/edit/<pk>', views.PowstanieStycznioweUpdate.as_view(), name='powstanieStycznioweEdit'),
    path('powstanie_styczniowe/delete/<pk>', views.PowstanieStycznioweDelete.as_view(), name='powstanieStycznioweDel'),
    path('powstanie_listopadowe/', views.powstanie_listopadowe, name='powstanieListopadowe'),
    path('powstanie_listopadowe/new', views.PowstanieListopadoweCreate.as_view(), name='powstanieListopadoweNew'),
    path('powstanie_listopadowe/edit/<pk>', views.PowstanieListopadoweUpdate.as_view(), name='powstanieListopadoweEdit'),
    path('powstanie_listopadowe/delete/<pk>', views.PowstanieListopadoweDelete.as_view(), name='powstanieListopadoweDel'),
    path('rewolucja_amerykanska/', views.rewolucja_amerykanska, name='rewolucjaAmerykanska'),
    path('rewolucja_amerykanska/new', views.RewolucjaAmerykanskaCreate.as_view(), name='rewolucjaAmerykanskaNew'),
    path('rewolucja_amerykanska/edit/<pk>', views.RewolucjaAmerykanskaUpdate.as_view(), name='rewolucjaAmerykanskaEdit'),
    path('rewolucja_amerykanska/delete/<pk>', views.RewolucjaAmerykanskaDelete.as_view(), name='rewolucjaAmerykanskaDel'),
    path('geojson/<table>/', views.geojson),
]
