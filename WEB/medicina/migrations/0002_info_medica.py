# Generated by Django 2.1.4 on 2020-01-08 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info_Medica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peso', models.FloatField()),
                ('sys', models.FloatField()),
                ('dia', models.FloatField()),
                ('pulse', models.IntegerField()),
                ('glucosa', models.FloatField()),
                ('colesterol', models.FloatField()),
            ],
        ),
    ]
