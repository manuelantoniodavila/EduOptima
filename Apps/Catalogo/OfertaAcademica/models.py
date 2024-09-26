from django.db import models
from pyodbc import DATETIME


# Create your models here.
class OfertaAcademica(models.Model):
 CodigoOferta = models.CharField(max_length=35)
 Grupo = models.CharField(max_length=25)
 Aula = models.CharField(max_length=16)
 AnoElectivo = models.CharField(max_length=60)
 HoraInicial = models.CharField(max_length=10)
 HoraFinal = models.CharField(max_length=10)

 def __str__(self):
  return self.CodigoOferta