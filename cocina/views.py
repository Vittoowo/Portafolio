from django.shortcuts import render

# Create your views here.
def gestionPlatos(request):
    return render(request,'gestion-platos.html')