from django.shortcuts import render
from django.db import connection
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def Mesas(request):
    data ={
        'lista_estado':listar_estados(),
        'mensaje': ""
        
    }
    if request.method == 'POST':
        numeromesa = request.POST.get('id_mesa')
        cantidadpersonas=request.POST.get('capacidad')
        estadomesa=request.POST.get('estado')
        salida = agregar_mesa(numeromesa,cantidadpersonas, estadomesa)
        if salida==1:
            data['mensaje'] = 'mesa agregada correctamente'
        else:
            data['mensaje'] = 'mesa no se pudo agregar'

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
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida= 0;
    cursor.callproc ('SP_CREATE_MESAS',[numeromesa,cantidadpersonas,estadomesa,salida])
    return salida



#lo del video
def mesas(request):
    return render(request, 'mesas/Mesas.html')
