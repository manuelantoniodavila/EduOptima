from django.contrib import admin

from Apps.Catalogo.Departamento.models import Departamento


@admin.register(Departamento)

# Register your models here.
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ['Codigo_Departamento', 'Nombre_Departamento']
    search_fields = ['Codigo_Departamento', 'Nombre_Departamento']



# Register your models here.
