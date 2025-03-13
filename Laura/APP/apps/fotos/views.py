from django.shortcuts import render
from .models import Mifoto

# Create your views here.
def inicio(request):
    mis_fotos = Mifoto.objects.all()
    return render(request,"pages/inicio.html",{})

