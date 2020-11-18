from django import forms
from .models import Animal, Producto

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = ['nombre']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre','descripcion','peso','valor','animal_id','imagen','stock']
