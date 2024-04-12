from django.db import models

from django.db.models import Avg, Sum, Count
from django.db.models.functions import Lower


class PrestamoManager(models.Manager):
    def libros_promedio_edades(self, libro_id):
        resultado = self.filter(
            libro__id=libro_id
        ).aggregate(
            promedio_edad=Avg('lector__edad'),
            suma_edades=Sum('lector__edad')
        )
        return resultado

    def num_libros_prestados(self):
        resultado = self.values(
            # Se le inficara en base a que parametro se desea contar
            'libro',
            'lector' # Cuantas veces se ha prestado este libro el lector especifico
        ).annotate(
            num_prestados=Count('libro'),
            titulo=Lower('libro__titulo')
        )

        # Cuando se utiliza en anotete ya no regresa un lista simple
        # ahora regresara un lista pero de diccionarios

        for res in resultado:
            print('==================')
            print(res, res['num_prestados'])

        return resultado
