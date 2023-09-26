from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    
    class Meta:
        model = Vacancy
        fields = '__all__'
        widgets = {
            'visibility': forms.HiddenInput(),
        }
