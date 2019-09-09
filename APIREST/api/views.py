from django.shortcuts import render
from rest_framework import viewsets
from . import models
from . import serializers
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
class PersonaViewset(viewsets.ModelViewSet):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.PersonaSerializer

class MedicoViewset(viewsets.ModelViewSet):
	queryset = models.Noticias.objects.all()
	serializer_class = serializers.MedicoSerializer

class TarifaViewset(viewsets.ModelViewSet):
	queryset = models.Ventas.objects.all()
	serializer_class = serializers.TarifaSerializer

class HorarioViewset(viewsets.ModelViewSet):
    queryset = models.Servicio.objects.all()
    serializer_class = serializers.HorarioSerializer

class CitaViewset(viewsets.ModelViewSet):
	queryset = models.Noticias.objects.all()
	serializer_class = serializers.CitaSerializer

class RecetaViewset(viewsets.ModelViewSet):
	queryset = models.Ventas.objects.all()
	serializer_class = serializers.RecetaSerializer
