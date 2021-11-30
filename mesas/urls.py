from django.urls import path
from .views import *

urlpatterns = [
    path('mesas/',Mesas,name='mesas'),
    path('MesasDisponibles/',mesas_totem, name= 'mesas_totem'),
    path('MesasModificar/<num_mesa>/<capacidad>/<estado>',mesas_modificar, name= 'mesasModificar'),
    path('Home_totem/',Home_totem, name='Home_totem'),
]