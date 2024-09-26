from tkinter.constants import CASCADE

from django.db import models


# Create your models here.
class InformacionEstudiante(models.Model):
    Codigo_Estudiante = models.CharField(max_length=35)
    Nombres = models.CharField(max_length=75)
    Apellidos = models.CharField(max_length=75)
    Sexo = models.CharField(max_length=15)
    Fecha_Nacimiento = models.CharField(max_length=15)

    def __str__(self):
        return self.Codigo_Estudiante