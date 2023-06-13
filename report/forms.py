from django import forms
from .models import DateTimeModel


class DateTimeForm(forms.ModelForm):
    class Meta:
        model = DateTimeModel
        fields = '__all__'
        widgets = {
            'Prev_Start': forms.DateTimeInput(attrs={'class': 'flatpickr'}),
            'Prev_End': forms.DateTimeInput(attrs={'class': 'flatpickr'}),
            'Curr_Start': forms.DateTimeInput(attrs={'class': 'flatpickr'}),
            'Curr_End': forms.DateTimeInput(attrs={'class': 'flatpickr'}),
        }
