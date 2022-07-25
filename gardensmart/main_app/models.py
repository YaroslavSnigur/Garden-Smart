from django.db import models

# Create your models here.


class Input(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    cost = models.FloatField(default = 0.0)

    

    #add user model later

    def __str__(self):
        return self.name

    #add get absolute url later


class Veg(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 250)
    cost = models.FloatField(default = 0.0)
    seeded = models.IntegerField(default = 0)
    stage = models.CharField(max_length = 50)

    inputs = models.ManyToManyField(Input)

    def __str__(self):
        return self.name



