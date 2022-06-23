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


def crear_curso(request):

    #Get
    if  request.method == "GET":
        pass

    #Post
    elif request.method == "POST":
        info_formulario = request.POST
        curso = Curso(info_formulario("nombre_curso"),info_formulario("comision_curso"),info_formulario("cantidad_maxima_de_personas_curso"))
        
        curso.save()
    else:
        pass

    return render(request,"ProyectoCursosApp/formulario_curso.html",{})
