from rest_framework import serializers
from medicina import models

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Persona
		fields=("id","nombre","apellido","tipo_documento","numero_documento","fecha_nac","sexo","telefono","ciudad","direccion")

class UsuarioSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	persona_id=PersonaSerializer()
	class Meta:
		model= models.Usuario
		fields=("id","email","username","password","persona_id")

	def create(self, validated_data):
		persona_id = validated_data.pop('persona_id')
		usuario = models.Usuario.objects.create(**validated_data)
		usuario.set_password(validated_data['password'])
        
		for persona in persona_id:
			person = models.Persona.objects.create(**persona, usuario=usuario)
		
		usuario.save()
		return usuario
<<<<<<< HEAD
=======
		
>>>>>>> fad016dbf53022260091fe70aae42a116eef4bbf

class EspecialidadSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Especialidad
		fields=("nombre","descripcion")

class AdministradorSerializer(serializers.ModelSerializer):
	user_id=UsuarioSerializer()
	class Meta:
		model= models.Administrador
		fields=("id","user_id")

class MedicoSerializer(serializers.ModelSerializer):
	user_id=UsuarioSerializer()

	class Meta:
		model= models.Doctor
		fields=("id","identificador_medico","calificacion_total","citas_realizadas","user_id")

class MatchEspecialidadSerializer(serializers.ModelSerializer):
	doctor=MedicoSerializer()
	especialidad=EspecialidadSerializer()
	class Meta:
		model= models.MatchEspecialidades
		fields=("id","doctor","especialidad")

class PacienteSerializer(serializers.ModelSerializer):
	user_id=UsuarioSerializer()
	class Meta:
		model= models.Paciente
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