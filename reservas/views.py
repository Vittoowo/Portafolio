from django.shortcuts import redirect, render
from django.db import connection
import cx_Oracle
# Create your views here.


def Reservas(request):
    data ={
        'Lista_Estado_Reserva':listar_estados(),
        'Reserva':listado_reservas()
    }
    
    if 'Guardar' in request.POST:
        ID_RESERVA = request.POST.get('IDReserva')
        ESTADO_RESERVA_ID_EST_RESERVA = request.POST.get('EstadoReserva')
        RUT_RESERVA = request.POST.get('RutReserva')
        FECHA_RESERVA = request.POST.get('FechaReserva')
        EMAIL = request.POST.get('Email')
        TELEFONO_RESERVA = request.POST.get('Telefono')
        CANTIDAD_PERSONAS_RESERVA = request.POST.get('CantidadPersonas')
        salida = agregar_reserva(ID_RESERVA, ESTADO_RESERVA_ID_EST_RESERVA, RUT_RESERVA, FECHA_RESERVA, EMAIL, TELEFONO_RESERVA, CANTIDAD_PERSONAS_RESERVA)
        if salida == 1:
            data['Mensaje'] = 'Reserva Agregada'
            data['Reserva'] = listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Reservas.html', data)
    
    elif 'Eliminar' in request.POST:
        ID_RESERVA = request.POST.get('IDReserva')
        salida = eliminar_reserva (ID_RESERVA)
        if salida == 1:
            data['Mensaje'] = 'Reserva Eliminada'
            data['Reserva'] = listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido eliminar'
        return render(request, 'Reservas.html', data)

    elif 'Modificar' in request.POST:
        ID_RESERVA = request.POST.get('IDReserva')
        ESTADO_RESERVA_ID_EST_RESERVA = request.POST.get('EstadoReserva')
        RUT_RESERVA = request.POST.get('RutReserva')
        FECHA_RESERVA = request.POST.get('FechaReserva')
        EMAIL = request.POST.get('Email')
        TELEFONO_RESERVA = request.POST.get('Telefono')
        CANTIDAD_PERSONAS_RESERVA = request.POST.get('CantidadPersonas')
        salida = modificar_reserva(ID_RESERVA, ESTADO_RESERVA_ID_EST_RESERVA, RUT_RESERVA, FECHA_RESERVA, EMAIL, TELEFONO_RESERVA, CANTIDAD_PERSONAS_RESERVA)
        if salida == 1:
            data['Mensaje'] = 'Reserva Modificada'
            data['Reserva'] = listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido modificar'
        return render(request, 'Reservas.html', data)
    return render(request, 'Reservas.html', data)
    


def listar_estados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_R_ESTADO_RESERVA",[out_cur])
    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista

def listado_reservas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RESERVAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista


def agregar_reserva(ID_RESERVA, estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA',[ID_RESERVA,estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva, salida])
    return salida.getvalue()



def eliminar_reserva(ID_RESERVA):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_ELIMINAR_RESERVA',[ID_RESERVA, salida])
    return salida.getvalue()

def modificar_reserva(ID_RESERVA, estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_MODIFICAR_RESERVA',[ID_RESERVA,estado_reserva_id_est_reserva, rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva, salida])
    return salida.getvalue()