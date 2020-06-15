from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .bartender import Bartender

class Cocktail(models.Model):

    title = models.CharField(max_length=50)
    bartender = models.ForeignKey(Bartender, on_delete=models.DO_NOTHING)
    price = models.FloatField()
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    location = models.CharField(max_length=75, null=True)
    image = models.CharField(max_length=255)
    created_at = models.DateTimeField()
   


    def __str__(self):
        return self.title 