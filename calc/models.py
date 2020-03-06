from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
class Order(models.Model):
    numLocations = models.IntegerField()
    nonWhiteApparel = models.BooleanField(default=True)
    colorsF = models.IntegerField()
    colorsB = models.IntegerField()
    colorsR = models.IntegerField()
    colorsL = models.IntegerField()
    colorsSP = models.IntegerField()
    colorsOS = models.IntegerField()
    costPerItem = models.IntegerField()
    margin = models.FloatField()
    quantity = models.IntegerField()
