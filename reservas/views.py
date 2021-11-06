from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required
from reservas.models import Reservas as reservas
from mesas.models import Mesas
# Create your views here.

@login_required
def Reservas(request):
    data ={
        'Lista_Estado_Reserva':reservas.listar_estados(),
        'Reserva':reservas.listado_reservas(),
        'Lista_Mesas':Mesas.listado_mesa(),
    }
    
    if 'Guardar' in request.POST:
        ID_RESERVA = request.POST.get('IDReserva')
        ESTADO_RESERVA_ID_EST_RESERVA = request.POST.get('EstadoReserva')
        RUT_RESERVA = request.POST.get('RutReserva') + " - " + request.POST.get('DVRUTReserva')
        FECHA_RESERVA = request.POST.get('FechaReserva') + " " + request.POST.get('HoraReserva')
        EMAIL = request.POST.get('Email')
        TELEFONO_RESERVA = request.POST.get('Telefono')
        CANTIDAD_PERSONAS_RESERVA = request.POST.get('CantidadPersonas')
        NUM_MESA = request.POST.get('MesaReserva')
        salida = reservas.agregar_reserva(ID_RESERVA, ESTADO_RESERVA_ID_EST_RESERVA, RUT_RESERVA, FECHA_RESERVA, EMAIL, TELEFONO_RESERVA, CANTIDAD_PERSONAS_RESERVA,NUM_MESA)
        if salida == 1:
            data['Mensaje'] = 'Reserva Agregada'
            data['Reserva'] = reservas.listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Reservas.html', data)
    
    elif 'Eliminar' in request.POST:
        ID_RESERVA = request.POST.get('IDReserva')
        salida = reservas.eliminar_reserva(ID_RESERVA)
        if salida == 1:
            data['Mensaje'] = 'Reserva Eliminada'
            data['Reserva'] = reservas.listado_reservas()
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
        NUM_MESA = request.POST.get('MesaReserva')
        salida = reservas.modificar_reserva(ID_RESERVA, ESTADO_RESERVA_ID_EST_RESERVA, RUT_RESERVA, FECHA_RESERVA, EMAIL, TELEFONO_RESERVA,CANTIDAD_PERSONAS_RESERVA, NUM_MESA)
        if salida == 1:
            data['Mensaje'] = 'Reserva Modificada'
            data['Reserva'] = reservas.listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido modificar'
        return render(request, 'Reservas.html', data)

    elif 'btnBuscarReservaPorRUT' in request.POST:
        RUT_RESERVA = request.POST.get('BuscarReservaRUT')
        data['Reserva'] = reservas.buscar_reservas_por_rut(RUT_RESERVA)
        return render(request, 'Reservas.html', data)

    elif 'btnTodasLasReservas' in request.POST:
        data['Reserva'] = reservas.listado_reservas()
        return render(request, 'Reservas.html', data)
    
    return render(request, 'Reservas.html', data)
    


