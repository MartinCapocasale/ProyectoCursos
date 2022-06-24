from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from .forms import *


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
    #Post
    if request.method == "POST":
        formulario = NuevoCurso(request.POST)

        if formulario.is_valid():
            info_curso = formulario.cleaned_data

            curso = Curso(nombre_curso = info_curso["nombre_curso"],comision_curso = int(info_curso["comision_curso"]),cantidad_maxima_de_personas_curso = int(info_curso["cantidad_maxima_de_personas_curso"]))
            
            curso.save()#guardamos en la bdd
            
            return redirect("cursos")#te redirecciono a la pagina de inicio
        else:
            return render(request,"ProyectoCursosApp/formulario_curso.html",{"form":formularioVacio})

    #Get y otros
    else:
        formularioVacio = NuevoCurso()
        return render(request,"ProyectoCursosApp/formulario_curso.html",{"form":formularioVacio})


def buscar_comision(request):
    if request.method == "POST":
        comision = request.POST["comision_curso"]
        comisiones = Curso.objects.filter(comision_curso__icontains=comision)
        return render(request,"ProyectoCursosApp/buscar_comision.html",{"comisiones":comisiones})

    else: 
        comisiones = []
        return render(request,"ProyectoCursosApp/buscar_comision.html",{"comisiones":comisiones})
