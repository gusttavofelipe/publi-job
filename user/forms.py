from __future__ import annotations
from django import forms
from django.contrib.auth.models import User
from . import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = "__all__"
        exclude = ("username_profile",)


class UserForm(forms.ModelForm):
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label="Password",
    )

    password2 = forms.CharField(
        required=False, widget=forms.PasswordInput(), label="Confirm password"
    )

    def __init__(self, user=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.user = user

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "password2",
        )

    def clean(self, *args, **kwargs):
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        user_data = cleaned.get("username")
        email_data = cleaned.get("email")
        password_data = cleaned.get("password")
        password2_data = cleaned.get("password2")

        user_db = User.objects.filter(username=user_data).first()
        email_db = User.objects.filter(email=email_data).first()

        error_msg_user_exists = "Usuário já existe"
        error_msg_email_exists = "E-mail já existe"
        error_msg_password_match = "As duas senhas não conferem"
        error_msg_password_short = "Sua senha precisa de pelo menos 6 caracteres"
        error_msg_required_field = "Este campo é obrigatório."

        if not self.user:
            if user_db:
                validation_error_msgs["username"] = error_msg_user_exists

            if email_db:
                validation_error_msgs["email"] = error_msg_email_exists

            if not password_data:
                validation_error_msgs["password"] = error_msg_required_field

            if not password2_data:
                validation_error_msgs["password2"] = error_msg_required_field

            if password_data != password2_data:
                validation_error_msgs["password"] = error_msg_password_match
                validation_error_msgs["password2"] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_msgs["password"] = error_msg_password_short

        if validation_error_msgs:
            raise (forms.ValidationError(validation_error_msgs))
