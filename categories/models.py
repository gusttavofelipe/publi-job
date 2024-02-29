from django.db import models


class Category(models.Model):
    name = models.CharField("Name", max_length=255)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self) -> str:
        return self.name
