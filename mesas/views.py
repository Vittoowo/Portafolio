from django.shortcuts import render
from django.db import connection
# Create your views here.
from django.contrib.auth.decorators import login_required
import cx_Oracle

"""
def Mesas(request):
    data ={
        'lista_estado':listar_estados(),
        'mensaje': "",
    }
    return render(request,'Mesas.html',data)

      
try:
        if request.method == 'POST':
            numeromesa = int(request.POST.get('idmesa'))
            cantidadpersonas=int(request.POST.get('capacidad'))
            estadomesa=int(request.POST.get('estado'))
            salida = agregar_mesa(numeromesa,cantidadpersonas,estadomesa)
            if salida==1:
                data['mensaje'] = 'Mesa agregada correctamente'
            else:
                data['mensaje'] = f'No se pudo agregar la mesa :('
    except Exception as e:
        data['mensaje']= f'Error al agregar mesa: {e.__str__()}'
"""
@login_required
def Mesas(request):
    data ={
        'lista_estado':listar_estados(),
        'mensaje': "",
        'Mesas' :listado_mesa(),
    }
    print ('estoy en la linea 36')    
    if 'Guardar' in request.POST:
        print ('estoy en la linea 38') 
        numeromesa = int(request.POST.get('idmesa'))
        cantidadpersonas=int(request.POST.get('capacidad'))
        estadomesa=int(request.POST.get('estado'))
        print ('estoy en la linea 42') 
        salida = agregar_mesa(numeromesa,cantidadpersonas,estadomesa)
        print ('estoy en la linea 44') 
        if salida==1:
            print ('estoy en la linea 45') 
            data['mensaje'] = 'Mesa agregada correctamente'
            data['Mesas'] = listado_mesa()
        else:
            data['mensaje'] = f'No se pudo agregar la mesa :('
        return render(request, 'Mesas.html', data)


    elif 'Eliminar' in request.POST:
        numeromesa= int (request.POST.get('idmesa'))
        salida = eliminar_mesa(numeromesa)
        if salida == 1:
            data['mensaje'] = 'Mesa Eliminada Correctamente'
            data['Mesas'] = listado_mesa()
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
            data['Mesas'] = listado_mesa()
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

#VARIABLES DEL CRUDCITO

#agregar-create-a;adir-crear del Crud
def agregar_mesa(numeromesa,cantidadpersonas,estadomesa):
    try:
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida= cursor.var(cx_Oracle.NUMBER)
        cursor.callproc ('SP_CREATE_MESAS',[numeromesa,cantidadpersonas,estadomesa,salida])
        return salida.getvalue()
    except Exception as e:
        raise e.__str__()

#listado-leer-mostrar-read del cRud
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

#ELIMINAR MESITAS UVU
def eliminar_mesa(numeromesa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_DELETE_MESAS',[numeromesa, salida])
    return salida.getvalue()

#EL MODIFICAR PULENTO
def modificar_mesa(numeromesa,cantidadpersonas,estadomesa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_UPDATE_MESAS',[numeromesa,cantidadpersonas,estadomesa,salida])
    return salida.getvalue()