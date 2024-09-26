
from django.db import models

# Create your models here.
class Departamento(models.Model):
    Codigo_Departamento = models.CharField(max_length=35)
    Nombre_Departamento = models.CharField(max_length=60)

    def __str__(self):
        return self.Codigo_Departamento


# Create your models here.
