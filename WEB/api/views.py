from django.shortcuts import render
from rest_framework import generics, status
from medicina import models
from . import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


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
    	serializer = serializers.UsuarioSerializer(data=request.data)
    	if serializer.is_valid():
    		serializer.save()
    		return Response(serializer.data, status=status.HTTP_201_CREATED)
    	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DoctorViewset(generics.ListAPIView):
	queryset = models.Doctor.objects.all()
	serializer_class = serializers.MedicoSerializer

class PaqueteViewset(generics.ListAPIView):
	queryset = models.Paquete.objects.all()
	serializer_class = serializers.PaquetesSerializer

class TarifaViewset(generics.ListAPIView):
	queryset = models.Tarifa.objects.all()
	serializer_class = serializers.TarifasSerializer

class ConsultaViewset(generics.ListAPIView):
	queryset = models.Detalle_Consulta.objects.all()
	serializer_class = serializers.DetalleConsultaSerializer

class EspecialidadViewset(generics.ListAPIView):
	queryset = models.Especialidad.objects.all()
	serializer_class = serializers.EspecialidadSerializer

class CreateUser(generics.CreateAPIView):
	serializer_class = serializers.UsuarioSerializer
	def post(self, request, format=None):
		serializer = serializers.UsuarioSerializer(data=request.data)
		if serializer.is_valid():

			serializer.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)