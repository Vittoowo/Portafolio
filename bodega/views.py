from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required
from bodega.models import *
# Create your views here.

@login_required
def Productos(request):
    data ={
        'Producto': Producto.listar_productos(),
        'Listado_Proveedores': Bodega.listar_proveedores(),
        'Listado_Marcas': Bodega.listar_marcas(),
        'Listado_Formato_Stock': Bodega.listar_formato_stock(),
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
        FORMATO_STOCK_ID_FORMATO_STOCK = request.POST.get('FormatoStockProducto')
        MEDIDA_STOCK = request.POST.get('MedidaProducto')
        UNIDAD_MEDIDA_ID_UNIDAD = request.POST.get('UnidadMedidaProducto')
        salida = Producto.agregar_producto(ID_PRODUCTO,
                            NOM_PRODUCTO,
                            PROVEEDOR_ID_PROVEEDOR,
                            MARCA_PRODUCTO_ID_MARCA,
                            STOCK,
                            FORMATO_STOCK_ID_FORMATO_STOCK,
                            MEDIDA_STOCK,
                            UNIDAD_MEDIDA_ID_UNIDAD)
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
        FORMATO_STOCK_ID_FORMATO_STOCK = request.POST.get('FormatoStockProducto')
        MEDIDA_STOCK = request.POST.get('MedidaProducto')
        UNIDAD_MEDIDA_ID_UNIDAD = request.POST.get('UnidadMedidaProducto')
        salida = Producto.modificar_producto(ID_PRODUCTO,
                            NOM_PRODUCTO,
                            PROVEEDOR_ID_PROVEEDOR,
                            MARCA_PRODUCTO_ID_MARCA,
                            STOCK,
                            FORMATO_STOCK_ID_FORMATO_STOCK,
                            MEDIDA_STOCK,
                            UNIDAD_MEDIDA_ID_UNIDAD)
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
    




@login_required
def Insumos(request):
    data ={
        'Insumos': Insumo.listar_insumos(),
        'Listado_Proveedores': Bodega.listar_proveedores(),
        'Listado_Formato_Stock': Bodega.listar_formato_stock(),
        'Mensaje': "",
    }

    #Metodo para captar el Insumo a ingresar
    if 'Guardar' in request.POST:
        ID_INSUMO = request.POST.get('IDInsumo')
        NOM_INSUMO = request.POST.get('NombreInsumo')
        STOCK = request.POST.get('StockInsumo')
        PROVEEDOR_ID_PROVEEDOR = request.POST.get('ProveedorInsumo')
        FORMATO_STOCK_ID_FORMATO = request.POST.get('FormatoStockInsumo')
        salida = Insumo.agregar_insumo(ID_INSUMO,NOM_INSUMO, STOCK, PROVEEDOR_ID_PROVEEDOR, FORMATO_STOCK_ID_FORMATO)
        if salida == 1:
            data['Mensaje'] = 'Insumo Agregado'
            data['Insumos'] = Insumo.listar_insumos()
        else:
            data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Insumos.html', data)

    #Metodo para captar el Insumo a modificar
    elif 'Modificar' in request.POST:
        ID_INSUMO = request.POST.get('IDInsumo')
        NOM_INSUMO = request.POST.get('NombreInsumo')
        STOCK = request.POST.get('StockInsumo')
        PROVEEDOR_ID_PROVEEDOR = request.POST.get('ProveedorInsumo')
        FORMATO_STOCK_ID_FORMATO = request.POST.get('FormatoStockInsumo')
        salida = Insumo.modificar_insumo(ID_INSUMO,NOM_INSUMO, STOCK, PROVEEDOR_ID_PROVEEDOR, FORMATO_STOCK_ID_FORMATO)
        if salida == 1:
            data['Mensaje'] = 'Insumo Modificado'
            data['Insumos'] = Insumo.listar_insumos()
        else:
            data['Mensaje'] = 'No se ha podido modificar'
        return render(request, 'Insumos.html', data)

    #Metodo para captar el insumo a eliminar
    elif 'Eliminar' in request.POST:
        ID_INSUMO = request.POST.get('IDInsumo')
        salida = Insumo.eliminar_insumo(ID_INSUMO)
        if salida == 1:
            data['Mensaje'] = 'Insumo Eliminado'
            data['Insumos'] = Insumo.listar_insumos()
        else:
            data['Mensaje'] = 'No se ha podido eliminar'
        return render(request, 'Insumos.html', data)

    #Metodo para captar el insumo a buscar segun codigo de barras
    elif 'btnBuscarInsumoCodigo' in request.POST:
        ID_INSUMO = request.POST.get('BuscarInsumoPorCodigo')
        data['Insumos'] = Insumo.buscar_insumos_por_codigo(ID_INSUMO)
        return render(request, 'Insumos.html', data)

    #Metodo para captar el insumo a buscar segun proveedor
    elif 'btnBuscarInsumoProveedor' in request.POST:
        PROVEEDOR_ID_PROVEEDOR = request.POST.get('BuscarInsumoPorProveedor')
        data['Insumos'] = Insumo.buscar_insumos_por_proveedor(PROVEEDOR_ID_PROVEEDOR)
        return render(request, 'Insumos.html', data)

    #Metodo para captar el insumo a buscar segun stock
    elif 'btnBuscarInsumoStock' in request.POST:
        STOCK = request.POST.get('BuscarInsumoPorStock')
        data['Insumos'] = Insumo.buscar_insumos_por_stock(STOCK)
        return render(request, 'Insumos.html', data)

    #Metodo para captar todos los insumos a traves de 1 boton
    elif 'btnTodosLosInsumos' in request.POST:
        data['Insumos'] = Insumo.listar_insumos()
        return render(request, 'Insumos.html', data)

    
    elif 'Cancelar' in request.POST:
        return render(request, 'Insumos.html', data)

    return render(request, 'Insumos.html', data)

    
def productosModificar(request,ID_PRODUCTO):
    
    pro=Producto.buscar_productos_por_codigo(ID_PRODUCTO)
    data ={
        'Listado_Proveedores': Bodega.listar_proveedores(),
        'Listado_Marcas': Bodega.listar_marcas(),
        'Listado_Unidades_Medida': Producto.listar_unidades_medida(),
        'Listado_Formato_Stock': Bodega.listar_formato_stock(),
        'Producto':pro[0],
        'proveedorPro':pro[0][2],
        'marcaPro':pro[0][3],
        'formStockPro':pro[0][5],
        'unidadMedidaPro':pro[0][7]
    }
    
    return render(request,'Bodega-Modificar.html', data)


def insumosModificar(request,ID_INSUMO):
    
    ins=Insumo.buscar_insumos_por_codigo(ID_INSUMO)
    data ={
        'Listado_Proveedores': Bodega.listar_proveedores(),
        'Listado_Formato_Stock': Bodega.listar_formato_stock(),
        'Insumo':ins[0],
        'proveedorIns':ins[0][3],
        'formStockIns':ins[0][4],
    }
    
    return render(request,'Insumos-Modificar.html', data)



def Proveedores(request):
    data={
        'Proveedores': Bodega.listar_proveedores()
    }
    if 'Guardar' in request.POST:
        ID_PROVEEDOR = request.POST.get('IDProveedor')
        NOMBRE_PROVEEDOR = request.POST.get('NombreProveedor')
        salida = Proveedor.agregar_proveedor(ID_PROVEEDOR,NOMBRE_PROVEEDOR)
        if salida == 1:
            data['Mensaje'] = 'Proveedor Agregado'
            data['Proveedores'] = Bodega.listar_proveedores()
        else:
            data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Proveedores.html', data)
    
    if 'Modificar' in request.POST:
        ID_PROVEEDOR = request.POST.get('IDProveedor')
        NOMBRE_PROVEEDOR = request.POST.get('NombreProveedor')
        salida = Proveedor.modificar_proveedor(ID_PROVEEDOR,NOMBRE_PROVEEDOR)
        if salida == 1:
            data['Mensaje'] = 'Proveedor Modificado'
            data['Proveedores'] = Bodega.listar_proveedores()
        else:
            data['Mensaje'] = 'No se ha podido modificar'
        return render(request, 'Proveedores.html', data)
    
    if 'Eliminar' in request.POST:
        ID_PROVEEDOR = request.POST.get('IDProveedor')
        salida = Proveedor.eliminar_proveedor(ID_PROVEEDOR)
        if salida == 1:
            data['Mensaje'] = 'Proveedor Eliminado'
            data['Proveedores'] = Bodega.listar_proveedores()
        else:
            data['Mensaje'] = 'No se ha podido eliminar'
        return render(request, 'Proveedores.html', data)
    
    if 'btnBuscarProveedorNombre' in request.POST:
        NOMBRE_PROVEEDOR = request.POST.get('BuscarProveedorPorNombre')
        data['Proveedores'] = Proveedor.buscar_proveedor_por_nombre(NOMBRE_PROVEEDOR)
        return render(request, 'Proveedores.html', data)

    if 'btnTodosLosProveedores' in request.POST:
        data['Proveedores'] = Bodega.listar_proveedores()
        return render(request, 'Proveedores.html', data)

    elif 'Cancelar' in request.POST:
        return render(request, 'Proveedores.html', data)
        
    return render(request, 'Proveedores.html',data)


def proveedorModificar(request, NOMBRE_PROVEEDOR):
    prov=Proveedor.buscar_proveedor_por_nombre(NOMBRE_PROVEEDOR)
    data={
        'IDProveedor': prov[0][0],
        'NombreProveedor': prov[0][1]
    }
    return render(request,'Proveedores-Modificar.html',data)
    


def Marcas(request):
    data={
        'Marcas': Bodega.listar_marcas()
    }
    if 'Guardar' in request.POST:
        ID_MARCA = request.POST.get('IDMarca')
        MARCA = request.POST.get('NombreMarca')
        salida = Marca.agregar_marca(ID_MARCA,MARCA)
        if salida == 1:
            data['Mensaje'] = 'Marca Agregada'
            data['Marcas'] = Bodega.listar_marcas()
        else:
            data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Marcas.html', data)

    if 'Modificar' in request.POST:
        ID_MARCA = request.POST.get('IDMarca')
        MARCA = request.POST.get('NombreMarca')
        salida = Marca.modificar_marca(ID_MARCA,MARCA)
        if salida == 1:
            data['Mensaje'] = 'Marca Modificada'
            data['Marcas'] = Bodega.listar_marcas()
        else:
            data['Mensaje'] = 'No se ha podido modificar'
        return render(request, 'Marcas.html', data)

    if 'Eliminar' in request.POST:
        ID_MARCA = request.POST.get('IDMarca')
        salida = Marca.eliminar_marca(ID_MARCA)
        if salida == 1:
            data['Mensaje'] = 'Marca Eliminada'
            data['Marcas'] = Bodega.listar_marcas()
        else:
            data['Mensaje'] = 'No se ha podido eliminar'
        return render(request, 'Marcas.html', data)
    
    if 'btnBuscarMarcaNombre' in request.POST:
        MARCA = request.POST.get('BuscarMarcaPorNombre')
        data['Marcas'] = Marca.buscar_marca_por_nombre(MARCA)
        return render(request, 'Marcas.html', data)

    if 'btnTodasLasMarcas' in request.POST:
        data['Marcas'] = Bodega.listar_marcas()
        return render(request, 'Marcas.html', data)

    elif 'Cancelar' in request.POST:
        return render(request, 'Marcas.html', data)
    return render (request, 'Marcas.html',data)

def marcaModificar(request, MARCA):
    marc = Marca.buscar_marca_por_nombre(MARCA)
    data={
        'IDMarca': marc[0][0],
        'NombreMarca': marc[0][1]
    }
    return render(request,'Marcas-Modificar.html',data)