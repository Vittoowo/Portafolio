from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.db import connection
from django.contrib.auth import login
from django.contrib.auth import authenticate

# Create your views here.

def home(request):
    return render(request,'usuarios/home.html')

def log(request):

    
    if request.method =='POST':

        us=request.POST.get("username")
        pas=request.POST.get("password1")
        user = authenticate(username=us, password=pas)
        if user is None:
            print("no hay usuario")
        else:
           print("si hay usuario")
    return render(request,'registration/login.html') 

def RegistroUsuario(request):
    data={
       'grupos':listar_grupos(),
       'message':""
    }
    if request.method =='POST':
        #formulario= CustomUserForm(request.POST)
        try:
            
            username=request.POST.get("username")
            password=request.POST.get("password1")
            print(password)
            email=request.POST.get("email")
            id_grupo=int(request.POST.get('groups'))
            #print(f'{username}, {password} , {email} , {id_grupo}')
            #v1= listar_grupos()
            #v1 = [i[0].__str__()+'-'+i[1].__str__() for i in v1]
            #v2=str.join(';', v1)
            #data['message']=v2
            user = User.objects.create_user(username,email,password)
            group=Group.objects.get(id=id_grupo)
            user.groups.add(group)
            login(request,user)
            if user.groups.filter(name='Administrador').exists():
                return redirect (to='mesas')
            else:
                return redirect (to='home')
        except Exception as e:
            data['message']=e.__str__()

        #if formulario.is_valid():
        #print(request.POST.get("groups"))
        #formulario.save()
        #return redirect (to='home')
        
        #else:
        #    print("error")    
    return render(request,'registration/registro.html',data)

def listar_grupos():

    lista=[]
    #group = Group.objects.values_list()[0][1]
    size= Group.objects.count()
    for g in range (size):
        lista.append(Group.objects.values_list()[g])
    return lista
    #for g in range (size):
    #    dic[g]=Group.objects.values_list()[g][1]
    #return dic
    #django_cursor = connection.cursor()
    #cursor = django_cursor.connection.cursor()
    #out_cur = django_cursor.connection.cursor()
    #cursor.callproc("SP_R_GRUPOS",[out_cur])
    #lista=[]
    #for fila in out_cur:
    #    lista.append(fila)
    #return lista

"""class RegistroUsuario(CreateView):
    model = User
    template_name= "registration/registro.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('mesas')
"""