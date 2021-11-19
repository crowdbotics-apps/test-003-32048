from django.conf import settings
from django.db import models


class Boat(models.Model):
    "Generated Model"
    model = models.CharField(
        max_length=256,
    )
    engine_hp = models.BigIntegerField(
        null=True,
        blank=True,
    )
