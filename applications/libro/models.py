from django.db import models
from django.db.models.signals import post_save

# Apps Tercero
from PIL import Image

# managers
from .managers import LibroManager, CategoriaManager

# Create your models here.
from applications.autor.models import Autor


class Categoria(models.Model):
    nombre = models.CharField('Nombre de la categoria', max_length=50)

    objects = CategoriaManager()

    def __str__(self) -> str:
        return f"ID: {self.id} - {self.nombre}"


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        # Llegar de la categoria a los libros
        related_name='categoria_libro'
    )

    autores = models.ManyToManyField(Autor)
    titulo = models.CharField('Titulo', max_length=250)

    fecha = models.DateField('Fecha de lanzamiento')
    portada = models.ImageField(
        'Imagen de portada', upload_to='portada', blank=True, null=True)
    visitas = models.PositiveIntegerField(default=0, blank=True)
    stock = models.PositiveBigIntegerField(default=0)

    objects = LibroManager()

    class Meta:
        '''
            Es todo aquello que no es un atributo del modelo ni de la tabla de datos, 
            estos metadatos nos van ayudar a personalizar la apariencia de todo en nuestro 
            administrador
        '''
        verbose_name: "Libro"
        verbose_name_plural = "Libros"
        ordering = ['titulo', 'fecha']

    def __str__(self):
        return f"{self.id} - {self.titulo}"


def optimizar_img(sender, instance, **kwargs):

    if instance.portada:
        portada = Image.open(instance.portada.path)
        portada.save(instance.portada.path, quality=20, optimize=True)


post_save.connect(optimizar_img, sender=Libro)

