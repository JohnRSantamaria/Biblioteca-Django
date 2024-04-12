from django.contrib import admin

from .models import Libro
from .models import Categoria
# Register your models here.


class LibroAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'categoria',
                    'stock', 'visitas',)
    search_fields = ('titulo', 'categoria__nombre')
    list_filter = ('categoria', 'fecha', 'autores')

    filter_horizontal = ('autores',)


admin.site.register(Categoria)
admin.site.register(Libro, LibroAdmin)
