from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

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

class Usuario(models.Model):
	user=models.EmailField()
	password=models.CharField(max_length=250)
	persona_id=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)


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

class Calificacion(models.Model):
	valor=models.IntegerField()
	paciente_id=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	doctor_id=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)	

class Detalle_Consulta(models.Model):
	fecha=models.DateField()
	precio=models.FloatField()
	calificacion=models.IntegerField()

class Llamada(models.Model):
	tipo=models.TextField()
	precio=models.IntegerField()
	calificacion=models.IntegerField()


class Consulta(models.Model):
	estado=models.TextField()
	paciente_id=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	doctor_id=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
	detalle_id=models.ForeignKey(Detalle_Consulta, null=True, blank=True, on_delete=models.CASCADE)
	llamada_id=models.ForeignKey(Llamada, null=True, blank=True, on_delete=models.CASCADE)


class Receta(models.Model):	
	descripcion=models.TextField()
	consulta_id=models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)