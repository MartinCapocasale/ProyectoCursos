from django.shortcuts import render
from django.http import HttpResponse
from .models import *


# Create your views here.

def inicio(request):
     return render(request,"ProyectoCursosApp/index.html",{})

def cursos(request):
    cursos = Curso.objects.all()
    return render(request,"ProyectoCursosApp/cursos.html",{"cursos":cursos})


def eventos(request):
    eventos = Evento.objects.all()
    return render(request,"ProyectoCursosApp/eventos.html",{"eventos":eventos})

def base(request):
    return render(request,"ProyectoCursosApp/base.html",{})