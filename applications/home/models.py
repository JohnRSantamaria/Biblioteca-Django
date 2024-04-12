from django.db import models


# Create your models here.
class Persona(models.Model):
    nombre_completo = models.CharField('Nombre completo', max_length=50)
    pais = models.CharField("Pais", max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField()
    apelativo = models.CharField('Apelativo', max_length=10)

    class Meta:
        """ Meta definition for persona """
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        # para crear de esta forma el nombre
        db_table = "persona"
        # La combinacion no debe repetirse
        unique_together = ["pais", "apelativo"]
        # Restricciones
        constraints = [
            models.CheckConstraint(check=models.Q(
                edad__gte=18), name="edad_mayor_que_18")
        ]
        # Esto lo hace para los modelos que no se usan como tal mas que para herencia
        abstract = True

    def __str__(self) -> str:
        return self.nombre_completo


class Empleado(Persona):
    empleo = models.CharField('Empleo', max_length=50)
