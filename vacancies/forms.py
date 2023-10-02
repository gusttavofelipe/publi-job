from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    
    class Meta:
        model = Vacancy
        fields = '__all__'
        widgets = {
            'visibility': forms.HiddenInput(),
            'user': forms.HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(VacancyForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.user = user