import datetime
from django.db import models
from django.db.models import Count

from django.contrib.postgres.search import TrigramSimilarity


class LibroManager(models.Manager):
    """ Managers para el modelo Libro """

    def listar_libros(self, kword):

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=('2022-01-01', '2024-12-31')
        )
        return resultado

    def listar_libros_trgm(self, kword):
        if kword:
            resultado = self.filter(
                titulo__trigram_similar=kword,
            )
            return resultado
        else:
            return self.all()[:10]

    def listar_libros2(self, kword, fecha1, fecha2):

        date1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d")
        date2 = datetime.datetime.strptime(fecha2, "%Y-%m-%d")

        resultado = self.filter(
            titulo__icontains=kword,
            fecha__range=(date1, date2)
        )
        return resultado

    def listar_libros_categoria(self, categoria_id=0):

        if not categoria_id:
            return self.all()
        else:
            return self.filter(
                categoria__id=categoria_id
            ).order_by('titulo')

    def add_autor_libro(self, libro_id: str, autor: str):
        libro = self.get(id=libro_id)

        libro.autores.add(autor)  # Para agregar solo utilizadara el id
        # libro.autores.remove(autor)
        return libro

    def libros_num_prestamos(self):
        resultado = self.aggregate(
            num_prestamos=Count('libro_prestamo')
        )
        return resultado


class CategoriaManager(models.Manager):
    """ Managers para el modelo Categoria """

    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct()

    def listar_categoria_libros(self):
        '''
        Como estoy dentro de el manager de Categorias escribir: 
        self.

        sera igual que escribir: 
        Categioria.objets. 
        ↑ es el modelo 
        '''

        # annotate es como usar un filtro
        resultado = self.annotate(
            # Contara el total de libros que tiene categoria sin embargo libros es un FK
            # y no esta directamente dentro de nuestro modelo categoria, Sin embargo podremos
            # acceder haciendo uso de la relación inversa en Django, en este caso con el related_name
            num_libros=Count('categoria_libro')
        )

        """
        se a agregado num_libros a resultado, y resultado biene siendo la categoria es decir que ademas 
        del id y el nombre que tiene el modelo de categorias ahora este tambien tendra num_libros 
        si se llama este manager
        """

        for res in resultado:
            print(res, res.num_libros)

        return resultado
