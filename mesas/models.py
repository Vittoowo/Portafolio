from django.db import models
from django.db import connection
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

    