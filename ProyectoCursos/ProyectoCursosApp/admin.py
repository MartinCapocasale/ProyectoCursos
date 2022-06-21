from django.contrib import admin
from .models import *

# Register your models here.

class CursoAdmin(admin.ModelAdmin):
    list_display = ("nombre_curso",)

class EventoAdmin(admin.ModelAdmin):
    list_display = ("nombre_evento",)


admin.site.register(Curso,CursoAdmin)
admin.site.register(Evento, EventoAdmin)