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


# --- TABLA EXPERIENCIA LABORAL ---
class ExperienciaLaboral(models.Model):
    idexperiencialaboral = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, db_column='idperfilconqueestaactivo')
    
    cargodesempenado = models.CharField(max_length=100)
    nombreempresa = models.CharField(max_length=50)
    lugarempresa = models.CharField(max_length=50)
    emailempresa = models.CharField(max_length=100)
    sitiowebempresa = models.CharField(max_length=100)
    nombrecontactoempresarial = models.CharField(max_length=100)
    telefonocontactoempresarial = models.CharField(max_length=60)
    fechainiciogestion = models.DateField()
    fechafingestion = models.DateField()
    descripcionfunciones = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True) # Tu campo bit
    rutacertificado = models.CharField(max_length=100)

    class Meta:
        db_table = "EXPERIENCIALABORAL"


# --- TABLA RECONOCIMIENTOS ---
class Reconocimientos(models.Model):
    TIPO_CHOICES = [
        ('Academico', 'Académico'),
        ('Laboral', 'Laboral'),
        ('Institucional', 'Institucional'),
    ]

    idreconocimiento = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, db_column='idperfilconqueestaactivo')
    
    tiporeconocimiento = models.CharField(max_length=100, choices=TIPO_CHOICES)
    fechareconocimiento = models.DateField()
    descripcionreconocimiento = models.CharField(max_length=100)
    entidadpatrocinadora = models.CharField(max_length=100)
    nombrecontactoauspicia = models.CharField(max_length=100)
    telefonocontactoauspicia = models.CharField(max_length=60)
    activarparaqueseveaenfront = models.BooleanField(default=True)
    rutacertificado = models.CharField(max_length=100)

    class Meta:
        db_table = "RECONOCIMIENTOS"


# --- TABLA CURSOS REALIZADOS ---
class CursosRealizados(models.Model):
    idcursorealizado = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, db_column='idperfilconqueestaactivo')
    nombrerecurso = models.CharField(max_length=100)
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
        db_table = "CURSOSREALIZADOS"

# --- TABLA PRODUCTOS ACADÉMICOS ---
class ProductosAcademicos(models.Model):
    idproductoacademico = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, db_column='idperfilconqueestaactivo')
    nombrerecurso = models.CharField(max_length=100)
    clasificador = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = "PRODUCTOSACADEMICOS"

# --- TABLA PRODUCTOS LABORALES ---
class ProductosLaborales(models.Model):
    idproductoslaborales = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, db_column='idperfilconqueestaactivo')
    nombreproducto = models.CharField(max_length=100)
    fechaproducto = models.DateField()
    descripcion = models.CharField(max_length=100)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = "PRODUCTOSLABORALES"

# --- TABLA VENTA GARAGE ---
class VentaGarage(models.Model):
    idventagarage = models.IntegerField(primary_key=True)
    idperfilconqueestaactivo = models.ForeignKey(DatosPersonales, on_delete=models.CASCADE, db_column='idperfilconqueestaactivo')
    nombreproducto = models.CharField(max_length=100)
    estadoproducto = models.CharField(max_length=40) # chk: Bueno, Regular
    descripcion = models.CharField(max_length=100)
    valordelbien = models.DecimalField(max_digits=5, decimal_places=2)
    activarparaqueseveaenfront = models.BooleanField(default=True)

    class Meta:
        db_table = "VENTAGARAGE"
