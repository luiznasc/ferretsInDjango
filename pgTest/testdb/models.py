from django.db import models

# Create your models here.
class Ferret(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
    weight = models.FloatField()