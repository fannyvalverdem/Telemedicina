# Generated by Django 2.1.4 on 2019-10-23 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0008_auto_20191010_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.FloatField()),
            ],
        ),
    ]