from django.views.generic import ListView, DetailView

# Models local
from .models import Libro


# Create your views here.
class ListLibros(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):

        palabra_clave = self.request.GET.get("kword", '')
        fecha_1 = self.request.GET.get("fecha1", '')
        fecha_2 = self.request.GET.get("fecha2", '')

        if fecha_1 and fecha_2:
            return Libro.objects.listar_libros2(palabra_clave, fecha_1, fecha_2)
        else:
            return Libro.objects.listar_libros(palabra_clave)


class ListLibrosTrgm(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista.html'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword", '')

        return Libro.objects.listar_libros_trgm(palabra_clave)


class ListLibros2(ListView):
    context_object_name = 'lista_libros'
    template_name = 'libro/lista2.html'

    def get_queryset(self):

        categoria_id = self.request.GET.get("categoria_id", '')
        return Libro.objects.listar_libros_categoria(categoria_id)


class LibroDetailView(DetailView):
    model = Libro
    template_name = "libro/detalle.html"
