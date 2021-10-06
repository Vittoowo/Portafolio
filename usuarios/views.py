from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User
from django.shortcuts import render
from django.db import connection
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate


#Vista que retorna Home
def home(request):
    return render(request,'usuarios/home.html')

#Vista del Home
def log(request):
    #Si se hace una solicitud de tipo POST    
    if request.method =='POST':
        #Obtiene los datos mandados por el formulario en POST
        usr=request.POST.get("username")
        pwd=request.POST.get("password1")
        #Autentica el usuario y nos devuelve el usuario
        user = authenticate(username=usr, password=pwd)
        if user is None:
            print("no hay usuario")
        else:
            #Iniciamos sesion con el usuario
            login(request,user)
            #Obtenemos su grupo y segun esto, le redireccionamos a otra pagina
            if user.groups.filter(name='Administrador').exists():
                return redirect (to='mesas')
            else:
                return redirect (to='home')
    return render(request,'registration/login.html') 

#Vista del logout
#Lo que hace simplemente es terminar la sesion y redirigir al home
def logout_def(request):
    logout(request)
    return redirect (to='home')

#Vista del Registro del Usuario
def RegistroUsuario(request):
    #Este es un diccionario que se le pasará por parametro y se le incrustan
    #datos que metamos, en este caso, incrustamos una lista de tuplas y un mensaje
    data={
       'grupos':listar_grupos(),
       'message':""
    }
    if request.method =='POST':
        #formulario= CustomUserForm(request.POST)
        try:
            #Obtenemos usuario,contraseña, email y el  id del grupo
            username=request.POST.get("username")
            password=request.POST.get("password1")
            email=request.POST.get("email")
            id_grupo=int(request.POST.get('groups'))
            #Creamos el usuario
            user = User.objects.create_user(username,email,password)
            #Traemos el grupo que seleccionaron
            group=Group.objects.get(id=id_grupo)
            #Agregamos al usuario a un grupo
            user.groups.add(group)
            #Lo redirigimos al login
            return redirect(to='login')
            
        except Exception as e:
            data['message']=e.__str__()   
    return render(request,'registration/registro.html',data)
#Metodo que devuelve la lista de los grupos
def listar_grupos():
    #Creamos una lista vacia que devolveremos
    lista=[]
    #Obtenemos la cantidad total de grupos
    size= Group.objects.count()
    #Iteramos segun la cantidad de grupos y añadimos uno por uno los grupos
    for g in range (size):
        lista.append(Group.objects.values_list()[g])
    #Finalmente retornamos la lista
    return lista