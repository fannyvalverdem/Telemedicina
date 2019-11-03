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

	url(r'^selec_medico/$', views.selec_medico, name='selec_medico'),
	url(r'^confirmacion_cita/$', views.confirmacion_cita, name='confirmacion_cita'),
	url(r'^login/$', views.login, name='login'),
	url(r'^cerrar_sesion/$', views.cerrar_sesion, name='cerrar_sesion'),

	url(r'^zoom_video/$', views.zoom, name='zoom_video'),
	url(r'^agendar_cita_medico/$', views.agendar_cita_medico, name='agendar_cita_medico'),

	url(r'^boton_pago/$', views.boton_pago, name='boton_pago'),
	url(r'^acciones_consulta/$', views.acciones_consulta, name='acciones_consulta'),
	url(r'^escribir_receta/$', views.escribir_receta, name='escribir_receta'),

	url(r'^citas_medico/$', views.citas_medico, name='citas_medico'),
	url(r'^conteo_citas/$', views.conteo_citas, name='conteo_citas'),
	url(r'^ver_tarifas/', views.ver_tarifas, name='ver_tarifas'),
	url(r'^ver_paquetes/', views.ver_paquetes, name='ver_paquetes'),
	url(r'^ing_paquete/$', views.ingresar_paquete, name='ing-paquete'),
	url(r'^ing_tarifa/$', views.ingresar_tarifa, name='ing-tarifa'),
	url(r'^ing_medico/$', views.ingresar_medico, name='ing-medico'),
	url(r'^ing_horario/$', views.ingresar_horario, name='ing-horario'),
	url(r'^registro/', views.registro, name='registro'),
	url(r'^paciente/$', views.index_paciente, name='index_paciente'),
	url(r'^medico/$', views.index_medico, name='index_medico'),
	url(r'^administrador/', views.index_admin, name='index_admin'),
	url(r'^agendar_cita/$', views.agendar_cita, name='ag-cita'),

	url(r'^ingresar_especialidad/$', views.ingresar_especialidad, name='ingresar_especialidad'),
	url(r'^match_especialidad/$', views.match_especialidad, name='match_especialidad'),

	url(r'^auth_zoom/$', views.auth_zoom, name='auth_zoom'),
	url(r'^prueba_auth/$', views.test_view, name='prueba_auth'),
]