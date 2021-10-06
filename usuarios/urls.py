from django.urls import path
from .views import home, RegistroUsuario,log,logout_def
from Administrador import views

urlpatterns = [
    path('', home,name='home'),
    #path('registro/', registro,name='registro'),
    path('registro/',RegistroUsuario,name="registro"),
    path('Administrador/',views.Mesas,name="mesas"),
    path('login/',log,name='login'),
    path('logout/',logout_def,name='logout'),


]