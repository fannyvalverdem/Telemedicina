# Generated by Django 2.1.4 on 2020-01-12 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0013_info_medica_talla'),
    ]

    operations = [
        migrations.AlterField(
            model_name='info_medica',
            name='talla',
            field=models.FloatField(),
        ),
    ]
