# Generated by Django 2.1.4 on 2020-01-09 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0008_paquete_paciente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paquete_paciente',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='paquete_paciente',
            name='paquete',
        ),
        migrations.DeleteModel(
            name='Paquete_Paciente',
        ),
    ]
