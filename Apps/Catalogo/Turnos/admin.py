from django.contrib import admin
from Apps.Catalogo.Turnos.models import Turnos


@admin.register(Turnos)

# Register your models here.
class TurnosAdmin(admin.ModelAdmin):
    list_display = ['CodigoModalidad', 'NombreModalidad', 'Horario_Clases']
    search_fields = ['CodigoModalidad', 'NombreModalidad', 'Horario_Clases']