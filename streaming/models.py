from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Tipo(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Tipo de contenido"
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre


class Genero(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Género"
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre


class Audiovisual(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, verbose_name="Título")
    generos = models.ManyToManyField(Genero, related_name="media_genero", verbose_name="Géneros")
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE, verbose_name="Tipo")
    visualizaciones = models.PositiveIntegerField(default=0, verbose_name="No. Visualizaciones")
    puntaje = models.PositiveSmallIntegerField(
        default=1,
        validators=[MinValueValidator(1) ,MaxValueValidator(5)],
        verbose_name="Puntaje Promedio")
    
    class Meta:
        verbose_name = "Película/Serie"
        ordering = ['nombre']

    def __str__(self) -> str:
        return self.nombre


class AudiovisualUser(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    media = models.ForeignKey(Audiovisual, on_delete=models.CASCADE)
    visto = models.BooleanField(
        default=False)
    puntuacion = models.PositiveSmallIntegerField(
        null=True, validators=[MinValueValidator(1) ,MaxValueValidator(5)])

    class Meta:
        unique_together = ['media', 'user']
        ordering = ['media__nombre']

