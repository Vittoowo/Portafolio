from django.shortcuts import redirect, render
from django.db import connection
from django.contrib.auth.decorators import login_required
from reservas.models import Reservas as reservas
from mesas.models import Mesas
from datetime import datetime
# Create your views here.

@login_required
def Reservas(request):
    
    data ={
        'Reserva':reservas.listado_reservas(),
        'Lista_Mesas':Mesas.listado_mesa(),
        
    }
    if 'Guardar' in request.POST:
        rut_reserva = request.POST.get('RutReserva') + " - " + request.POST.get('DVRUTReserva')
        fecha_reserva=str(datetime.strptime(request.POST.get('FechaReserva'), '%Y-%m-%d').date().strftime("%d-%m-%Y"))+" "+request.POST.get('HoraReserva')
        email = request.POST.get('Email')
        telefono_reserva = request.POST.get('Telefono')
        cantidad_personas_reserva = request.POST.get('CantidadPersonas')
        mesas_id_mesa = request.POST.get('MesaReserva')
        salida = reservas.agregar_reserva( rut_reserva, fecha_reserva, email, telefono_reserva, cantidad_personas_reserva,mesas_id_mesa)
        if salida == 1:
            data['Mensaje'] = 'Reserva Agregada'
            data['Reserva'] = reservas.listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Reservas.html', data)
    elif 'btnBuscarReservaPorRUT' in request.POST:
        RUT_RESERVA = request.POST.get('BuscarReservaRUT')
        data['Reserva'] = reservas.buscar_reservas_por_rut(RUT_RESERVA)
        return render(request, 'Reservas.html', data)

    elif 'btnTodasLasReservas' in request.POST:
        data['Reserva'] = reservas.listado_reservas()
        return render(request, 'Reservas.html', data)
    
    return render(request, 'Reservas.html', data)
    
def modificarReservas(request,id):
    
    rsv=reservas.buscar_reservas_por_id(id)
    data ={
        'Lista_Estado_Reserva':reservas.listar_estados(),
        'Lista_Mesas':Mesas.listado_mesa(),
        'reserva':rsv[0],
        'mesaR':rsv[0][1],
        'estadoR':rsv[0][6],
        'fecha': rsv[0][4],
    }
    if 'Modificar' in request.POST:
        ID_RESERVA = request.POST.get('ID_RESERVA')
        ESTADO_RESERVA_ID_EST_RESERVA = request.POST.get('EstadoReserva')
        RUT_RESERVA = request.POST.get('RutReserva') + " - " + request.POST.get('DVRUTReserva')
        FECHA_RESERVA=str(datetime.strptime(request.POST.get('FechaReserva'), '%Y-%m-%d').date().strftime("%d-%m-%Y"))+" "+request.POST.get('HoraReserva')
        EMAIL = request.POST.get('Email')
        TELEFONO_RESERVA = request.POST.get('Telefono')
        CANTIDAD_PERSONAS_RESERVA = request.POST.get('CantidadPersonas')
        NUM_MESA = request.POST.get('MesaReserva')
        print("Los resultados son: " , NUM_MESA)
        salida = reservas.modificar_reserva(ID_RESERVA, ESTADO_RESERVA_ID_EST_RESERVA, RUT_RESERVA, FECHA_RESERVA, EMAIL, TELEFONO_RESERVA,CANTIDAD_PERSONAS_RESERVA, NUM_MESA)
        if salida == 1:
            data['Mensaje'] = 'Reserva Modificada'
            data['Reserva'] = reservas.listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido modificar'
        return redirect(to='reservas')
    elif 'Eliminar' in request.POST:
        salida = reservas.eliminar_reserva(id)
        if salida == 1:
            data['Mensaje'] = 'Reserva Eliminada'
            data['Reserva'] = reservas.listado_reservas()
        else:
            data['Mensaje'] = 'No se ha podido eliminar'
        return redirect(to='reservas') 
    
    return render(request,'Reservas-modificar.html', data)

def ConfirmarReserva(request, rut, dvRut, num_mesa, estado_mesa, capacidad ):
    data = {
        'rut': rut,
        'dv': dvRut,
        'numMesa': num_mesa,
        'estadoMesa':estado_mesa,
        'capacidadMesa': capacidad,
        'fecha': datetime.today().strftime('%Y-%m-%d')
    }
    if 'ConfirmarReserva' in request.POST:
        if request.POST.get('CantidadPersonas')<=capacidad:
            ESTADO_RESERVA_ID_EST_RESERVA = 1
            RUT_RESERVA = request.POST.get('RutReserva') + " - " + request.POST.get('DVRUTReserva')
            FECHA_RESERVA = request.POST.get('FechaReserva')
            CANTIDAD_PERSONAS_RESERVA = request.POST.get('CantidadPersonas')
            MESAS_ID_MESA = request.POST.get('IDMesa')
            salida = reservas.agregar_reserva_totem(ESTADO_RESERVA_ID_EST_RESERVA, RUT_RESERVA, FECHA_RESERVA, CANTIDAD_PERSONAS_RESERVA ,MESAS_ID_MESA)
            if salida == 1:
                data['Mensaje'] = 'Reserva Agregada'
            else:
                data['Mensaje'] = 'No se ha podido guardar'
        return render(request, 'Reserva-Realizada.html')

    return render(request, 'Confirmar-Reserva.html', data)

