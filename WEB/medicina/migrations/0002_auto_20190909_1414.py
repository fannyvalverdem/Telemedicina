# Generated by Django 2.2.4 on 2019-09-09 19:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('medicina', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Doctor')),
                ('paciente_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.TextField()),
                ('doctor_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Doctor')),
                ('paciente_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle_Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_reser', models.DateField()),
                ('fecha_prog', models.DateField()),
                ('precio', models.FloatField()),
                ('calificacion', models.IntegerField()),
                ('consulta_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Especialidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Llamada',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.TextField()),
                ('duracion', models.IntegerField()),
                ('calificacion', models.IntegerField()),
                ('consulta_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Consulta')),
            ],
        ),
        migrations.CreateModel(
            name='Paquete',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.FloatField()),
                ('duracion', models.IntegerField()),
                ('especialidad', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Especialidad')),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('consulta_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Consulta')),
            ],
        ),
        migrations.RemoveField(
            model_name='recetas',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='recetas',
            name='paciente_id',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='user_id',
        ),
        migrations.AddField(
            model_name='usuario',
            name='persona_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Persona'),
        ),
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Citas',
        ),
        migrations.DeleteModel(
            name='Recetas',
        ),
        migrations.AddField(
            model_name='doctor',
            name='especialidad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='medicina.Especialidad'),
        ),
    ]
