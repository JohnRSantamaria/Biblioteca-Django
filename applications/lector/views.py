from datetime import date

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Prestamo
from .forms import MultiplePrestamoForm, PrestamoForm
# Create your views here.


class RegistarPrestamo(FormView):
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = "add"

    def form_valid(self, form):
        """ Por el contrario .save() solo lo hace si el objeto no esta ya en 
            la base de datos, de estar en la base de datos solo lo actulizara
        """
        prestamo = Prestamo(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            fecha_prestamo=date.today(),
            devuelto=False
        )
        prestamo.save()

        libro = form.cleaned_data['libro']

        libro.stock = libro.stock - 1
        libro.save()

        return super(RegistarPrestamo, self).form_valid(form)


class AddPrestamo(FormView):
    template_name = "lector/add_prestamo.html"
    form_class = PrestamoForm
    success_url = "add"

    def form_valid(self, form):
        """
        Si el registro existe lo recuperamos, si no lo creamos

        en obj: guardara el objeto creado o recuperado.
        en created: es un boleano que dice si lo creo o no. 
        """
        obj, created = Prestamo.objects.get_or_create(
            lector=form.cleaned_data['lector'],
            libro=form.cleaned_data['libro'],
            devuelto=False,
            # Si el registro no existe le podremos decir los datos que necesitaria para crearse
            defaults={
                'fecha_prestamo': date.today()
            }
        )

        if created:
            return super(AddPrestamo, self).form_valid(form)
        else:
            # desde este lugar podriamos redirigir a un lugar en donde
            # informar que ya se le presto el libro a esta presona
            return HttpResponseRedirect('/')


class AddMultiplePrestamo(FormView):
    template_name = "lector/add_multiple_prestamo.html"
    form_class = MultiplePrestamoForm
    success_url = "multiple-add"

    def form_valid(self, form):
        '''
        print(form.cleaned_data['libros'])
        <QuerySet [
          <Libro: 106 - Alias Grace>,
          <Libro: 86 - Cementerio de animales>,
          <Libro: 99 - Conversación en la catedral>,
          <Libro: 47 - El amor en los tiempos del cólera>
        ]>
        '''

        prestamos = []
        'Debemos crear objetos de tipos libros con este query set'
        for l in form.cleaned_data['libros']:
            prestamo = Prestamo(
                lector=form.cleaned_data['lector'],
                libro=l,
                fecha_prestamo=date.today(),
                devuelto=False
            )

            prestamos.append(prestamo)

        '''
            Bulk create recibe un lista, lo registrara todo en una sola 
            consulta
        '''
        Prestamo.objects.bulk_create(prestamos)

        return super(AddMultiplePrestamo, self).form_valid(form)
