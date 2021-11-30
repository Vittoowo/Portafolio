from django.urls import path, include
from .views import *
from mesas import views as mv
from reservas import views as rv

urlpatterns = [
    #path('', home,name='home'),
    path('registro/',RegistroUsuario,name="registro"),
    path('',login_user,name='login'),
    path('logout/',logout_def,name='logout'),
    path('mesas/', include('mesas.urls')),
    path('reservas/',include('reservas.urls')),
    path('bodega/',include('bodega.urls')),
    path('Administrador/home',inicioAdmin,name="Administrador"),
    path('Cocina/home',inicioCocina,name="Cocina"),
    path('Bodega/home',inicioBodega,name="Bodega"),
    path('Cocina/',include('cocina.urls')),
    path('Totem/home',Home_totem, name='Home_totem'),
    #path('Administrador/Mesas',mv.Mesas,name="mesas"),#modificar con include
    #path('Administrador/Reservas',rv.Reservas,name="reservas"), #modificar con include
    
    ##Agregar Reservas
    #Agregar Mesas
]