from django import forms

from products.models import Product
from .models import Contract


class ContractForm(forms.ModelForm):
    class Meta:
        model = Contract
        fields = ['name', 'product', 'document', 'start_date', 'end_date', 'amount']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }
        labels = {
            'name': 'Название контракта',
            'product': 'Предоставляемый продукт',
            'document': 'Файл документа (PDF, DOC, DOCX)',
            'start_date': 'Дата заключения',
            'end_date': 'Период действия до',
            'amount': 'Сумма (руб.)',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(is_active=True)