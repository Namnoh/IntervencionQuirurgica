from django.contrib import admin
from . import models

# Register your models here.

class CirugiaAdmin(admin.ModelAdmin):
    search_fields = ['cirugiaId', 'cirugiaNombre'],
    ordering = ['cirugiaNombre']

admin.site.register(models.Usuario)
admin.site.register(models.Cirugia, CirugiaAdmin)
admin.site.register(models.Paciente)
admin.site.register(models.RegRecepcion)
admin.site.register(models.InfIntervencion)
admin.site.register(models.InfTraslado)
admin.site.register(models.RegQuirurgico)