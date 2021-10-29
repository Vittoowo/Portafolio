from django.urls import path, include
from .views import *

urlpatterns = [
    path('gestionPlatos', gestionPlatos,name='gestion-platos'),

    #path('Administrador/Reservas',rv.Reservas,name="reservas"), #modificar con include
    
    ##Agregar Reservas
    #Agregar Mesas
]