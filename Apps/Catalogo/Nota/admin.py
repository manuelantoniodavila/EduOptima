from django.contrib import admin

from Apps.Catalogo.Nota.models import Notas


@admin.register(Notas)

# Register your models here.
class NotasAdmin(admin.ModelAdmin):
    list_display = ['CodigoNota', 'HoraInicio', 'CodigoEstudiante','ApellidoEstudiante','Modalidad','Grado',
        'Materia','Seccion','PrimerCorte','SegundoCorte','TercerCorte','CuartoCorte','PrimerSemestre','SegundoSemestre'
        ,'TotalNotas']
    search_fields = ['CodigoNota', 'HoraInicio', 'CodigoEstudiante','ApellidoEstudiante','Modalidad','Grado',
         'Materia','Seccion','PrimerCorte','SegundoCorte','TercerCorte','CuartoCorte','PrimerSemestre'
         ,'SegundoSemestre','TotalNotas']