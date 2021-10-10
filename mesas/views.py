from django.shortcuts import render
from django.db import connection
# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def Mesas(request):
    data ={
        'estado':listar_estados()
    }
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

"""
def CreateMesas(request):

    django_cursor = connection.cursor()

    cursor = django_cursor.connection.cursor()

    out_cur = 0;

    cursor.callproc("SP_CREATE_MESAS",[request. ,2,1,    out_cur])

    if out_cur == 1:
        return render(request, 'mesas/Mesas.html')
    else:
        return render(request,'Mesas.html')


"""


#lo del video
def mesas(request):
    return render(request, 'mesas/Mesas.html')
