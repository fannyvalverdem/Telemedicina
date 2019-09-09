from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
	user=models.EmailField()
	password=models.CharField(max_length=250)


class Persona(models.Model):
	nombre=models.CharField(max_length=250) 
	apellido=models.CharField(max_length=250) 
	tipo_documento=models.CharField(max_length=250) 
	numero_documento=models.CharField(max_length=250)
	fecha_nac=models.DateField()
	sexo=models.CharField(max_length=250)
	telefono=models.CharField(max_length=250)
	ciudad=models.CharField(max_length=250)
	direccion=models.CharField(max_length=250)
	user_id=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

class Doctor(models.Model):
	identificador_medico=models.CharField(max_length=250)
	user_id=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

class Paciente(models.Model):
	user_id=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

class Administrador(models.Model):
	user_id=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)

class Historial_consulta(models.Model):
	tipo_sangre=models.CharField(max_length=10)
	peso=models.FloatField()
	estatura=models.FloatField()
	fecha=models.DateField()
	documento=models.TextField()
	paciente_id=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

class Recetas(models.Model):
	fecha=models.DateField()
	descripcion=models.TextField()
	paciente_id=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	doctor_id=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)

class Citas(models.Model):
	fecha=models.DateField()
	paciente_id=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	doctor_id=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
