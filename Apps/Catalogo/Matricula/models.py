from django.db import models
# Create your models here.
class Matricula(models.Model):
 Codigo_Matricula = models.CharField(max_length=35)
 Grado = models.CharField(max_length=25)
 Fecha_Matricula = models.DateTimeField(auto_now_add=True)

 def __str__(self):
  return self.Codigo_Matricula