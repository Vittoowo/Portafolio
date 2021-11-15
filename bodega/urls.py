from django.urls import path
from .views import *


urlpatterns = [
    path('Productos',Productos,name='bodega'),
    path('Insumos',Insumos,name='bodega')
]