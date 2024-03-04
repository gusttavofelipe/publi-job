from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        if user:
            self.user = user

    class Meta:
        model = Vacancy
        exclude = ["visibility", "owner"]
