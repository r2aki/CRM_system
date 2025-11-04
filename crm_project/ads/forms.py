from django import forms

from products.models import Product
from .models import AdCampaign


class AdCampaignForm(forms.ModelForm):
    class Meta:
        model = AdCampaign
        fields = ['name', 'product', 'channel', 'budget', 'start_date', 'end_date', 'is_active']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'budget': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'name': 'Название кампании',
            'product': 'Рекламируемый продукт',
            'channel': 'Канал продвижения',
            'budget': 'Бюджет на рекламу (руб.)',
            'start_date': 'Дата начала',
            'end_date': 'Дата окончания',
            'is_active': 'Активна',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(is_active=True)