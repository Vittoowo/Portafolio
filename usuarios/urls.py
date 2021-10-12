from django.urls import path
from .views import home, RegistroUsuario,log,logout_def
from mesas import views as mv
from reservas import views as rv

urlpatterns = [
    path('', home,name='home'),
    path('registro/',RegistroUsuario,name="registro"),
    path('Administrador/Mesas',mv.Mesas,name="mesas"),
    path('login/',log,name='login'),
    path('logout/',logout_def,name='logout'),
    path('Administrador/Reservas',rv.Reservas,name="reservas"),
    #Agregar Reservas
    #Agregar Mesas


]