from django.shortcuts import render
from .models import DatosPersonales

def inicio(request):
    datos = DatosPersonales.objects.first()
    return render(request, "perfil/datos_personales.html", {
        "datos": datos
    })
