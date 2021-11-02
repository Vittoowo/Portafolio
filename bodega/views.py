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

    #Metodo para captar el producto a ingresar
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

    #Metodo para captar el producto a modificar
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

    #Metodo para captar el producto a eliminar
    elif 'Eliminar' in request.POST:
        ID_PRODUCTO = request.POST.get('IDProducto')
        salida = Producto.eliminar_producto(ID_PRODUCTO)
        if salida == 1:
            data['Mensaje'] = 'Producto Eliminado'
            data['Producto'] = Producto.listar_productos()
        else:
            data['Mensaje'] = 'No se ha podido eliminar'
        return render(request, 'Bodega.html', data)

    #Metodo para captar el producto a buscar segun codigo de barras
    elif 'btnBuscarProductoCodigo' in request.POST:
        ID_PRODUCTO = request.POST.get('BuscarProductoPorCodigo')
        data['Producto'] = Producto.buscar_productos_por_codigo(ID_PRODUCTO)
        return render(request, 'Bodega.html', data)

    #Metodo para captar el producto a buscar segun proveedor
    elif 'btnBuscarProductoProveedor' in request.POST:
        PROVEEDOR_ID_PROVEEDOR = request.POST.get('BuscarProductoPorProveedor')
        data['Producto'] = Producto.buscar_productos_por_proveedor(PROVEEDOR_ID_PROVEEDOR)
        return render(request, 'Bodega.html', data)
    
    #Metodo para captar el producto a buscar segun marca
    elif 'btnBuscarProductoMarca' in request.POST:
        MARCA_PRODUCTO_ID_MARCA = request.POST.get('BuscarProductoPorMarca')
        data['Producto'] = Producto.buscar_productos_por_marca(MARCA_PRODUCTO_ID_MARCA)
        return render(request, 'Bodega.html', data)

    #Metodo para captar el producto a buscar segun stock
    elif 'btnBuscarProductoStock' in request.POST:
        STOCK = request.POST.get('BuscarProductoPorStock')
        data['Producto'] = Producto.buscar_productos_por_stock(STOCK)
        return render(request, 'Bodega.html', data)

    #Metodo para captar todos los productos a traves de 1 boton
    elif 'btnTodosLosProductos' in request.POST:
        data['Producto'] = Producto.listar_productos()
        return render(request, 'Bodega.html', data)
    return render(request, 'Bodega.html', data)
    