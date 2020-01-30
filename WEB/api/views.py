from django.shortcuts import render
from rest_framework import generics, status
from medicina import models
from . import serializers
from rest_framework import filters
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests,json
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

# Create your views here

class AutenticarUsuario(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(AutenticarUsuario, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        # print(models.Paciente.objects.get(user_id=token.user_id).user_id.id)
        if token.user_id == models.Paciente.objects.get(user_id=token.user_id).user_id.id:
        	return Response({'token': token.key, 'id': token.user_id})
        else:
        	return Response("No es paciente", status=status.HTTP_400_BAD_REQUEST)
		
class PersonaViewset(generics.ListAPIView):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer
    def post(self, request, format=None):
    	serializer = serializers.PersonaSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsuarioViewset(generics.ListAPIView):
	queryset = models.Usuario.objects.all()
	serializer_class = serializers.UsuarioSerializer
	
	def post(self, request, format=None):
		# persona=models.Persona.objects.all().last()
		myDict = dict(request.data)
		myDict["persona_id"] = serializers.PersonaSerializer(myDict)
		print(myDict)
		serializer = serializers.UsuarioSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
    def put(self,request,user_id):
    	serializer=UsuarioSerializer(data=request.data)

    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)"""

class AdministradorViewset(generics.ListAPIView):
    queryset = models.Administrador.objects.all()
    serializer_class = serializers.AdministradorSerializer

    def post(self, request, format=None):
    	serializer = serializers.AdministradorSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PacienteViewset(generics.ListAPIView):
	queryset = models.Paciente.objects.all()
	serializer_class = serializers.PacienteSerializer

	def post(self, request, format=None):
		# persona=models.Usuario.objects.all().last()
		myDict = dict(request.data)
		myDict["user_id"] = serializers.UsuarioSerializer(myDict)
		myDict["persona_id"] = serializers.PersonaSerializer(myDict)
		serializer = serializers.PacienteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class HorarioViewset(generics.ListAPIView):
	queryset = models.Horario.objects.all()
	serializer_class = serializers.HorarioSerializer

class DoctorViewset(generics.ListAPIView):
	queryset = models.Doctor.objects.all()
	serializer_class = serializers.MedicoSerializer

class PaqueteViewset(generics.ListAPIView):
	queryset = models.Paquete.objects.all()
	serializer_class = serializers.PaquetesSerializer

class TarifaViewset(generics.ListAPIView):
	queryset = models.Tarifa.objects.all()
	serializer_class = serializers.TarifasSerializer
	def post(self, request, format=None):
		serializer = serializers.TarifasSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.error,status=status.HTTP_400_BAD_REQUEST)

class ConsultaViewset(generics.ListAPIView):
	queryset = models.Consulta.objects.all()
	serializer_class = serializers.ConsultaSerializer

class EspecialidadViewset(generics.ListAPIView):
	queryset = models.Especialidad.objects.all()
	serializer_class = serializers.EspecialidadSerializer

class MatchEspecialidadesViewset(generics.ListAPIView):
	queryset = models.MatchEspecialidades.objects.all()
	serializer_class = serializers.MatchEspecialidadSerializer

class PagosViewset(generics.ListAPIView):
	queryset = models.Pagos_Paciente.objects.all()
	serializer_class = serializers.PagosPacienteSerializer

class DetallesEspecialidadViewset(generics.ListAPIView):
	queryset = models.Detalles_Especialidad.objects.all()
	serializer_class = serializers.DetallesEspecialidadSerializer

class DetallesPaquetesViewset(generics.ListAPIView):
	queryset = models.Detalles_Paquetes.objects.all()
	serializer_class = serializers.DetallesPaquetesSerializer


class GrupoFamiliarViewset(generics.ListAPIView):
	queryset = models.Grupo_Familiar.objects.all()
	serializer_class = serializers.GrupoFamiliarSerializer

class PublicidadViewset(generics.ListAPIView):
	queryset = models.Publicidad.objects.all()
	serializer_class = serializers.PublicidadSerializer

class RecetasViewset(generics.ListAPIView):
	queryset = models.Receta.objects.all()
	serializer_class = serializers.RecetaSerializer

class MedicamentosViewset(generics.ListAPIView):
	queryset = models.Medicamento.objects.all()
	serializer_class = serializers.MedicamentosSerializer

class RecetarMedicamentoViewset(generics.ListAPIView):
	queryset = models.RecetarMedicamentos.objects.all()
	serializer_class = serializers.RecetarMedicamentoSerializer

class ExamenesViewset(generics.ListAPIView):
	queryset = models.Examenes.objects.all()
	serializer_class = serializers.ExamenesSerializer

class InfoMedicaViewset(generics.ListAPIView):
	queryset = models.Info_Medica.objects.all()
	serializer_class = serializers.InfoMedicaSerializer

class ConsejosViewset(generics.ListAPIView):
	queryset = models.Consejos.objects.all()
	serializer_class = serializers.ConsejosSerializer

class NoticiasViewset(generics.ListAPIView):
	queryset = models.Noticias.objects.all()
	serializer_class = serializers.NoticiasSerializer

class MedicoFavViewset(generics.ListAPIView):
	queryset = models.Medico_Favorito.objects.all()
	serializer_class = serializers.MedicoFavSerializer

class PagoDoctorViewset(generics.ListAPIView):
	queryset = models.Pagos_Doctor.objects.all()
	serializer_class = serializers.PagosMedicoSerializer

class CitasMedicoViewset(generics.ListAPIView):
	queryset = models.Citas_Medico.objects.all()
	serializer_class = serializers.CitasMedicoSerializer

class JuntaMedicaViewset(generics.ListAPIView):
	queryset = models.Junta_Medica.objects.all()
	serializer_class = serializers.JuntaMedicaSerializer