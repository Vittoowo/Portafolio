from django.urls import path, include
from .views import home, RegistroUsuario, inicioAdmin,login_user,logout_def
from mesas import views as mv
from reservas import views as rv

urlpatterns = [
    path('', home,name='home'),
    path('registro/',RegistroUsuario,name="registro"),
    path('login/',login_user,name='login'),
    path('logout/',logout_def,name='logout'),
    path('mesas/', include('mesas.urls')),
    path('/',include('reservas.urls')),
    path('Administrador/home',inicioAdmin,name="inicio-admin"),
    
    #path('Administrador/Mesas',mv.Mesas,name="mesas"),#modificar con include
    #path('Administrador/Reservas',rv.Reservas,name="reservas"), #modificar con include
    
    ##Agregar Reservas
    #Agregar Mesas
]