from django.urls import path
from .views import *


urlpatterns = [
    path('',Reservas,name='reservas'),
    path('modificar/<id>',modificarReservas,name='modificar-reservas'),
]
