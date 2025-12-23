from django.shortcuts import render, get_object_or_404
from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    CursoRealizado,
    Reconocimiento,
    ProductoAcademico,
    ProductoLaboral,
    VentaGarage
)

def cv_view(request, idperfil):
    perfil = get_object_or_404(DatosPersonales, idperfil=idperfil)

    experiencia = ExperienciaLaboral.objects.filter(
        idperfilconqueestaactivo=idperfil,
        activarparaqueseveaenfront=1
    ).order_by('-fechainiciogestion')

    cursos = CursoRealizado.objects.filter(
        idperfilconqueestaactivo=idperfil,
        activarparaqueseveaenfront=1
    )

    reconocimientos = Reconocimiento.objects.filter(
        idperfilconqueestaactivo=idperfil,
        activarparaqueseveaenfront=1
    )

    productos_academicos = ProductoAcademico.objects.filter(
        idperfilconqueestaactivo=idperfil,
        activarparaqueseveaenfront=1
    )

    productos_laborales = ProductoLaboral.objects.filter(
        idperfilconqueestaactivo=idperfil,
        activarparaqueseveaenfront=1
    )

    venta_garage = VentaGarage.objects.filter(
        idperfilconqueestaactivo=idperfil,
        activarparaqueseveaenfront=1
    )

    context = {
        'perfil': perfil,
        'experiencia': experiencia,
        'cursos': cursos,
        'reconocimientos': reconocimientos,
        'productos_academicos': productos_academicos,
        'productos_laborales': productos_laborales,
        'venta_garage': venta_garage,
    }

    return render(request, 'hoja_vida/cv.html', context)
