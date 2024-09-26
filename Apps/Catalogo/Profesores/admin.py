from django.contrib import admin
from Apps.Catalogo.Profesores.models import Profesores


@admin.register(Profesores)

# Register your models here.
class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ['Codigo_Profesor', 'Codigo_Seccion', 'Nombres','Apellidos','Modalidad','Sexo','Cedula']
    search_fields = ['Codigo_Profesor', 'Codigo_Seccion', 'Nombres','Apellidos','Modalidad','Sexo','Cedula']