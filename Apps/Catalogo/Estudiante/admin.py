from django.contrib import admin


from Apps.Catalogo.Estudiante.models import  InformacionEstudiante


@admin.register(InformacionEstudiante)

# Register your models here.
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ['Codigo_Estudiante', 'Nombres', 'Apellidos','Sexo','Fecha_Nacimiento']
    search_fields = ['Codigo_Estudiante', 'Nombres', 'Apellidos','Sexo','Fecha_Nacimiento']