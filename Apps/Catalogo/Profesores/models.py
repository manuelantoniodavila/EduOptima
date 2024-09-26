from django.db import models

# Create your models here.
class Profesores(models.Model):
 Codigo_Profesor = models.CharField(max_length=35)
 Codigo_Seccion = models.CharField(max_length=25)
 Nombres = models.CharField(max_length=80)
 Apellidos = models.CharField(max_length=80)
 Modalidad = models.CharField(max_length=50)
 Sexo = models.CharField(max_length=15)
 Cedula = models.CharField(max_length=50)

 def __str__(self):
  return self.Codigo_Profesor