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

class PacienteSerializer(serializers.ModelSerializer):
	user_id=UsuarioSerializer()
	class Meta:
		model= models.Doctor
		fields=("id","user_id")


class PaquetesSerializer(serializers.ModelSerializer):
	especialidad=EspecialidadSerializer()
	
	class Meta:
		model= models.Paquete
		fields=("nombre","descripcion","precio","duracion","especialidad")

class TarifasSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= models.Tarifa
		fields=("nombre","descripcion","precio")


class DiasSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Dias
		fields=("id","nombre")

class HorarioSerializer(serializers.ModelSerializer):
	dias=DiasSerializer()
	doctor=MedicoSerializer()
	class Meta:
		model= models.Horario
		fields=("hora_entrada","hora_salida","dias","doctor")


class ConsultaSerializer(serializers.ModelSerializer):
	doctor_id=MedicoSerializer()
	paciente_id=PacienteSerializer()
	class Meta:
		model= models.Consulta
		fields=("estado","paciente_id","doctor_id")

class DetalleConsultaSerializer(serializers.ModelSerializer):
	consulta_id=ConsultaSerializer()
	class Meta:
		model= models.Detalle_Consulta
		fields=("fecha_reser","fecha_prog","precio","calificacion","consulta_id")

#class RecetaSerializer(serializers.ModelSerializer):
#	class Meta:
#		model= models.Recetas
#		fields=("fecha","paciente_id","doctor_id")