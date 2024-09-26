from django.db import models


# Create your models here.
class Tutores(models.Model):
 Cedula = models.CharField(max_length=50)
 Nombre1 = models.CharField(max_length=50)
 Nombre2 = models.CharField(max_length=50)
 Apellido1 = models.CharField(max_length=50)
 Apellido2 = models.CharField(max_length=50)
 Centro_de_Trabajo = models.CharField(max_length=85)
 Telefono = models.CharField(max_length=12)
 Correo_Electronico = models.CharField(max_length=75)
 def __str__(self):
   return self.Cedula