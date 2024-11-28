from django.shortcuts import render
from .models import Curso

# Se crean funciones de que elementos de la clase Curso se van a ver 

def lista_cursos(request):
    cursos = Curso.objects.all()
#   carpeta/ html    La variable curso, se cambia a clave y valor para que en html se pueda llamar
    return render(request, 'cursos/lista_cursos.html', {'cursos': cursos})