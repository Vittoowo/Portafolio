from django.contrib.auth.models import User, Group
from django.db import models
from django.db import connection
from django.shortcuts import render
import cx_Oracle

class Reservas():
    def __init__(self,ID_RESERVA, ESTADO_RESERVA, RUT_RESERVA, FECHA_RESERVA, EMAIL_RESERVA, TELEFONO_RESERVA, CANTIDAD_PERSONAS_RESERVAS):
        self.ID_RESERVA = ID_RESERVA
        self.ESTADO_RESERVA = ESTADO_RESERVA
        self.RUT_RESERVA = RUT_RESERVA
        self.FECHA_RESERVA = FECHA_RESERVA
        self.EMAIL_RESERVA = EMAIL_RESERVA
        self.TELEFONO_RESERVA = TELEFONO_RESERVA
        self.CANTIDAD_PERSONAS_RESERVAS = CANTIDAD_PERSONAS_RESERVAS

        #Listado de estado de reserva
    def listar_estados():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_R_ESTADO_RESERVA",[out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista
    def listar_rangos():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_R_RANGO_HORA",[out_cur])
        lista=[]
        for fila in out_cur:
            lista.append(fila)
        return lista


        #Listado de Reservas
    def listado_reservas():
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()

        cursor.callproc("SP_LISTAR_RESERVAS", [out_cur])

        lista = []
        for fila in out_cur:
            lista.append(fila)

        return lista

    def buscar_reservas_por_rut(RUT_RESERVA):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_BUSCAR_RESERVAS_POR_RUT", [RUT_RESERVA, out_cur])
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista

        #Guardar Reserva
    def agregar_reserva( estado_reserva_id_est_reserva, rut_reserva, 
                        fecha_reserva,RANGO_HORA, email, telefono_reserva, 
                        cantidad_personas_reserva,num_mesa):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc('SP_AGREGAR_RESERVA',[estado_reserva_id_est_reserva, 
                                              rut_reserva, fecha_reserva,RANGO_HORA, email, telefono_reserva,
                                              cantidad_personas_reserva,num_mesa, salida])
        return salida.getvalue()

        #Eliminar Reserva
    def eliminar_reserva(ID_RESERVA):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc('SP_ELIMINAR_RESERVA',[ID_RESERVA, salida])
        return salida.getvalue()

        #Modificar Reserva
    def modificar_reserva(ID_RESERVA, estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva,num_mesa):
        
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida = cursor.var(cx_Oracle.NUMBER)
        cursor.callproc('SP_MODIFICAR_RESERVA',[ID_RESERVA,estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva,num_mesa, salida])
        return salida.getvalue()
    
    def buscar_reservas_por_id(ID_RESERVA):
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        out_cur = django_cursor.connection.cursor()
        cursor.callproc("SP_BUSCAR_RESERVAS_POR_ID", [ID_RESERVA, out_cur])
        lista = []
        for fila in out_cur:
            lista.append(fila)
        return lista