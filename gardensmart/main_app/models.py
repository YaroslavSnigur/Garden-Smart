from django.db import models
from django.urls import reverse
from datetime import datetime

#user schema and authorization
from django.contrib.auth.models import User

# Create your models here.


class Input(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(max_length=50)
    description = models.TextField(max_length=250)
    cost = models.FloatField(default = 0.0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #add user model later

    def __str__(self):
        return self.name

    #add get absolute url later


class Veg(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 250)
    cost = models.FloatField(default = 0.0)
    date = models.DateField("Date", default=datetime.now)
    planted = models.IntegerField(default = 0)
    stage = models.CharField(max_length = 50)

    inputs = models.ManyToManyField(Input, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

