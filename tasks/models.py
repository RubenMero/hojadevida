from django.db import models

# DATOS PERSONALES (Tabla principal):
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
        db_table = 'datospersonales'

# EXPERIENCIA LABORAL:
class ExperienciaLaboral(models.Model):
    idexperiencilaboral = models.IntegerField(primary_key=True)
    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )
    cargodesempenado = models.CharField(max_length=100)
    nombrempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)
    emailempresa = models.CharField(max_length=100)
    sitiowebempresa = models.CharField(max_length=100)
    nombrecontactoempresarial = models.CharField(max_length=100)
    telefonocontactoempresarial = models.CharField(max_length=60)
    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField()
    descripcionfunciones = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    class Meta:
        db_table = 'experiencialaboral'

# RECONOCIMIENTOS (Base de datos documento):
class Reconocimiento(models.Model):
    idreconocimiento = models.IntegerField(primary_key=True)
    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )
    tiporeconocimiento = models.CharField(max_length=100)
    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    class Meta:
        db_table = 'reconocimientos'

# CURSOS REALIZADOS (Base de datos documento):
class CursoRealizado(models.Model):
    idcursorealizado = models.IntegerField(primary_key=True)
    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )
    nombrecurso = models.CharField(max_length=100)
    fechainicio = models.DateField()
    fechafin = models.DateField()
    totalhoras = models.IntegerField()
    descripcioncurso = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)
    emailempresapatrocinadora = models.CharField(max_length=60)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    class Meta:
        db_table = 'cursosrealizados'

# PRODUCTOS ACADEMICOS
class ProductoAcademico(models.Model):
    idproductoacademico = models.IntegerField(primary_key=True)
    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )
    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = 'productosacademicos'

# PRODUCTOS LABORALES
class ProductoLaboral(models.Model):
    idproductoslaborales = models.IntegerField(primary_key=True)
    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )
    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField()
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = 'productoslaborales'

# VENTA GARAGE
class VentaGarage(models.Model):
    idventagarage = models.IntegerField(primary_key=True)
    perfil = models.ForeignKey(
        DatosPersonales,
        on_delete=models.CASCADE,
        db_column='idperfilconqueestaactivo'
    )
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40)
    descripcion = models.CharField(max_length=100)
    valordelbien = models.DecimalField(max_digits=5, decimal_places=2)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = 'ventagarage'
