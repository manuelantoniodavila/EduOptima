
from django.db import models

# Create your models here.
class Ocupacion(models.Model):
 CodigoOcupacion = models.CharField(max_length=30)
 NombreOcupacion = models.CharField(max_length=60)
 Salario = models.CharField(max_length=20)


 def __str__(self):
  return self.CodigoOcupacion