from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.inicio, name='inicio'),
	url(r'^agendar_emergencia/$', views.agendar_emergencia, name='agendar_emergencia'),
	url(r'^accounts/$', include('allauth.urls')),
	url(r'^medico_emergencia/$', views.selec_med_emergencia, name='selec_med_emergencia'),
	url(r'^confirmacion_emergencia/$', views.confirmacion_emergencia, name='confirmacion_emergencia'),
	url(r'^conteo_citas/$', views.conteo_citas, name='conteo_citas'),
	url(r'^tarifas/', views.tarifas, name='tarifas'),
	url(r'^ing_paquete/$', views.ingresar_paquete, name='ing-paquete'),
	url(r'^ing_tarifa/$', views.ingresar_tarifa, name='ing-tarifa'),
	url(r'^ing_medico/$', views.ingresar_medico, name='ing-medico'),
	url(r'^ing_horario/$', views.ingresar_horario, name='ing-horario'),
	url(r'^registro/', views.registro, name='registro'),
	url(r'^paciente/$', views.index_paciente, name='index_paciente'),
	url(r'^medico/$', views.index_medico, name='index_medico'),
	url(r'^administrador/', views.index_admin, name='index_admin'),
]