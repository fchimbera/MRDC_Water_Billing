from django import forms
from .models import MeterReading
from django.contrib.auth import get_user_model

User = get_user_model()

class MeterReadingForm(forms.ModelForm):
    account = forms.ModelChoiceField(
        queryset=User.objects.all().order_by('account_id'),  # Fetch all users, order by account_id
        label='Account',
        to_field_name='account_id',  # Use account_id as the value in the dropdown
        widget=forms.Select(attrs={'class': 'form-control'}),  # Optional: Add a CSS class for styling
        help_text='Select the Account for this reading.'
    )
    reading_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        label='Reading Date'
    )
    reading_value = forms.DecimalField(
        label='Reading Value',
        max_digits=10,
        decimal_places=2,
        widget=forms.NumberInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = MeterReading
        fields = ['account', 'reading_date', 'reading_value']

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.account = self.cleaned_data['account']  # account field now holds the User object
        if commit:
            instance.save()
        return instance