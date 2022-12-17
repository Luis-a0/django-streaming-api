from django.db import models

# Create your models here.
class Tipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)


class Genero(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)


class Audiovisual(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    generos = models.ManyToManyField(Genero)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    visualizaciones = models.PositiveIntegerField(default=0)
    puntaje = models.PositiveSmallIntegerField(default=1)
