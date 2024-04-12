from django import forms
from applications.libro.models import Libro


from .models import Prestamo


class PrestamoForm(forms.ModelForm):
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro'
        )


class MultiplePrestamoForm(forms.ModelForm):
    """ 
        A 'ModelMultipleChoiceField' se le debe pasar un conjunto de datos 
        lo cual se puede hacer de esta forma: 
        libros = forms.ModelMultipleChoiceField(
            queryset=Libro.objects.all()
        )
    """

    libros = forms.ModelMultipleChoiceField(
        queryset=None,
        required=True,
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Prestamo
        fields = ('lector',)

    def __init__(self, *args, **kwargs):
        super(MultiplePrestamoForm, self).__init__(*args, **kwargs)
        "Dentro de esta funcion podremos operar o haerlo que querramos."

        self.fields['libros'].queryset = Libro.objects.all()
