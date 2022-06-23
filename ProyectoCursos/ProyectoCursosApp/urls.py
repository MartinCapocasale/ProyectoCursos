from django.urls import path
from .views import *

urlpatterns = [
    path('',inicio,name="inicio"),
    path('cursos/', cursos, name="cursos"),
    path('eventos/', eventos, name="eventos"),
    path('crear_curso/', crear_curso, name="crear_curso"),
    path('buscar_comision/', buscar_comision, name="buscar_comision"),
    #path('base/', base),
]
