from django.urls import path
from .views import *


urlpatterns = [
    path('productos',Productos,name='productos'),
    path('insumos',Insumos,name='insumos')
]