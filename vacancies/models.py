from django.db import models
from PIL import Image
import os
from django.conf import settings
from categories.models import Category

from choices.stt_choices import STATE_CHOICES
from choices.occupation_choices import OCCUPATION_AREA_CHOICES


class Vacancy(models.Model):
    name = models.CharField('Name', max_length=255)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    occupation_area = models.CharField(
        'Occupation area',
        max_length=3,
        choices=OCCUPATION_AREA_CHOICES
        )
    state = models.CharField('State', max_length=2, choices=STATE_CHOICES)
    city = models.CharField('City', max_length=255)
    number = models.IntegerField('Vacancies number', default=0)
    date_posted = models.DateTimeField(auto_now=True)
    img = models.ImageField(
        'Image', upload_to='vacancies_img/%Y/%m/%d', blank=True, null=True
        )
    salary = models.CharField('Salary', max_length=255)
    about_company = models.TextField('About the company')
    requirements = models.TextField('Requirements')
    activities = models.TextField('Activities')
    benefits = models.TextField('Benefits', blank=True, null=True)
    schedule =  models.TextField('Schedule')
    

    def __str__(self) -> str:
        return self.name
