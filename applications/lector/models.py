from django.db import models
from django.db.models.signals import post_delete

# Create your models here.
from applications.libro.models import Libro
from applications.autor.models import Persona

# Managers
from .managers import PrestamoManager


class Lector(Persona):

    class Meta:
        verbose_name = "Lector"
        verbose_name_plural = "Lectores"


class Prestamo(models.Model):
    lector = models.ForeignKey(
        Lector,
        on_delete=models.CASCADE
    )
    libro = models.ForeignKey(
        Libro,
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )

    fecha_prestamo = models.DateField()

    fecha_devolucion = models.DateField(
        blank=True,
        null=True
    )

    devuelto = models.BooleanField()

    objects = PrestamoManager()

    """ 
    la función save funciona para cuando se ha guardado algún registro en nuestro modelo 
    """

    def save(self, *args, **kwargs):
        self.libro.stock = self.libro.stock - 1
        self.libro.save()
        super(Prestamo, self).save(*args, **kwargs)

    def __str__(self):
        return self.libro.titulo


def update_libro_stock(sender, instance, **kwargs):
    # update stock if the loan is deleted
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.save()


post_delete.connect(update_libro_stock, sender=Prestamo)
