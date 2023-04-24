from django.db import models
from categories.models import Categorie

from choices.stt_choices import STATE_CHOICES
from choices.type_choices import TYPE_CHOICES


class Vacancie(models.Model):
    name = models.CharField('Name', max_length=255)
    categorie = models.ForeignKey(Categorie, on_delete=models.DO_NOTHING)
    kind =  models.CharField('Type', max_length=11,choices=TYPE_CHOICES)
    state = models.CharField('State', max_length=2, choices=STATE_CHOICES)
    city = models.CharField('City', max_length=255)
    number = models.IntegerField('Vacancies number', default=0)
    date_posted = models.DateTimeField(auto_now=True)
    img = models.ImageField('Image', upload_to='vacancies_img/%Y/%m/%d', blank=True, null=True)

    def __str__(self) -> str:
        return self.name
