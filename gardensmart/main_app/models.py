from django.db import models

# Create your models here.

class Veg(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 250)
    cost = models.FloatField(default = 0.0)
    seeded = models.IntegerField(default = 0)
    stage = models.CharField(max_length = 50)


class Input(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    cost = models.FloatField(default = 0.0)

    veg = models.ManyToManyField(Veg)

    #add user model later

    def __str__(self):
        return self.NAME

    #add get absolute url later


