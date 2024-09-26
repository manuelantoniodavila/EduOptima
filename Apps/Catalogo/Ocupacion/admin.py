from django.contrib import admin

from Apps.Catalogo.Ocupacion.models import Ocupacion

@admin.register(Ocupacion)

# Register your models here.
class OcupacionAdmin(admin.ModelAdmin):
    list_display = ['CodigoOcupacion', 'NombreOcupacion', 'Salario']
    search_fields = ['CodigoOcupacion', 'NombreOcupacion', 'Salario']