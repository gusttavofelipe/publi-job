from django.db import models
from choices.schooling_choices import SCHOOLING_CHOICES
from choices.stt_choices import STATE_CHOICES
from django.contrib.auth.models import User


class Profile(models.Model):
    username_profile = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Username", null=True, blank=True
    )
    whatsapp = models.PositiveBigIntegerField("WhatsApp")
    phone_number = models.PositiveBigIntegerField("Phone number")
    occupation = models.CharField("Occupation", max_length=255)
    schooling = models.CharField(
        "Schooling",
        max_length=3,
        choices=SCHOOLING_CHOICES,
    )
    user_type = models.CharField(
        "User type",
        max_length=3,
        choices=SCHOOLING_CHOICES,
    )
    about_you = models.TextField("About you")
    address = models.CharField("Address", max_length=255)
    zip_code = models.IntegerField("Zip code")
    neighborhood = models.CharField("Neighborhood", max_length=255)
    city = models.CharField("City", max_length=255)
    state = models.CharField("State", max_length=2, choices=STATE_CHOICES)

    def __str__(self) -> str:
        return f"{self.username_profile}"
