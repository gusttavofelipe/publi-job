from django.db import models
from PIL import Image
import os
from django.conf import settings
from categories.models import Category

from choices.stt_choices import STATE_CHOICES
from choices.type_choices import TYPE_CHOICES
from choices.occupation_choices import OCCUPATION_AREA_CHOICES


class Vacancy(models.Model):
    name = models.CharField('Name', max_length=255)
    categorie = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
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
    


    # @staticmethod
    # def resize_img(img, new_width=200):
    #     img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)
    #     # print(img_full_path)
    #     img_pill = Image.open(img_full_path) # abrindo img
    #     original_width, original_height = img_pill.size # largura e altura originais

    #     if original_width <= new_width:
    #         img_pill.close() # fechando imagem
    #         return
        
    #     new_height = round(new_width * original_height / original_width)

    #     new_img = img_pill.resize((new_width, new_height), Image.LANCZOS)
    #     new_img.save(img_full_path, optimize=True, quality=50)

    # def save(self, *args, **kwargs) -> None:
    #     # if not self.slug: # slug automatico
    #     #     slug = f'{slugify(self.nome)}'
    #     #     self.slug = slug
            
    #     super().save(*args, **kwargs)

    #     max_img_size = 800
    #     if self.img:
    #         self.resize_img(self.img, max_img_size)

    def __str__(self) -> str:
        return self.name
