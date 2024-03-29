from django.db import models


class State(models.Model):
    name = models.CharField("State", max_length=255)

    def __str__(self) -> str:
        return self.name
