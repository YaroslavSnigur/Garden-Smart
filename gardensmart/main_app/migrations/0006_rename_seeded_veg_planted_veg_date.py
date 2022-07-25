# Generated by Django 4.0.6 on 2022-07-25 19:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_veg_inputs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='veg',
            old_name='seeded',
            new_name='planted',
        ),
        migrations.AddField(
            model_name='veg',
            name='date',
            field=models.DateField(default=datetime.datetime.now, verbose_name='Date'),
        ),
    ]
