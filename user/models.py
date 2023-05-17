from django.db import models


class Conta(models.Model):
    first_name = models.CharField("First name", max_length=255)
    surname = models.CharField("Surname", max_length=255)
    email = models.CharField("E-mail", max_length=255)
    whatsapp = models.IntegerField("WhatsApp")
    phone_number= models.IntegerField("Phone number")
    occupation = models.CharField("Occupation", max_length=255)
    schooling = models.CharField("Schooling", max_length=255)