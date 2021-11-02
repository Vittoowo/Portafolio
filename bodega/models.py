from django.db import models
from django.contrib.auth.models import User, Group
from django.db import connection
from django.shortcuts import render
import cx_Oracle
# Create your models here.

    
class Producto():

    def __init__(self,ID_PRODUCTO, NOM_PRODUCTO, PROVEEDOR, MARCA, STOCK, FORMATO_STOCK, MEDIDA, UNIDAD_MEDIDA):
        self.ID_PRODUCTO = ID_PRODUCTO
        self.NOM_PRODUCTO = NOM_PRODUCTO
        self.PROVEEDOR = PROVEEDOR
        self.MARCA = MARCA
        self.STOCK = STOCK
        self.FORMATO_STOCK = FORMATO_STOCK
        self.MEDIDA = MEDIDA
        self.UNIDAD_MEDIDA = UNIDAD_MEDIDA


    #Metodo para llamar al procedimiento para listar las marcas
    def listar_marcas():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_LISTAR_MARCAS",[out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista

    
    #Metodo para llamar al procedimiento para listar los formatos de stock
    def listar_formato_stock():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_LISTAR_FORMATO_STOCK",[out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista


    #Metodo para llamar al procedimiento para listar los proveedores
    def listar_proveedores():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_LISTAR_PROVEEDORES",[out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista

    
    #Metodo para llamar al procedimiento para listar los productos
    def listar_productos():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista

    #Metodo para llamar al procedimiento para listar las unidades de medida
    def listar_unidades_medida():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_LISTAR_MEDIDAS", [out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista


    #Metodo para llamar al procedimiento para agregar un producto
    def agregar_producto(ID_PRODUCTO, NOM_PRODUCTO, PROVEEDOR_ID_PROVEEDOR, MARCA_PRODUCTO_ID_MARCA, STOCK, FORMATO_STOCK_ID_FORMATO, MEDIDA, UNIDAD_MEDIDA_ID_UNIDAD):
        try:
            django_cursor = connection.cursor()
            cursor = django_cursor.connection.cursor()
            salida= cursor.var(cx_Oracle.NUMBER)
            cursor.callproc ('SP_AGREGAR_PRODUCTO',[ID_PRODUCTO, NOM_PRODUCTO, PROVEEDOR_ID_PROVEEDOR, MARCA_PRODUCTO_ID_MARCA, STOCK, FORMATO_STOCK_ID_FORMATO, MEDIDA, UNIDAD_MEDIDA_ID_UNIDAD, salida])
            return salida.getvalue()
        except Exception as e:
            raise e.__str__()
    

    #Metodo para llamar al procedimiento para modificar un producto
    def modificar_producto(ID_PRODUCTO, NOM_PRODUCTO, PROVEEDOR_ID_PROVEEDOR, MARCA_PRODUCTO_ID_MARCA, STOCK, FORMATO_STOCK_ID_FORMATO, MEDIDA, UNIDAD_MEDIDA_ID_UNIDAD):
        try:
            django_cursor = connection.cursor()
            cursor = django_cursor.connection.cursor()
            salida= cursor.var(cx_Oracle.NUMBER)
            cursor.callproc ('SP_MODIFICAR_PRODUCTO',[ID_PRODUCTO, NOM_PRODUCTO, PROVEEDOR_ID_PROVEEDOR, MARCA_PRODUCTO_ID_MARCA, STOCK, FORMATO_STOCK_ID_FORMATO, MEDIDA, UNIDAD_MEDIDA_ID_UNIDAD, salida])
            return salida.getvalue()
        except Exception as e:
            raise e.__str__()

    
    #Metodo para llamar al procedimiento para eliminar un producto
    def eliminar_producto(ID_PRODUCTO):
        try:
            django_cursor = connection.cursor()
            cursor = django_cursor.connection.cursor()
            salida= cursor.var(cx_Oracle.NUMBER)
            cursor.callproc ('SP_ELIMINAR_PRODUCTO',[ID_PRODUCTO, salida])
            return salida.getvalue()
        except Exception as e:
            raise e.__str__()


    #Metodo para llamar al procedimiento buscar productos segun codigo de barras
    def buscar_productos_por_codigo(ID_PRODUCTO):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_BUSCAR_PRODUCTOS_POR_CODIGO", [ID_PRODUCTO, out_cur])
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista


    #Metodo para llamar al procedimiento buscar productos segun proveedor
    def buscar_productos_por_proveedor(PROVEEDOR_ID_PROVEEDOR):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_BUSCAR_PRODUCTOS_POR_PROVEEDOR", [PROVEEDOR_ID_PROVEEDOR, out_cur])
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista

    #Metodo para llamar al procedimiento buscar productos segun marca
    def buscar_productos_por_marca(MARCA_PRODUCTO_ID_MARCA):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_BUSCAR_PRODUCTOS_POR_MARCA", [MARCA_PRODUCTO_ID_MARCA, out_cur])
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista

    #Metodo para llamar al procedimiento buscar productos segun stock
    def buscar_productos_por_stock(STOCK):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_BUSCAR_PRODUCTOS_POR_STOCK", [STOCK, out_cur])
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista
