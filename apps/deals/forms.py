from django import forms
from .models import Deal


class DealForm(forms.ModelForm):
    class Meta:
        model = Deal
        fields = ['title', 'value', 'stage', 'contact', 'company', 'close_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'value': forms.NumberInput(attrs={'class': 'form-control'}),
            'stage': forms.Select(attrs={'class': 'form-select'}),
            'contact': forms.Select(attrs={'class': 'form-select'}),
            'company': forms.Select(attrs={'class': 'form-select'}),
            'close_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
