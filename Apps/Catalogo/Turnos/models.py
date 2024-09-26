from django.db import models
from pyodbc import DATETIME


# Create your models here.
class Turnos(models.Model):
 CodigoModalidad = models.CharField(max_length=35)
 NombreModalidad = models.CharField(max_length=25)
 Horario_Clases  = models.CharField(max_length=10)


 def __str__(self):
  return self.CodigoModalidad