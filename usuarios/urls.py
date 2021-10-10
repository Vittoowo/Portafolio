from django.urls import path
from .views import home, RegistroUsuario,log,logout_def
from Administrador import views as av
from mesas import views as mv
from reservas import views as rv

urlpatterns = [
    path('', home,name='home'),
    path('registro/',RegistroUsuario,name="registro"),
    path('Administrador/',av.Mesas,name="mesas"),
    path('login/',log,name='login'),
    path('logout/',logout_def,name='logout'),
    #Agregar Reservas
    #Agregar Mesas


]