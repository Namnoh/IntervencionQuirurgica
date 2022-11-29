from django.db import models
import datetime, django
from django.contrib.auth.models import User

# Create your models here.

class Usuario (models.Model):

    userRut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut Usuario')
    userNombres = models.CharField(max_length=100, verbose_name='Nombres Usuario')
    userApellidos = models.CharField(max_length=100, verbose_name='Apellidos Usuario')
    userCorreo = models.CharField(max_length=50, verbose_name='Correo Usuario')
    userPassword = models.CharField(max_length=50, verbose_name='Contraseña Usuario')
    user = models.OneToOneField(User, on_delete=models.CASCADE, default="")

    def __str__(self):
        return f'{self.userRut} | {self.userNombres}'

class Cirugia (models.Model):

    cirugiaId = models.BigAutoField(primary_key=True, verbose_name='Id Cirugía')
    cirugiaNombre = models.CharField(max_length=100, verbose_name='Nombre Cirugia')

    class Meta:
        ordering=['cirugiaNombre']

    def __str__(self):
        return f'{self.cirugiaId} - {self.cirugiaNombre}'

class Paciente (models.Model):

    paRut = models.CharField(primary_key=True, max_length=10, verbose_name='Rut Paciente')
    paNombres = models.CharField(max_length=100, verbose_name='Nombres Paciente')
    paApellidos = models.CharField(max_length=100 ,verbose_name='Apellidos Paciente')
    paCorreoEmerg = models.CharField(max_length=50, verbose_name='Correo Emergencia Paciente')
    paCirugia = models.ForeignKey(Cirugia, on_delete=models.CASCADE)
    paAlergias = models.CharField(max_length=100, blank=True, default="", verbose_name='Alergias Paciente')
    paCirugiasAnteriores = models.CharField(max_length=250, blank=True, default="", verbose_name='Cirugia Anteriores Paciente')

    def __str__(self):
        return f'{self.paRut} | {self.paNombres}'

class RegRecepcion (models.Model):

    regRecepId = models.BigAutoField(primary_key=True, verbose_name='Id  Registro de Recepción')
    regRecepFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Registro de Recepción')
    regRecepPac = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.regRecepId}'

class InfIntervencion (models.Model):

    interId = models.BigAutoField(primary_key=True, verbose_name='Id  Intervención')
    interFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Intervención')
    interNombre = models.ForeignKey(Cirugia, on_delete=models.CASCADE)
    interAnestesia = models.CharField(max_length=50, verbose_name='Anestesia Intervención')
    interApoyo = models.CharField(max_length=50, blank=True, default="", verbose_name='Apoyo Intervención')
    interCantApoyo = models.IntegerField(blank=True, default=0, verbose_name='Cantidad de Apoyo Intervención')
    interObs = models.CharField(max_length=250, blank=True, default="", verbose_name='Observación Intervención')
    interInsumos = models.CharField(max_length=500, blank=True, default=0,verbose_name='Recuento de Insumos Intervención')
    interRecep = models.OneToOneField(RegRecepcion, on_delete=models.CASCADE)
    


    def __str__(self):
        return f'{self.interId}'

class InfTraslado (models.Model):

    trasId = models.BigAutoField(primary_key=True, verbose_name='Id  Traslado')
    trasFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Traslado')
    trasEquipo = models.CharField(max_length=50, verbose_name='Equipo Traslado')
    trasSala = models.CharField(max_length=50, verbose_name='Sala Traslado')
    trasObs = models.CharField(max_length=250, blank=True, default="", verbose_name='Observación Traslado')
    trasRecep = models.OneToOneField(RegRecepcion, on_delete=models.CASCADE)
    trasInter = models.OneToOneField(InfIntervencion, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'{self.trasId}'

class RegQuirurgico (models.Model):

    regQuiId = models.BigAutoField(primary_key=True, verbose_name='Id  Registro de Quirúrgico')
    regQuiFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Registro de Quirúrgico')
    regQuiRec = models.OneToOneField(RegRecepcion, on_delete=models.CASCADE)
    regQuiInter = models.OneToOneField(InfIntervencion, on_delete=models.CASCADE, blank=True, null=True)
    regQuiTras = models.OneToOneField(InfTraslado, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.regQuiId}'