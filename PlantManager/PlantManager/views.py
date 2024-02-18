from django.shortcuts import render, redirect
from .models import Plant
from .forms import PlantForm

def inicio (request):
    return render(request, "AppPlantManager/inicio.html")

def busqueda (request):
    return render(request, "AppPlantManager/busqueda.html")

def contacto (request):
    return render(request, "AppPlantManager/contacto.html")

def registro (request):
    return render(request, "AppPlantManager/registro.html")

def agregar_planta(request):
    if request.method == 'POST':
                form = PlantForm (request.POST)
                if form.is_valid():
                   form.save()
                   return



     
