from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
     return render(request,"ProyectoCursosApp/index.html",{})

def cursos(request):
    return render(request,"ProyectoCursosApp/cursos.html",{})

def eventos(request):
    return render(request,"ProyectoCursosApp/eventos.html",{})

def base(request):
    return render(request,"ProyectoCursosApp/base.html",{})