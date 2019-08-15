from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.base, name='base'),
	path('inicio/', views.inicio, name='inicio'),
	path('registro/', views.registro, name='registro'),
	path('paciente/', views.index_paciente, name='index_paciente'),
	path('medico/', views.index_medico, name='index_medico'),
	path('administrador/', views.index_admin, name='index_admin'),
]