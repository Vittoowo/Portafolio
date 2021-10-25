from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required
from bodega.models import Bodega as bodega
# Create your views here.

@login_required
def Bodega(request):
    data ={
        'mensaje': "",
    }

    if 'Guardar' in request.POST:
            id_prod = int(request.POST.get('id_prod'))
            marca_prod= request.post.get('marca_prod')
            nombre_prod=request.POST.get('nombre_prod')
            proveedor_prod=request.POST.get('estado')
            precio_compra= int(request.POST.get('precio_compra'))
            ultima_compra = int(request.POST.get('ultima_compra'))
            prod_c=bodega(id_prod,marca_prod,proveedor_prod,precio_compra,ultima_compra) #creando el objeto
            salida = prod_c.agregar_producto()#llamamos al metodo del models, creamos una variable y le asigna el valor que va a retornar
            if salida==1:
                print 
                data['mensaje'] = 'Producto agregado correctamente👍'
            else:
                data['mensaje'] = f'ERROR, no se pudo agregar el producto correctamente😢'
            return render(request, 'Bodega.html', data)