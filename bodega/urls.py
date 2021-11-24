from django.urls import path
from .views import *


urlpatterns = [
    path('productos',Productos,name='productos'),
    path('insumos',Insumos,name='insumos'),
    path('insumosModificar/<ID_INSUMO>',insumosModificar, name= 'modificar-insumo'),
    path('productosModificar/<ID_PRODUCTO>',productosModificar, name= 'modificar-producto'),
]