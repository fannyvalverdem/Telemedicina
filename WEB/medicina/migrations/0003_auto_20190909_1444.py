# Generated by Django 2.2.4 on 2019-09-09 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0002_auto_20190909_1414'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='user',
            new_name='email',
        ),
    ]