# Generated by Django 4.0.6 on 2022-07-27 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_merge_20220727_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='category',
            field=models.CharField(choices=[('Fertilizers', 'Fertilizers'), ('Pesticides', 'Pesticides'), ('Tools', 'Tools'), ('Seeds', 'Seeds')], default='Fertilizers', max_length=11),
        ),
    ]
