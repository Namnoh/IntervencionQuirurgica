from django.db import models

# Create your models here.

# class Paciente (models.Model):

    # paRut = models.IntegerField(primary_key=True, verbose_name='Rut Paciente')
    # paDigVer = models.CharField(max_length=1, verbose_name='Dígito Verificador Paciente')
    # paNombres = models.CharField(max_length=100, verbose_name='Nombres Paciente')
    # paApellidos = models.CharField(max_length=100 ,verbose_name='Apellidos Paciente')
    # paTelefono = models.IntegerField(verbose_name='Teléfono Paciente') # default = None
    # paCorreo = models.CharField(max_length=50, verbose_name='Correo Paciente') # null = True
    # paDireccion = models.CharField(max_length=150,verbose_name='Dirección Paciente')
    # paContEmerg = models.IntegerField(verbose_name='Contacto de Emergencia Paciente')

    # def __str__(self):
    #     return f'{self.paRut} - {self.paDigVer} | {self.paNombres}'

# class RegRecepcion (models.Model):

    # regRecepId = models.BigAutoField(primary_key=True, verbose_name='Id  Registro de Recepción')
    # regRecepFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Registro de Recepción')
    # regRecepHora = models.DateField(default=django.utils.timezone.now, verbose_name='Hora Registro de Recepción')
    # regRecepPac = models.OneToOneField(Paciente, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.regRecepId}'

# class RegQuirurgico (models.Model):

    # regQuiId = models.BigAutoField(primary_key=True, verbose_name='Id  Registro de Quirúrgico')
    # regQuiFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Registro de Quirúrgico')
    # regQuiHora = models.DateField(default=django.utils.timezone.now, verbose_name='Hora Registro de Quirúrgico')
    # regQuiPac = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    # regQuiBit = models.OneToOneField(Bitacora, on_delete=models.CASCADE)
    # regQuiRec = models.OneToOneField(RegRecepcion, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.regQuiId}'

# class Bitacora (models.Model):

    # bitacoraId = models.BigAutoField(primary_key=True, verbose_name='Id  Bitacora')
    # bitacoraFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Bitacora')
    # bitacoraHora = models.DateField(default=django.utils.timezone.now, verbose_name='Hora Bitacora')
    # bitacoraInter = models.OneToOneField(InfIntervencion, on_delete=models.CASCADE)
    # bitacoraTras = models.OneToOneField(infTraslado, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.bitacoraId}'

# class InfIntervencion (models.Model):

    # interId = models.BigAutoField(primary_key=True, verbose_name='Id  Bitacora')
    # interFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Bitacora')
    # interHora = models.DateField(default=django.utils.timezone.now, verbose_name='Hora Bitacora')
    # interTras = models.OneToOneField(infTraslado, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.bitacoraId}'

# class InfTraslado (models.Model):

    # trasId = models.BigAutoField(primary_key=True, verbose_name='Id  Bitacora')
    # trasFecha = models.DateField(default=django.utils.timezone.now, verbose_name='Fecha Bitacora')
    # trasHora = models.DateField(default=django.utils.timezone.now, verbose_name='Hora Bitacora')
    # trasInter = models.OneToOneField(InfIntervencion, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.bitacoraId}'