from django.db import models
from django.db.models import F
from .cocktail import Cocktail

class Ingredient(models.Model):

    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=50)
    measurement = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return f'{self.measurement} of {self.ingredient}' 