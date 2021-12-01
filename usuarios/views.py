from django.shortcuts import render, redirect,render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario
from mesas.models import Mesas as mesas

#Vista que retorna Home
def home(request):
    return render(request,'usuarios/home.html')


@login_required
def inicioAdmin(request):
    if request.user.groups.filter(name='Administrador').exists():
        print(request.user.groups.get(),"=",len("Administrador"))
        return render(request,'usuarios/inicio-admin.html')
    else:
        data = {'message':'Usted no tiene permisos para ingresar a este apartado'}
        logout(request)
        return redirect('login')
    

#@login_required
def inicioCocina(request):
    return render(request,'usuarios/inicio-cocina.html')

@login_required
def inicioBodega(request):
    return render(request,'usuarios/inicio-bodega.html')

def login_user(request):
    #Si se hace una solicitud de tipo POST
    data ={
        'message':''
    }    
    if request.method =='POST':
        #Obtiene los datos mandados por el formulario en POST
        usr=request.POST.get("username")
        pwd=request.POST.get("password1")
        #Autentica el usuario y nos devuelve el usuario
        user = authenticate(username=usr, password=pwd)
        if user is None:
            data['message']='Usuario y/o contraseña incorrecta'
            return render(request,'registration/login.html',data)
        else:
            #Iniciamos sesion con el usuario
            login(request,user)
            #Obtenemos su grupo y segun esto, le redireccionamos a otra pagina
            if user.groups.filter(name='Administrador').exists():
                
                return redirect (to='Administrador')
            elif user.groups.filter(name='Cocina').exists():
                return redirect (to='Cocina')
            elif user.groups.filter(name='Totem').exists():
                return redirect (to='Home_totem')
            elif user.groups.filter(name='Bodega').exists():
                return redirect (to='Bodega')
            elif user.groups.filter(name='Recepcion').exists():
                return redirect (to='reservas')
            else:
                return redirect (to='home')
    return render(request,'registration/login.html',data) 

#Vista del logout
#Lo que hace simplemente es terminar la sesion y redirigir al home
def logout_def(request):
    logout(request)
    return redirect (to='login')

@login_required
def RegistroUsuario(request):
    if request.user.groups.filter(name='Administrador').exists():
        data={
           'grupos':Usuario.lista_grupos(),
           'message':""
        }
        if request.method =='POST':
            #formulario= CustomUserForm(request.POST)
            try:
                #Obtenemos usuario,contraseña, email y el  id del grupo
                username=request.POST.get("username")
                password=request.POST.get("password1")
                email=request.POST.get("email")
                 #Traemos el grupo que seleccionaron
                id_grupo=int(request.POST.get('groups'))
                first_name = request.POST.get('first_name')
                last_name=request.POST.get('last_name')
                print(last_name)
                #Pasamos los datos a la clase Usuario(creada por nosotros)
                user = Usuario(username,password,email,id_grupo,first_name,last_name)
                #Utilizamos el metodo crear usuario(creado por nosotros)
                user.create_user()
                #Lo redirigimos al login
                data['message']='Usuario creado exitosamente'    
                return redirect (to='home')   
            except Exception as e:
                data['message']=e.__str__
                return render(request,'registration/registro.html',data)
        return render(request,'registration/registro.html',data)
    else:
        data = {'message':'Usted no tiene permisos para ingresar a este apartado'}
        logout(request)
        return redirect('login')     


def Home_totem(request ):
    if 'vermesasdisponibles' in request.POST:
        
        return redirect(to='mesas_totem',rut=request.POST.get('RutReserva'), dvRut= request.POST.get('DVRUTReserva'))
        #return render (request,'./MesasDisponibles.html',data)
    return render (request,'usuarios/Home_totem.html')