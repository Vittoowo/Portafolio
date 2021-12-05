from django.shortcuts import render
from bodega.models import Producto 

# Create your views here.
def gestionPlatos(request):
    data = {"Producto":Producto.listar_productos(), "UnidadMedidaProducto":Producto.listar_unidades_medida()}
    return render(request,'gestion-platos.html',data)