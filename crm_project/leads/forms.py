from django import forms

from ads.models import AdCampaign
from .models import Lead


class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'middle_name', 'phone', 'email', 'campaign', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'middle_name': 'Отчество',
            'phone': 'Телефон',
            'email': 'Email',
            'campaign': 'Рекламная кампания',
            'notes': 'Примечания',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['campaign'].queryset = AdCampaign.objects.filter(is_active=True)