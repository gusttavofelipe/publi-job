from django.db import models


class Categorie(models.Model):
    name = models.CharField('Name', max_length=255)

    def __str__(self) -> str:
        return self.name
    