from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from datetime import datetime 
from inicio import forms


def inicio(request):
    datos = {'fecha ': datetime.now()}
    
    return render (request, r'\inicio\inicio.html', datos)
    
def crear_curso(request):
    if request.method = 'POST':
        if formulario.is.valid()
    curso= Curso (nombre=request.GET.ge('titulo'), apellido=request.GET'numero')
    curso.save()
    
    print (request.method)
    print (request.GET)
    print(request.POST)
    formulario = curso_cafe()
    formulario = curso_cafe (request.POST)
    return render(request, r'\inicio\curso_creado.html', {'formulario'=formulario})

# Create your views here.
 