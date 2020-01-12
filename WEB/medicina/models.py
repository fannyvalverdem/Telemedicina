from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

def imagen_up(instance,filename):
	return "usuarios/%s" %(filename)

def doc_up(instance,filename):
	return "documento/%s" %(filename)

class Persona(models.Model):
	nombre=models.CharField(max_length=250) 
	apellido=models.CharField(max_length=250) 
	tipo_documento=models.CharField(max_length=250, null=True) 
	numero_documento=models.CharField(max_length=250,null=True)
	fecha_nac=models.DateField(null=True)
	edad=models.IntegerField(null=True)
	sexo=models.CharField(max_length=250,null=True)
	telefono=models.CharField(max_length=250,null=True)
	pais=models.CharField(max_length=250,null=True)
	ciudad=models.CharField(max_length=250,null=True)
	direccion=models.CharField(max_length=250,null=True)
	imagen=models.ImageField(upload_to=imagen_up,null=True)

class Usuario(AbstractUser):
	email=models.EmailField()
	username= models.CharField(max_length=50, unique=True)
	persona_id=models.ForeignKey(Persona, null=True, blank=True, on_delete=models.CASCADE)
	
class Especialidad(models.Model):
	nombre= models.CharField(max_length=100)
	descripcion=models.TextField()
	def __str__(self):
		return self.nombre

class Doctor(models.Model):
	identificador_medico=models.CharField(max_length=250)
	documento=models.FileField(upload_to=doc_up,null=True)
	calificacion_total=models.FloatField(default=0,null=True)
	citas_realizadas=models.IntegerField(default=0,null=True)
	user_id=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.user_id.persona_id.nombre+" "+self.user_id.persona_id.apellido

class MatchEspecialidades(models.Model):
	especialidad=models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)
	doctor=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)

class Dias(models.Model):
	nombre= models.CharField(max_length=100)
		
class Horario(models.Model):
	hora_entrada=models.TimeField()
	hora_salida=models.TimeField()
	dias=models.ForeignKey(Dias, null=True, blank=True, on_delete=models.CASCADE)
	doctor=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)

class Paciente(models.Model):
	user_id=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	citas_realizadas=models.IntegerField(default=0,null=True)
	def __str__(self):
		return self.user_id.persona_id.nombre+" "+self.user_id.persona_id.apellido

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

class Citas_Medico(models.Model):
	m_id=models.IntegerField()
	m_url=models.CharField(max_length=300,null=True)
	m_duration=models.IntegerField()
	fecha=models.DateField()
	hora=models.TimeField()
	doctor=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)

class Detalle_Consulta(models.Model):
	fecha_reser=models.DateField()
	fecha_prog=models.DateField()
	hora=models.TimeField()
	precio=models.FloatField()
	calificacion=models.IntegerField()
	especialidad=models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)
	zoom=models.ForeignKey(Citas_Medico, null=True, blank=True, on_delete=models.CASCADE)

class Consulta(models.Model):
	estado=models.TextField()
	paciente_id=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	doctor_id=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
	detalle=models.ForeignKey(Detalle_Consulta, null=True, blank=True, on_delete=models.CASCADE)

class Llamada(models.Model):
	tipo=models.TextField()
	duracion=models.IntegerField()
	calificacion=models.IntegerField()
	consulta_id=models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)

class Receta(models.Model):	
	descripcion=models.TextField()
	consulta_id=models.ForeignKey(Consulta, null=True, blank=True, on_delete=models.CASCADE)

class Examenes(models.Model):
	nombre=models.CharField(max_length=100)
	descripcion=models.CharField(max_length=100)

class Paquete(models.Model):
	nombre= models.CharField(max_length=100)
	descripcion=models.TextField()
	precio=models.FloatField()
	duracion= models.IntegerField()
	citas=models.IntegerField()
	especialidad=models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)
	examen=models.ForeignKey(Examenes, null=True, blank=True, on_delete=models.CASCADE)

class Tarifa(models.Model):
	nombre= models.CharField(max_length=100)
	descripcion=models.TextField()
	precio=models.FloatField()
	def __str__(self):
		return self.nombre
		
class Medicamento(models.Model):
	nombre= models.CharField(max_length=100)
	precio=models.FloatField()
	def __str__(self):
		return self.nombre

class RecetarMedicamentos(models.Model):
	receta=models.ForeignKey(Receta, null=True, blank=True, on_delete=models.CASCADE)
	medicamento=models.ForeignKey(Medicamento, null=True, blank=True, on_delete=models.CASCADE)

class Pagos_Paciente(models.Model):	
	pago_total=models.FloatField(default=0,null=True)
	paciente=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

class Detalles_Especialidad(models.Model):
	pagos_total=models.FloatField(default=0,null=True)
	total_doctor=models.IntegerField(default=0,null=True)
	citas_realizadas=models.IntegerField(default=0,null=True)
	especialidad=models.ForeignKey(Especialidad, null=True, blank=True, on_delete=models.CASCADE)

class MatchPaquetes(models.Model):
	paciente=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	paquete=models.ForeignKey(Paquete, null=True, blank=True, on_delete=models.CASCADE)

class Detalles_Paquetes(models.Model):
	pagos_total=models.FloatField(default=0,null=True)
	total_pacientes=models.IntegerField(default=0,null=True)
	paquetes=models.ForeignKey(Paquete, null=True, blank=True, on_delete=models.CASCADE)


class Grupo_Familiar(models.Model):	
	usuario_titular=models.ForeignKey(Usuario, null=True, blank=True, on_delete=models.CASCADE)
	paciente=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

class Publicidad(models.Model):
	imagen=models.ImageField(upload_to = 'static/imagenes', default='static/imagenes/no-img.jpg')
	name = models.CharField(max_length=100)
	fecha=models.DateTimeField(auto_now_add=True, blank=True)
	dueno=models.CharField(max_length=100)
	precio=models.FloatField()
	telefono=models.CharField(max_length=250,null=True)
	ciudad=models.CharField(max_length=250,null=True)
	direccion=models.CharField(max_length=250,null=True)
		
class Info_Medica(models.Model):	
	peso=models.FloatField()
	talla=models.FloatField()
	sys=models.FloatField()
	dia=models.FloatField()
	pulse= models.IntegerField()
	glucosa=models.FloatField()
	colesterol=models.FloatField()
	

class Noticias(models.Model):
	imagen=models.ImageField(upload_to = 'static/imagenes', default='static/imagenes/no-img.jpg')
	titulo=models.CharField(max_length=250)
	descripcion=models.TextField()
	fuente=models.CharField(max_length=250)

class Consejos(models.Model):
	imagen=models.ImageField(upload_to = 'static/imagenes', default='static/imagenes/no-img.jpg')
	titulo=models.CharField(max_length=250)
	descripcion=models.TextField()
	fuente=models.CharField(max_length=250)

class Medico_Favorito(models.Model):
	medico=models.ForeignKey(MatchEspecialidades, null=True, blank=True, on_delete=models.CASCADE)
	paciente=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)

class Paquete_Paciente(models.Model):
	citas_disponibles=models.IntegerField(default=0)
	paciente=models.ForeignKey(Paciente, null=True, blank=True, on_delete=models.CASCADE)
	paquete=models.ForeignKey(Paquete, null=True, blank=True, on_delete=models.CASCADE)

class Pagos_Doctor(models.Model):
	fecha=models.DateField()
	hora=models.TimeField()
	precio=models.FloatField()
	estado=models.CharField(max_length=200)
	doctor=models.ForeignKey(Doctor, null=True, blank=True, on_delete=models.CASCADE)
	
