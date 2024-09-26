from django.db import models
# Create your models here.
class Municipio(models.Model):
 Codigo_Municipio = models.CharField(max_length=35)
 Nombre_Municipio = models.CharField(max_length=75)

 def __str__(self):
  return self.Codigo_Municipio
