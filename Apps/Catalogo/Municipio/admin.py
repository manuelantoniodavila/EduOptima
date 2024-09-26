from django.contrib import admin

from Apps.Catalogo.Municipio.models import Municipio


@admin.register(Municipio)

# Register your models here.
class MunicipioAdmin(admin.ModelAdmin):
    list_display = ['Codigo_Municipio', 'Nombre_Municipio']
    search_fields = ['Codigo_Municipio', 'Nombre_Municipio']
