from django.contrib import admin

from Apps.Catalogo.Matricula.models import Matricula


@admin.register(Matricula)

# Register your models here.
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ['Codigo_Matricula', 'Grado', 'Fecha_Matricula']
    search_fields = ['Codigo_Matricula', 'Grado', 'Fecha_Matricula']
