from typing import Any, Dict
from django import forms
from ..vacancies import models
from django.contrib.auth.models import User


class PerfilForm(forms.ModelForm):
    class Meta:
        model = models.Conta
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

    def clean(self) -> Dict[str, Any]:
        data = self.data
        clenead = self.cleaned_data