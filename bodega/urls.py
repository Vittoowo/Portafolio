from django.urls import path
from .views import *


urlpatterns = [
    path('bodega',Bodega,name='bodega')
]