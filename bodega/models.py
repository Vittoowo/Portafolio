from django.db import models
from django.contrib.auth.models import User, Group
from django.db import connection
from django.shortcuts import render
import cx_Oracle
# Create your models here.


#bodega v_id_prod in NUMBER,
    
class Bodega():
    def __init__(self,nombre_prod,marca_prod,proveedor_prod,precio_compra,ultima_compra):
        self.nombre_prod = nombre_prod
        self.marca_prod=marca_prod
        self.proveedor_prod=proveedor_prod
        self.precio_compra= precio_compra
        self.ultima_compra= ultima_compra

    def agregar_producto(self):
            try:
                django_cursor = connection.cursor()
                cursor = django_cursor.connection.cursor()
                salida= cursor.var(cx_Oracle.NUMBER)
                cursor.callproc ('SP_CREATE_PRODUCTOS',[self.nombre_prod,self.marca_prod,self.proveedor_prod,
                self.precio_compra,self.ultima_compra,salida])
                return salida.getvalue()
            except Exception as e:
                raise e.__str__()
