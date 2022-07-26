from django.db import models
from django.urls import reverse
from datetime import datetime

#user schema and authorization
from django.contrib.auth.models import User
INPUTS = (
    ('Fertilizers','Fertilizers'),
    ('Pesticide', 'Pesticide'),
    ('Tools', 'Tools'),
    ('Seeds', 'Seeds')
)
# Create your models here.
<<<<<<< HEAD

STAGES = (
    ("S", "Seeded"),
    ("G","Growth"),
    ("H", "Harvest-Ready"),
)


=======
>>>>>>> 8e8aaf9739058280a970cd8dcee9f0591f5e2b60
class Input(models.Model):
    name = models.CharField(max_length = 50)
    category = models.CharField(
        max_length=11,
        choices=INPUTS,
        default=INPUTS[0][0]
    )
    description = models.TextField(max_length=250)
    cost = models.FloatField("Cost ($/use)", default = 0.0)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #add user model later

    def __str__(self):
        return self.name

    #add get absolute url later


class Veg(models.Model):
    name = models.CharField(max_length = 50)
    description = models.TextField(max_length = 250)
    cost = models.FloatField("Cost ($/plant)", default = 0.0)
    date = models.DateField("Date", default=datetime.now)
    planted = models.IntegerField(default = 0)
    stage = models.CharField( max_length = 1, choices = STAGES, default=STAGES[0][0])

    inputs = models.ManyToManyField(Input, blank=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

