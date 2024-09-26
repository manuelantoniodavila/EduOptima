from django.db import models
# Create your models here.
class Notas(models.Model):
 CodigoNota = models.CharField(max_length=35)
 HoraInicio = models.CharField(max_length=50)
 CodigoEstudiante = models.CharField(max_length=35)
 NombreEstudainte = models.CharField(max_length=35)
 ApellidoEstudiante = models.CharField(max_length=35)
 Modalidad = models.CharField(max_length=35)
 Grado = models.CharField(max_length=35)
 Materia = models.CharField(max_length=35)
 Seccion = models.CharField(max_length=35)
 PrimerCorte = models.CharField(max_length=35)
 SegundoCorte = models.CharField(max_length=35)
 TercerCorte = models.CharField(max_length=35)
 CuartoCorte = models.CharField(max_length=35)
 PrimerSemestre = models.CharField(max_length=35)
 SegundoSemestre = models.CharField(max_length=35)
 TotalNotas = models.CharField(max_length=50)


 def __str__(self):
  return self.CodigoNota