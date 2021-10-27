from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required
from bodega.models import Producto
# Create your views here.

@login_required
def Bodega(request):
    data ={
        'Producto': Producto.listar_productos(),
        'Listado_Proveedores': Producto.listar_proveedores(),
        'Listado_Marcas': Producto.listar_marcas(),
        'Listado_Formato_Stock': Producto.listar_formato_stock(),
        'Listado_Unidades_Medida': Producto.listar_unidades_medida(), 
        'Mensaje': "",
    }

    if 'Guardar' in request.POST:
        ID_PRODUCTO = request.POST.get('IDProducto')
        NOM_PRODUCTO = request.POST.get('NombreProducto')
        PROVEEDOR_ID_PROVEEDOR = request.POST.get('ProveedorProducto')
        MARCA_PRODUCTO_ID_MARCA = request.POST.get('MarcaProducto')
        STOCK = request.POST.get('StockProducto')
        FORMATO_STOCK_ID_FORMATO = request.POST.get('FormatoStockProducto')
        MEDIDA = request.POST.get('MedidaProducto')
        UNIDAD_MEDIDA_ID_UNIDAD = request.POST.get('UnidadMedidaProducto')
        salida = Producto.agregar_producto(ID_PRODUCTO, NOM_PRODUCTO, PROVEEDOR_ID_PROVEEDOR, MARCA_PRODUCTO_ID_MARCA, STOCK, FORMATO_STOCK_ID_FORMATO, MEDIDA, UNIDAD_MEDIDA_ID_UNIDAD)
        if salida == 1:
            data['Mensaje'] = 'Producto Agregado'
            data['Producto'] = Producto.listar_productos()
        else:
            data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Bodega.html', data)


    elif 'Modificar' in request.POST:
        ID_PRODUCTO = request.POST.get('IDProducto')
        NOM_PRODUCTO = request.POST.get('NombreProducto')
        PROVEEDOR_ID_PROVEEDOR = request.POST.get('ProveedorProducto')
        MARCA_PRODUCTO_ID_MARCA = request.POST.get('MarcaProducto')
        STOCK = request.POST.get('StockProducto')
        FORMATO_STOCK_ID_FORMATO = request.POST.get('FormatoStockProducto')
        MEDIDA = request.POST.get('MedidaProducto')
        UNIDAD_MEDIDA_ID_UNIDAD = request.POST.get('UnidadMedidaProducto')
        salida = Producto.modificar_producto(ID_PRODUCTO, NOM_PRODUCTO, PROVEEDOR_ID_PROVEEDOR, MARCA_PRODUCTO_ID_MARCA, STOCK, FORMATO_STOCK_ID_FORMATO, MEDIDA, UNIDAD_MEDIDA_ID_UNIDAD)
        if salida == 1:
            data['Mensaje'] = 'Producto Modificado'
            data['Producto'] = Producto.listar_productos()
        else:
            data['Mensaje'] = 'No se ha podido modificar'
        return render(request, 'Bodega.html', data)

    elif 'Eliminar' in request.POST:
        ID_PRODUCTO = request.POST.get('IDProducto')
        salida = Producto.eliminar_producto(ID_PRODUCTO)
        if salida == 1:
            data['Mensaje'] = 'Producto Eliminado'
            data['Producto'] = Producto.listar_productos()
        else:
            data['Mensaje'] = 'No se ha podido eliminar'
        return render(request, 'Bodega.html', data)
    return render(request, 'Bodega.html', data)
    