from django.shortcuts import render
from .models import *

def inicio(request):
    datos = DatosPersonales.objects.first()
    
    if not datos:
        return render(request, "perfil/datos_personales.html", {"error": "No hay datos en la base"})

    contexto = {
        "datos": datos,
        
        "experiencias": ExperienciaLaboral.objects.filter(
            idperfilconqueestaactivo=datos, activarparaqueseveaenfront=True
        ),
        
        "reconocimientos": Reconocimientos.objects.filter(
            idperfilconqueestaactivo=datos, activarparaqueseveaenfront=True
        ),
        
        "cursos": CursosRealizados.objects.filter(
            idperfilconqueestaactivo=datos, activarparaqueseveaenfront=True
        ),
        
        "prod_academicos": ProductosAcademicos.objects.filter(
            idperfilconqueestaactivo=datos, activarparaqueseveaenfront=True
        ),
        
        "prod_laborales": ProductosLaborales.objects.filter(
            idperfilconqueestaactivo=datos, activarparaqueseveaenfront=True
        ),
        
        "ventas": VentaGarage.objects.filter(
            idperfilconqueestaactivo=datos, activarparaqueseveaenfront=True
        ),
        
        "todos_los_reconocimientos": Reconocimientos.objects.filter(idperfilconqueestaactivo=datos),
    }
    
    return render(request, "perfil/datos_personales.html", contexto)

def cambiar_estado_reconocimiento(request, id):
    reconocimiento = get_object_or_404(Reconocimientos, idreconocimiento=id)
    reconocimiento.activarparaqueseveaenfront = not reconocimiento.activarparaqueseveaenfront
    reconocimiento.save()
    return redirect('inicio')