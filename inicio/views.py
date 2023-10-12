from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime 


def inicio(request):
    datos = {'fecha ': datetime.now()}
    
    return render (request, r'\inicio\inicio.html', datos)
    
def crear_curso(request,titulo, numero):
    curso= curso (titulo=titulo, numero=numero)
    curso.save()
    print (titulo)
    return render(request, r'\inicio\curso_creado.html', {})
# Create your views here.
 