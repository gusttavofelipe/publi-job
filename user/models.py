from django.db import models
from choices.schooling_choices import SCHOOLING_CHOICES
from choices.stt_choices import STATE_CHOICES


class Profile(models.Model):
    username = models.CharField("Username", max_length=255)
    whatsapp = models.IntegerField("WhatsApp")
    phone_number= models.IntegerField("Phone number")
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
    state = models.CharField(
        "State",
        max_length=2,
        choices=STATE_CHOICES
        )

    def  __str__(self) -> str:
        return self.address
    