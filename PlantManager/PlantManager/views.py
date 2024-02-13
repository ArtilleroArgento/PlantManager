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