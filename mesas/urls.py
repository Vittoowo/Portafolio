from django.urls import path
from .views import *

urlpatterns = [
    path('',Mesas,name='Mesas'),
]