from django.urls import path
from .views import *

urlpatterns = [
    path('mesas/',Mesas,name='mesas'),
    path('MesasDisponibles/',mesas_totem, name= 'mesas_totem'),
]