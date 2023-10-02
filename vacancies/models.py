from django.db import models
from PIL import Image
import os
from django.conf import settings
from categories.models import Category
from occupation.models import Occupation
from state.models import State
from django.contrib.auth.models import User


class Vacancy(models.Model):
    name = models.CharField('Name', max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    visibility = models.BooleanField('Visible', default=False)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    contact_number = models.PositiveBigIntegerField('Phone number')
    contact_whatsapp = models.PositiveBigIntegerField('WhatsApp')
    contact_email = models.EmailField('E-mail')
    occupation_area = models.ForeignKey(Occupation, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
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
