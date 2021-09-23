from django.urls import path
from .views import home, RegistroUsuario
from Administrador import views

urlpatterns = [
    path('', home,name='home'),
    #path('registro/', registro,name='registro'),
    path('registro/',RegistroUsuario,name="registro"),
    path('Administrador/',views.Mesas,name="mesas"),


]