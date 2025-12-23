from django.shortcuts import render
from .models import *

def hoja_vida(request, idperfil):
    perfil = DatosPersonales.objects.get(idperfil=idperfil)

    context = {
        'perfil': perfil,
        'experiencias': ExperienciaLaboral.objects.filter(perfil=perfil, activarparaqueseveaenfront=True),
        'reconocimientos': Reconocimiento.objects.filter(perfil=perfil, activarparaqueseveaenfront=True),
        'cursos': CursoRealizado.objects.filter(perfil=perfil, activarparaqueseveaenfront=True),
        'productos_academicos': ProductoAcademico.objects.filter(perfil=perfil, activarparaqueseveaenfront=True),
        'productos_laborales': ProductoLaboral.objects.filter(perfil=perfil, activarparaqueseveaenfront=True),
        'ventas': VentaGarage.objects.filter(perfil=perfil, activarparaqueseveaenfront=True),
    }

    return render(request, 'cv.html', context)
