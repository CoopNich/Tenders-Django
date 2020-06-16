from django.db import models
from django.db.models import F
from .cocktail import Cocktail

class Ingredient(models.Model):

    cocktail = models.ForeignKey(Cocktail, on_delete=models.DO_NOTHING)
    ingredient = models.CharField(max_length=50)
    measurement = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.measurement} of {self.ingredient}' 