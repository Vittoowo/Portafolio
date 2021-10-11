from django.urls import path
from .views import *


urlpatterns = [
    path('/reservas',Reservas,name='reservas'),
]