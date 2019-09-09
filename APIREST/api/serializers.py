from rest_framework import serializers
from . import models

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Paciente
		fields=("nombre","apellido","tipo_documento","numero_documento","fecha_nac","sexo","telefono","ciudad","direccion","user_id")

class MedicoSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Doctor
		fields=("identificador_medico")

class TarifaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Tarifa
		fields=("")

class HorarioSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Horarios
		fields=("")

class CitaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Citas
		fields=("fecha","paciente_id","doctor_id")

class RecetaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Recetas
		fields=("fecha","paciente_id","doctor_id")
