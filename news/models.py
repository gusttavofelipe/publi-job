from django.db import models


class News(models.Model):
    title = models.CharField('Title', max_length=255)
    img = models.ImageField('Image', upload_to='news_img/%Y/%m/%d', blank=True, null=True)
