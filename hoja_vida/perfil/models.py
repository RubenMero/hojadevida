from django.db import models

class DatosPersonales(models.Model):
    idperfil = models.IntegerField(primary_key=True)
    descripcionperfil = models.CharField(max_length=50)
    perfilactivo = models.IntegerField()

    apellidos = models.CharField(max_length=60)
    nombres = models.CharField(max_length=60)
    nacionalidad = models.CharField(max_length=20)
    lugarnacimiento = models.CharField(max_length=60)
    fechanacimiento = models.DateField()
    numerocedula = models.CharField(max_length=10, unique=True)
    sexo = models.CharField(max_length=1)
    estadocivil = models.CharField(max_length=50)
    licenciaconducir = models.CharField(max_length=6)

    telefonoconvencional = models.CharField(max_length=15)
    telefonofijo = models.CharField(max_length=15)

    direcciontrabajo = models.CharField(max_length=50)
    direcciondomiciliaria = models.CharField(max_length=50)

    sitioweb = models.CharField(max_length=60)

    class Meta:
        db_table = "DATOSPERSONALES"
