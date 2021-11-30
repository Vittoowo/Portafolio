from django.shortcuts import redirect, render
from django.db import connection
from django.contrib.auth.decorators import login_required
from mesas.models import Mesas as mesas

@login_required
def Mesas(request):
    data ={
        'lista_estado':mesas.listar_estados(),
        'mensaje': "",
        'Mesas' : mesas.listado_mesa(),
    }
      
    if 'Guardar' in request.POST:
        numeromesa = int(request.POST.get('idmesa'))
        cantidadpersonas=int(request.POST.get('capacidad'))
        estadomesa=int(request.POST.get('estado'))
        mesa_c=mesas(numeromesa,cantidadpersonas,estadomesa) 
        salida = mesa_c.agregar_mesa()
        if salida==1:
            print 
            data['mensaje'] = 'Mesa agregada correctamente'
            data['Mesas'] = mesas.listado_mesa()
        else:
            data['mensaje'] = f'No se pudo agregar la mesa'
        return render(request, 'Mesas.html', data)

    elif 'Eliminar' in request.POST:
        numeromesa= int (request.POST.get('idmesa'))
        salida = mesas.eliminar_mesa(numeromesa)
        if salida == 1:
            data['mensaje'] = 'Mesa Eliminada Correctamente'
            data['Mesas'] = mesas.listado_mesa()
        else:
            data['mensaje'] = 'No se ha podido eliminar la mesa'
        return render(request, 'Mesas.html', data)
 
    elif 'Modificar' in request.POST:
        numeromesa = int(request.POST.get('idmesa'))
        cantidadpersonas=int(request.POST.get('capacidad'))
        estadomesa=int(request.POST.get('estado'))
        mesa_m=mesas(numeromesa,cantidadpersonas,estadomesa)
        salida=mesa_m.modificar_mesa(numeromesa,cantidadpersonas,estadomesa)
        if salida == 1:
            data['mensaje'] = 'Mesa Modificada Correctamente'
            data['Mesas'] = mesas.listado_mesa()
        else:
            data['mensaje'] = 'No se ha podido modificar la mesa'
        return render(request, 'Mesas.html', data)
    return render(request, 'Mesas.html', data)

def mesas_totem(request):
    data ={
        'Mesas' : mesas.listado_mesa(),
        'message':"",
    }
    if 'Reservar' in request.POST:
        
        estado_mesa=int(request.POST.get('estado'))
        num_mesa=int(request.POST.get('numMesa'))
        if estado_mesa==1:
            mesas.modificar_estado_mesa(num_mesa,4)
            data['Mesas']=mesas.listado_mesa()
            return render (request,'./MesasDisponibles.html',data)
        else:
            data['message']="No puedes reservar una mesa que esta en este estado!"
            return render (request,'./MesasDisponibles.html',data)
    return render (request,'./MesasDisponibles.html',data)

def mesas_modificar(request,num_mesa,capacidad,estado):
    data={
        'num_mesaM':num_mesa,
        'capacidadM':capacidad,
        'estadoM': int(estado),
        'lista_estado':mesas.listar_estados(),
        
    }
    return render (request,'./Mesas-modificar.html',data)

def Home_totem(request ):
    if 'reserva' in request.POST:
        data={
            'rut' : request.POST.get('rut'),
            'Mesas' : mesas.listado_mesa(),
            'message':"",
        }
        return render (request,'./MesasDisponibles.html',data)
    return render (request,'./Home_totem.html')