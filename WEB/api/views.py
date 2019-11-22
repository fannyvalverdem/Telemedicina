from django.shortcuts import render
from rest_framework import generics, status
from medicina import models
from . import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import requests,json

# Create your views here.
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
		persona=models.Persona.objects.all().last()
		myDict = dict(request.data)
		myDict["persona_id"] = serializers.PersonaSerializer(myDict)
		serializer = serializers.UsuarioSerializer(data=myDict)
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
	queryset = models.Detalle_Consulta.objects.all()
	serializer_class = serializers.DetalleConsultaSerializer

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