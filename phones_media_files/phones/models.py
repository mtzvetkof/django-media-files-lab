from django.db import models


class Phone(models.Model):
    manufacturer = models.CharField(
        max_length=30,
    )
    model = models.CharField(
        max_length=15,
    )
