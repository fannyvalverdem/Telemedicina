from rest_framework import serializers
from medicina import models

class PersonaSerializer(serializers.ModelSerializer):
	class Meta:
		model= models.Persona
		fields=("id","nombre","apellido","tipo_documento","numero_documento","fecha_nac","sexo","telefono","ciudad","direccion")

class UsuarioSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only=True)
	persona_id=PersonaSerializer()
	
	def create(self, validated_data):
		persona_id = validated_data.pop('persona_id')
		usuario = models.Usuario.objects.create(
			email=validated_data['email'],
			username= validated_data['username']
		)
		usuario.set_password(validated_data['password'])
		print(persona_id)
		for persona in persona_id:
			print(persona)
			print(*persona)
		
		person = models.Persona.objects.create(nombre=persona_id['nombre'], apellido= persona_id['apellido'],telefono=persona_id['telefono'], usuario=usuario)
		# person = models.Persona.objects.create(**persona_id, usuario=usuario)
		usuario.persona_id=models.Persona.objects.get(id=person.id)
		usuario.save()
		return usuario

	class Meta:
		fields=("id","email","username","password","persona_id")
		model= models.Usuario

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
		fields=("id","user_id","citas_realizadas")

class PaquetesSerializer(serializers.ModelSerializer):
	especialidad=EspecialidadSerializer()
	
	class Meta:
		model= models.Paquete
		fields=("id","nombre","descripcion","precio","duracion","citas","especialidad")

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

class DetalleConsultaSerializer(serializers.ModelSerializer):
	
	class Meta:
		model= models.Detalle_Consulta
		fields=("fecha_reser","fecha_prog","precio","hora","calificacion")

class ConsultaSerializer(serializers.ModelSerializer):
	doctor_id=MedicoSerializer()
	paciente_id=PacienteSerializer()
	detalle=DetalleConsultaSerializer()
	class Meta:
		model= models.Consulta
		fields=("id","estado","paciente_id","doctor_id","detalle")


#class RecetaSerializer(serializers.ModelSerializer):
#	class Meta:
#		model= models.Recetas
#		fields=("fecha","paciente_id","doctor_id")

class PagosPacienteSerializer(serializers.ModelSerializer):
	paciente=PacienteSerializer()
	class Meta:
		model= models.Pagos_Paciente
		fields=("id","pago_total","paciente")


class DetallesEspecialidadSerializer(serializers.ModelSerializer):
	especialidad=EspecialidadSerializer()
	class Meta:
		model=models.Detalles_Especialidad
		fields=("id","pagos_total","total_doctor","citas_realizadas","especialidad")

class DetallesPaquetesSerializer(serializers.ModelSerializer):
	paquetes=PaquetesSerializer()
	class Meta:
		model=models.Detalles_Paquetes
		fields=("id","pagos_total","total_pacientes","paquetes")

			
class GrupoFamiliarSerializer(serializers.ModelSerializer):
	paciente=PacienteSerializer()
	class Meta:
		model= models.Grupo_Familiar
		fields=("id","usuario_titular","paciente")


class PublicidadSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Publicidad
		fields=("id","name","imagen","fecha","dueno","precio","telefono","ciudad","direccion")
		
class RecetaSerializer(serializers.ModelSerializer):
	paciente=PacienteSerializer()
	doctor_id=MedicoSerializer()
	class Meta:
		model=models.Receta
		fields=("estado","doctor_id","paciente","detalle")

class ExamenesSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Examenes
		fields=("nombre","descripcion")

class MedicamentosSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Examenes
		fields=("nombre","precio")

class RecetarMedicamentoSerializer(serializers.ModelSerializer):
	receta=RecetaSerializer()
	medicamento=MedicamentosSerializer()
	class Meta:
		model=models.RecetarMedicamentos
		fields=("medicamento","receta")

class InfoMedicaSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Info_Medica
		fields=("id","peso","sys","dia","pulse","glucosa","colesterol")

class ConsejosSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Consejos
		fields=("id","imagen","titulo","descripcion","fuente")

class NoticiasSerializer(serializers.ModelSerializer):
	class Meta:
		model=models.Noticias
		fields=("id","imagen","titulo","descripcion","fuente")

class MedicoFavSerializer(serializers.ModelSerializer):
	medico=MatchEspecialidadSerializer()
	paciente=PacienteSerializer()
	class Meta:
		model=models.Medico_Favorito
		fields=("medico","paciente")

class PagosMedicoSerializer(serializers.ModelSerializer):
	doctor=MedicoSerializer()
	class Meta:
		model= models.Pagos_Doctor
		fields=("id","fecha","hora","precio","estado","doctor")