from django.shortcuts import render
from django.db import connection
from django.contrib.auth.decorators import login_required
import cx_Oracle
from mesas.models import Mesas as mesas

@login_required
def Mesas(request):
    data ={
        'lista_estado':listar_estados(),
        'mensaje': "",
        'Mesas' : mesas.listado_mesa(),
    }
      
    if 'Guardar' in request.POST:
        
        numeromesa = int(request.POST.get('idmesa'))
        cantidadpersonas=int(request.POST.get('capacidad'))
        estadomesa=int(request.POST.get('estado'))
        
        salida = agregar_mesa(numeromesa,cantidadpersonas,estadomesa)
        print 
        if salida==1:
            print 
            data['mensaje'] = 'Mesa agregada correctamente'
            data['Mesas'] = mesas.listado_mesa()
        else:
            data['mensaje'] = f'No se pudo agregar la mesa :('
        return render(request, 'Mesas.html', data)


    elif 'Eliminar' in request.POST:
        numeromesa= int (request.POST.get('idmesa'))
        salida = eliminar_mesa(numeromesa)
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
        salida= modificar_mesa(numeromesa,cantidadpersonas,estadomesa)
        if salida == 1:
            data['mensaje'] = 'Mesa Modificada Correctamente'
            data['Mesas'] = mesas.listado_mesa()
        else:
            data['mensaje'] = 'No se ha podido modificar la mesa'
        return render(request, 'Mesas.html', data)
    return render(request, 'Mesas.html', data)

def listar_estados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_R_ESTADO_MESA",[out_cur])
    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista

#VARIABLES DEL CRUD

#agregar-create-añadir-crear del Crud
def agregar_mesa(numeromesa,cantidadpersonas,estadomesa):
    try:
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida= cursor.var(cx_Oracle.NUMBER)
        cursor.callproc ('SP_CREATE_MESAS',[numeromesa,cantidadpersonas,estadomesa,salida])
        return salida.getvalue()
    except Exception as e:
        raise e.__str__()


#ELIMINAR 
def eliminar_mesa(numeromesa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_DELETE_MESAS',[numeromesa, salida])
    return salida.getvalue()

#EL MODIFICAR 
def modificar_mesa(numeromesa,cantidadpersonas,estadomesa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_UPDATE_MESAS',[numeromesa,cantidadpersonas,estadomesa,salida])
    return salida.getvalue()