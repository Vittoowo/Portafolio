from django.urls import path
from .views import home, RegistroUsuario, inicioAdmin,log,logout_def
from mesas import views as mv
from reservas import views as rv

urlpatterns = [
    path('', home,name='home'),
    path('registro/',RegistroUsuario,name="registro"),
    path('Administrador/Mesas',mv.Mesas,name="mesas"),#modificar con include
    path('login/',log,name='login'),
    path('logout/',logout_def,name='logout'),
    path('Administrador/Reservas',rv.Reservas,name="reservas"), #modificar con include
    path('Administrador/home',inicioAdmin,name="inicio-admin"),
    #Agregar Reservas
    #Agregar Mesas


]