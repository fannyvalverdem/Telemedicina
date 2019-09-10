from rest_framework import serializers
from medicina import models

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Persona
		fields=("nombre","apellido","tipo_documento","numero_documento","fecha_nac","sexo","telefono","ciudad","direccion")

class UsuarioSerializer(serializers.ModelSerializer):
	persona_id=PersonaSerializer()
	class Meta:
		model= models.Usuario
		fields=("email","username","password","persona_id")


class EspecialidadSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Especialidad
		fields=("nombre","descripcion")

class MedicoSerializer(serializers.ModelSerializer):
	user_id=UsuarioSerializer()
	especialidad=EspecialidadSerializer()

	class Meta:
		model= models.Doctor
		fields=("identificador_medico","user_id","especialidad")


class PaquetesSerializer(serializers.ModelSerializer):
	especialidad=EspecialidadSerializer()
	
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