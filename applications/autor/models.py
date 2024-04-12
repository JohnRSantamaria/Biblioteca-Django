from django.db import models

# managers
from .managers import AutorManager


class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=70)
    nacionalidad = models.CharField(max_length=30)
    # para valores unicamente positivos por que no se puede tener una edad negativa
    edad = models.PositiveIntegerField()

    def __str__(self):
        return f" ID: {self.id} | {self.nombre} {self.apellidos}"

    class Meta:
        abstract = True


class Autor (Persona):
    # Conectamos el manager con el modelo
    seudonimo = models.CharField('seudomino', max_length=50, blank=True)
    objects = AutorManager()
    
