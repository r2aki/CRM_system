from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'is_active']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'price': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'name': 'Название продукта',
            'description': 'Описание',
            'price': 'Стоимость (руб.)',
            'is_active': 'Активен',
        }