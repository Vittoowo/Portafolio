from django.shortcuts import render
from bodega.models import Producto 

# Create your views here.
def gestionPlatos(request):
    data = {"Producto":Producto.listar_productos()}
    return render(request,'gestion-platos.html',data)