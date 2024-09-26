from django.contrib import admin

from Apps.Catalogo.OfertaAcademica.models import OfertaAcademica

@admin.register(OfertaAcademica)

# Register your models here.
class OfertaAcademicaAdmin(admin.ModelAdmin):
    list_display = ['CodigoOferta', 'Grupo', 'Aula','AnoElectivo','HoraInicial','HoraFinal']
    search_fields = ['CodigoOferta', 'Grupo', 'Aula','AnoElectivo','HoraInicial','HoraFinal']