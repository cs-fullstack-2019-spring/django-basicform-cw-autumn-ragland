from django.db import models
from django.utils import timezone


# Account Model
class Account(models.Model):
    name = models.CharField(default="", max_length=200)
    checking = models.DecimalField(max_digits=16, decimal_places=4)
    savings = models.DecimalField(max_digits=16, decimal_places=4)
    dateTimeOpen = models.DateTimeField(default=timezone.now)

    # display objects as object name
    def __str__(self):
        return self.name
