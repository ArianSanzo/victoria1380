from django import forms
from .models import Product, Image
from django.forms import inlineformset_factory

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'cost', 'primary_category', 'sizes', 'unique_size', 'secondary_categories', 'on_sale']
        labels = {
            'name': 'Nombre',
            'cost': 'Precio',
            'primary_category': 'Categoria principal',
            'secondary_categories': 'Categorías secundarias',
            'sizes': 'Talles',
            'unique_size': 'Talle unico',
            'on_sale': 'En oferta',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'primary_category': forms.Select(attrs={'class': 'form-control'}),
            'secondary_categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'sizes': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'unique_size': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'on_sale': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']
        labels = {
            'image': 'Imagen',
        }

ImageFormSet = inlineformset_factory(Product, Image, form=ImageForm, extra=3)
