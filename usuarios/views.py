from django.shortcuts import render, redirect,render
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario

#Vista que retorna Home
def home(request):
    return render(request,'usuarios/home.html')


@login_required
def inicioAdmin(request):
    return render(request,'usuarios/inicio-admin.html')
#@login_required
def inicioCocina(request):
    return render(request,'usuarios/inicio-cocina.html')
#Preguntar si tiene mucho sentido que esto se cambie a un models o no.
#Vista del Login
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
                return redirect (to='inicio-admin')
            if user.groups.filter(name='Cocina').exists():
                return redirect (to='inicio-cocina')
            if user.groups.filter(name='Totem').exists():
                return redirect (to='mesas_totem')
            if user.groups.filter(name='Bodega').exists():
                return redirect (to='bodega')
            else:
                return redirect (to='home')
    return render(request,'registration/login.html',data) 

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

#Metodo que devuelve la lista de los grupos
