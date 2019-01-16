from django.db import models

# Create your models here.
class Curso(models.Model):
    NomCurso = models.CharField(max_length=30)
    Valor = models.IntegerField(max_length=20)

