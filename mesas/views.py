from django.shortcuts import render
from django.db import connection
# Create your views here.
from django.contrib.auth.decorators import login_required
import cx_Oracle


@login_required
def Mesas(request):
    data ={
        'lista_estado':listar_estados(),
        'mensaje': ""
        
    }
    try:
        if request.method == 'POST':
            #numeromesa = request.POST.get('id_mesa')
            #cantidadpersonas=request.POST.get('capacidad')
            #estadomesa=request.POST.get('estado')
            salida = agregar_mesa(2,1,1)
            if salida=="1":
                data['mensaje'] = 'Mesa agregada correctamente'
            else:
                data['mensaje'] = f'el mensaje de error es: {salida}'
    except Exception as e:
        data['mensaje']= e.__str__()

    return render(request,'Mesas.html',data)

def listar_estados():

    django_cursor = connection.cursor()

    cursor = django_cursor.connection.cursor()

    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_R_ESTADO_MESA",[out_cur])
    
    lista=[]

    for fila in out_cur:
        lista.append(fila)
    return lista

def agregar_mesa(numeromesa,cantidadpersonas,estadomesa):
    try:
        django_cursor = connection.cursor()
        cursor = django_cursor.connection.cursor()
        salida= cursor.var(cx_Oracle.STRING)
        cursor.callproc ('SP_CREATE_MESAS',[numeromesa,cantidadpersonas,estadomesa,salida])
        return salida
    except Exception as e:
        return e.__str__()



#lo del video
def mesas(request):
    return render(request, 'mesas/Mesas.html')
