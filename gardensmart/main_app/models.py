from django.db import models

# Create your models here.

class Veg(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 250)
    cost = models.FloatField(default = 0.0)
    seeded = models.IntegerField(default = 0)
    stage = models.CharField(max_length = 50)