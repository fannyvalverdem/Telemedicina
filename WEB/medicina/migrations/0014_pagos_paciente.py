# Generated by Django 2.2.4 on 2019-11-16 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0013_auto_20191112_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagos_Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pago_total', models.FloatField()),
                ('paciente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Paciente')),
            ],
        ),
    ]
