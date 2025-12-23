from django.contrib import admin
from .models import (
    DatosPersonales,
    ExperienciaLaboral,
    CursoRealizado,
    Reconocimiento,
    ProductoAcademico,
    ProductoLaboral,
    VentaGarage
)

admin.site.register(DatosPersonales)
admin.site.register(ExperienciaLaboral)
admin.site.register(CursoRealizado)
admin.site.register(Reconocimiento)
admin.site.register(ProductoAcademico)
admin.site.register(ProductoLaboral)
admin.site.register(VentaGarage)