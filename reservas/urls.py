from django.urls import path
from .views import *


urlpatterns = [
    path('',Reservas,name='reservas'),
    path('modificar/<id>',modificarReservas,name='modificar-reservas'),
    path('confirmarReserva/<rut>/<dvRut>/<num_mesa>/<estado_mesa>/<capacidad>', ConfirmarReserva, name='ConfirmarReserva'),
    path('reservaConfirmada',reservaConfirmada, name="ReservaConfirmada")
]
