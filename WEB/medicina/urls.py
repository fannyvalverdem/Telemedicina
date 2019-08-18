from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.inicio, name='inicio'),
	path('agendar_emergencia/', views.agendar_emergencia, name='agendar_emergencia'),
	path('accounts/', include('allauth.urls')),
	path('medico_emergencia/', views.selec_med_emergencia, name='selec_med_emergencia'),
	path('confirmacion_emergencia/', views.confirmacion_emergencia, name='confirmacion_emergencia'),
	path('conteo_citas/', views.conteo_citas, name='conteo_citas'),
	path('registro/', views.registro, name='registro'),
	url(r'^paciente/$', views.index_paciente, name='index_paciente'),
	url(r'^medico/$', views.index_medico, name='index_medico'),
	url(r'^administrador/$', views.index_admin, name='index_admin'),
]