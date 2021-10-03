from django.shortcuts import render
from django.db import connection
# Create your views here.

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

#aqui voy a hacer el registro by:Yesni