from django.db import models

# Create your models here.


class Curso(models.Model):
    idCurso=models.AutoField(primary_key=True)
    nomCurso = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.IntegerField()
    imagen = models.ImageField(upload_to="media", blank=True, null=True)


class Mensaje(models.Model):
    codigoMensaje = models.AutoField(primary_key=True)
    curso = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 30)
    correo = models.EmailField(max_length = 30)
    mensaje = models.TextField()

    