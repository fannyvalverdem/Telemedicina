# Generated by Django 2.2.4 on 2019-11-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0010_recetarmedicamentos'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='calificacion_total',
            field=models.FloatField(default=0),
        ),
    ]