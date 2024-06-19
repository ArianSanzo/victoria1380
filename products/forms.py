from django import forms
from .models import Product, Image
from django.forms import inlineformset_factory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cost', 'categories']
        labels = {
            'name': 'Nombre',
            'cost': 'Precio',
            'categories': 'Categorias',
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        labels = {
            'image': 'Imagen',
        }

ImageFormSet = inlineformset_factory(Product, Image, form=ImageForm, extra=1)