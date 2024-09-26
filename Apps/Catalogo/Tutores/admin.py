from django.contrib import admin

from Apps.Catalogo.Tutores.models import Tutores


@admin.register(Tutores)

# Register your models here.
class TutoresAdmin(admin.ModelAdmin):
    list_display = ['Cedula', 'Nombre1', 'Nombre2', 'Apellido1', 'Apellido2', 'Centro_de_Trabajo', 'Telefono', 'Correo_Electronico']
    search_fields = ['Cedula', 'Nombre1', 'Nombre2', 'Apellido1', 'Apellido2', 'Centro_de_Trabajo', 'Telefono', 'Correo_Electronico']