from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from .bartender import Bartender

class Cocktail(models.Model):
    
    external_id = models.CharField()
    name = models.CharField()
    bartender = models.ForeignKey(Bartender, on_delete=models.DO_NOTHING)
    date_added = models.DateTimeField(auto_now=True)
    glass = models.CharField()
    instructions = models.CharField()
    is_edited = models.BooleanField()
    is_new = models.BooleanField()
    image_url = models.CharField(null=True)
   

    def __str__(self):
        return self.title 