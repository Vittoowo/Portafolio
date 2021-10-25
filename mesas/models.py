from django.contrib.auth.models import User, Group
from django.db import models
from django.db import connection
from django.shortcuts import render
import cx_Oracle

#mesas
class Mesas():
    def __init__(self,id_mesa,cant_mesa,id_estado_mesa):
        self.id_mesa = id_mesa
        self.cant_mesa=cant_mesa
        self.id_estado_mesa=id_estado_mesa
    def listado_mesa():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor() #llama
        out_cur= django_cursor.connection.cursor() #recibe
        #voy a llamar al procedimiento almacedado desde el cursor
        cursor.callproc("SP_READ_MESAS",[out_cur])
        #lo paso de cursor a listado
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista

    def listar_estados():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_R_ESTADO_MESA",[out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista

    #AGREGAR
    def agregar_mesa(self):
        try:
            django_cursor = connection.cursor()
            cursor = django_cursor.connection.cursor()
            salida= cursor.var(cx_Oracle.NUMBER)
            cursor.callproc ('SP_CREATE_MESAS',[self.id_mesa,self.cant_mesa,self.id_estado_mesa,salida])
            return salida.getvalue()
        except Exception as e:
            raise e.__str__()
    
    #ELIMINAR 
    def eliminar_mesa(id_mesa):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc('SP_DELETE_MESAS',[id_mesa,salida])
        return salida.getvalue()

    #MODIFICAR 
    def modificar_mesa(self,id_mesa,cant_mesa,id_estado_mesa):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc('SP_UPDATE_MESAS',[self.id_mesa, self.cant_mesa, self.id_estado_mesa,salida])
        return salida.getvalue()

    #METODO QUE SOLO CAMBIA EL ESTADO DE LA MESA
    def modificar_estado_mesa(self,id_estado_mesa):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc('SP_UPDATE_ESTADO',[self.id_estado_mesa,salida])
        return salida.getvalue()