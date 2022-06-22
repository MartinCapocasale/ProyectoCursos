from django.db import models
import datetime


# Create your models here.
class Curso(models.Model):

    nombre_curso = models.CharField(max_length=30)
    comision_curso = models.IntegerField()
    cantidad_maxima_de_personas_curso = models.IntegerField()

# Create your models here.
class Evento(models.Model):

    nombre_evento = models.CharField(max_length=30)
    lugar_evento = models.CharField(max_length=60)
    descripcion_evento = models.CharField(max_length=150)
    incio_evento = models.DateTimeField()
    fin_evento = models.DateTimeField()
