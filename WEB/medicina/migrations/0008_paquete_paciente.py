# Generated by Django 2.2.4 on 2020-01-09 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0007_auto_20200108_2141'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paquete_Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citas_disponibles', models.IntegerField(default=0)),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Paciente')),
                ('paquete', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Paquete')),
            ],
        ),
    ]
