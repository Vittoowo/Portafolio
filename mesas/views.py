from django.shortcuts import render
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
        mesa_c=mesas(numeromesa,cantidadpersonas,estadomesa) #creando el objeto
        salida = mesa_c.agregar_mesa()#llamamos al metodo del models, creamos una variable y le asigna el valor que va a retornar
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
    #aqui la logica pues
    return render (request,'./MesasDisponibles.html')
