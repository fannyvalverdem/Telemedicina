from rest_framework import serializers
from medicina import models

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Persona
		fields=("nombre","apellido","tipo_documento","numero_documento","fecha_nac","sexo","telefono","ciudad","direccion")

class MedicoSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Doctor
		fields=("identificador_medico")

class PaquetesSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Paquete
		fields=("nombre","descripcion","precio","duracion","especialidad")

#class HorarioSerializer(serializers.ModelSerializer):
#	class Meta:
#		model= models.Horarios
#		fields=("")

class ConsultaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Consulta
		fields=("estado","paciente_id","doctor_id")

#class RecetaSerializer(serializers.ModelSerializer):
#	class Meta:
#		model= models.Recetas
#		fields=("fecha","paciente_id","doctor_id")

class EspecialidadSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Especialidad
		fields=("nombre","descripcion")
