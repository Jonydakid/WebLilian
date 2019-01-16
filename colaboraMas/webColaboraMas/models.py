from django.db import models

# Create your models here.


class Curso(models.Model):
    nomCurso = models.CharField(max_length=100)
    descripcion = models.TextField()
    valor = models.IntegerField(max_length=20)
    imagen = models.ImageField(upload_to="cursos", blank=True, null=True)


class Mensaje(models.Model):
    codigoMensaje = models.AutoField(primary_key=True)
    curso = models.CharField(max_length = 100)
    nombre = models.CharField(max_length = 30)
    correo = models.EmailField(max_length = 30)
    mensaje = models.TextField()

    