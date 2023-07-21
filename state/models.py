from django.db import models
from choices.stt_choices import STATE_CHOICES


class State(models.Model):
    name = models.CharField(max_length=255, choices=STATE_CHOICES)

    def __str__(self) -> str:
        return self.name