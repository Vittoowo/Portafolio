from django.urls import path, include
from .views import *

urlpatterns = [
    path('',Mesas,name='Mesas'),
    path('', include('mesas.urls'))
]