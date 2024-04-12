'''
 En este lugar estaran todos los procedimientos o funciones que creamos para hacer consutalas a la base de datos
 al cargarlos los objetos del modelo
'''

from django.db import models
from django.db.models import Q

# Las funciones que creamos le pertenecen exclusivamente a un modelo, para este caso el modelo Autor


class AutorManager(models.Manager):
    """ Managers para el modelo Autor """

    def buscar_autor(self, kword):
        ''' Busca un autor por nombre usando icontains 
            icontains: es un filtro que busca en la base de datos sin importar si es mayuscula o minuscula 
        '''
        resultado = self.filter(
            nombre__icontains=kword
        )

        return resultado

    def buscar_autor2(self, kword):
        ''' Busca un autor por nombre o por apellidos usando icontains y el operador OR
            icontains: es un filtro que busca en la base de datos sin importar si es mayuscula o minuscula
            Q: es un objeto que nos permite hacer consultas mas complejas en la base de datos            
        '''
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )

        return resultado

    def buscar_autor3(self, kword):
        ''' Busca un autor por nombre o por apellidos usando icontains y excluyendo a los autores que tengan 25 años
            icontains: es un filtro que busca en la base de datos sin importar si es mayuscula o minuscula
            exclude: es un filtro que excluye los objetos que cumplan con la condicion
        '''

        resultado = self.filter(
            nombre__icontains=kword
        ).exclude(
            edad=75
        )

        return resultado

    def buscar_autor4(self, kword):
        ''' Busca un autor por nombre o por apellidos usando icontains y excluyendo a los autores que tengan 25 años

            icontains: es un filtro que busca en la base de datos sin importar si es mayuscula o minuscula
            exclude: es un filtro que excluye los objetos que cumplan con la condicion
            order_by: es un filtro que ordena los objetos de la base de datos
            
        
        '''
        resultado = self.filter(
            nombre__icontains=kword
        ).filter(
            edad__lte=75,
            edad__gte=45
        ).order_by('apellidos')

        return resultado
