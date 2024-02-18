from django.urls import path
from PlantManager import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('busqueda/', views.busqueda, name='busqueda'),
    path('registro/', views.registro, name='registro'),
    path('contacto/', views.contacto, name='contacto')
]

urlpatterns = [
    path('agregar_planta/', views.registro, name='agregar_panta'),
   
]

