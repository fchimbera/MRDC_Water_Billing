from django import forms
from .models import MeterReading

class MeterReadingForm(forms.ModelForm):
    class Meta:
        model = MeterReading
        fields = ['account','reading_date', 'reading_value']
        widgets = {
            'reading_date': forms.DateInput(attrs={'type': 'date'}),
        }