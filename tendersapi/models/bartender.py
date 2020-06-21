from django.db import models
from django.db.models import F
from django.contrib.auth.models import User

class Bartender(models.Model):

    user = models.OneToOneField(User, related_name="bartender", on_delete=models.CASCADE)
    image_url = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

