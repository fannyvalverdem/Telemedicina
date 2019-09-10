from django.shortcuts import render
from rest_framework import generics
from medicina import models
from . import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class PersonaViewset(generics.ListAPIView):
    queryset = models.Persona.objects.all()
    serializer_class = serializers.PersonaSerializer

class UsuarioViewset(generics.ListAPIView):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class DoctorViewset(generics.ListAPIView):
	queryset = models.Doctor.objects.all()
	serializer_class = serializers.MedicoSerializer

class PaqueteViewset(generics.ListAPIView):
	queryset = models.Paquete.objects.all()
	serializer_class = serializers.PaquetesSerializer

class ConsultaViewset(generics.ListAPIView):
	queryset = models.Detalle_Consulta.objects.all()
	serializer_class = serializers.DetalleConsultaSerializer

class EspecialidadViewset(generics.ListAPIView):
	queryset = models.Especialidad.objects.all()
	serializer_class = serializers.EspecialidadSerializer

