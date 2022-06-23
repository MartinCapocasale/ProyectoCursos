from django import forms

class NuevoCurso(forms.Form):

    nombre_curso = forms.CharField(max_length=30, label = "Curso:")
    comision_curso = forms.IntegerField(min_value=0, label= "Comision:")
    cantidad_maxima_de_personas_curso = forms.IntegerField(min_value=1, label="Cupo de estudiantes:")