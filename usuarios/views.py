from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User,GroupManager
from usuarios.forms import CustomUserForm
from django.shortcuts import render
from django.db import connection


# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def RegistroUsuario(request):
    data={
       'grupos':listar_grupos()
    }
    if request.method =='POST':
        #formulario= CustomUserForm(request.POST)
        user = User.objects.create_user("usuario3","portafolio","usuario3@vfarias.cl")
        #if formulario.is_valid():
        print(request.POST.get("username"))
        print(request.POST.get("groups"))
        #formulario.save()
        return redirect (to='home')
        
        #else:
        #    print("error")    
    return render(request,'registration/registro.html',data)

def listar_grupos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()
    cursor.callproc("SP_R_GRUPOS",[out_cur])
    lista=[]
    for fila in out_cur:
        lista.append(fila)
    return lista

"""class RegistroUsuario(CreateView):
    model = User
    template_name= "registration/registro.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mesas')
"""