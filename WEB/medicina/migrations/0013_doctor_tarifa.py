# Generated by Django 2.2.4 on 2020-01-12 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0012_detalle_consulta_zoom'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='tarifa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Tarifa'),
        ),
    ]
