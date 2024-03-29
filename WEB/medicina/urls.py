from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^inicio_pacientes/$', views.inicio_pacientes, name='inicio_pacientes'),
	url(r'^$', views.inicio, name='inicio'),
	url(r'^agendar_emergencia/$', views.agendar_emergencia, name='agendar_emergencia'),
	url(r'^accounts/$', include('allauth.urls')),
	url(r'^medico_emergencia/$', views.selec_med_emergencia, name='selec_med_emergencia'),
	url(r'^confirmacion_emergencia/$', views.confirmacion_emergencia, name='confirmacion_emergencia'),
	url(r'^junta_medica/$', views.junta_medica, name='junta_medica'),
	url(r'^ver_junta_medica/$', views.ver_junta_medica, name='ver_junta_medica'),
	
	url(r'^aceptar_junta/$', views.aceptar_junta, name='aceptar_junta'),
	url(r'^rechazar_junta/$', views.rechazar_junta, name='rechazar_junta'),


	url(r'^historial_medico_paciente/$', views.historial_medico_paciente, name='historial_medico_paciente'),


	url(r'^selec_medico/$', views.selec_medico, name='selec_medico'),
	url(r'^login/$', views.login, name='login'),
	url(r'^perfil/$', views.perfil, name='perfil'),
	url(r'^editar_perfil/$', views.editar_perfil, name='edit_perfil'),
	url(r'^cerrar_sesion/$', views.cerrar_sesion, name='cerrar_sesion'),

	url(r'^calificar_medico/$', views.calificar_medico, name='calificar_medico'),
	url(r'^calificar_cita/$', views.calificar_cita, name='calificar_cita'),
	
	url(r'^ver_info_medica/$', views.ver_info_medica, name='ver_info_medica'),
	url(r'^ingresar_info_medica/$', views.ingresar_info_medica, name='ingresar_info_medica'),

	url(r'^ver_mas_consejo/$', views.ver_mas_consejo, name='ver_mas_consejo'),
	url(r'^ver_mas_noticias/$', views.ver_mas_noticias, name='ver_mas_noticias'),
	url(r'^mis_noticias/$', views.mis_noticias, name='mis_noticias'),
	url(r'^mis_consejos/$', views.mis_consejos, name='mis_consejos'),

	
	url(r'^consejos_noticias/$', views.consejos_noticias, name='consejos_noticias'),
	
	url(r'^nuestros_paquetes/$', views.nuestros_paquetes, name='nuestros_paquetes'),
	url(r'^paquetes_inicio/$', views.paquetes_inicio, name='paquetes_inicio'),
	url(r'^paquete_pago/$', views.paquete_pago, name='paquete_pago'),
	url(r'^paquete_confirmacion/$', views.paquete_confirmacion, name='paquete_confirmacion'),
	url(r'^mis_paquetes/$', views.mis_paquetes, name='mis_paquetes'),

	url(r'^ver_medico_fav/$', views.ver_medico_fav, name='ver_medico_fav'),
	url(r'^ingresar_medico_fav/$', views.ingresar_medico_fav, name='ingresar_medico_fav'),
	url(r'^ingresar_fav/$', views.ingresar_fav, name='ingresar_fav'),
	
	url(r'^ingresar_noticias/$', views.ingresar_noticias, name='ingresar_noticias'),
	url(r'^ver_noticias/$', views.ver_noticias, name='ver_noticias'),
	url(r'^ingresar_consejos/$', views.ingresar_consejos, name='ingresar_consejos'),
	url(r'^ver_consejos/$', views.ver_consejos, name='ver_consejos'),

	
	url(r'^cambiar_cuenta/$', views.cambiar_cuenta, name='cambiar_cuenta'),
	url(r'^cuentas_vinculadas/$', views.cuentas_vinculadas, name='cuentas_vinculadas'),
	url(r'^crear_grupo_familiar/$', views.crear_grupo_familiar, name='crear_grupo_familiar'),
	url(r'^grupo_familiar/$', views.grupo_familiar, name='grupo_familiar'),

	url(r'^zoom_video/$', views.zoom, name='zoom_video'),
	url(r'^agendar_cita_medico/$', views.agendar_cita_medico, name='agendar_cita_medico'),
	
	url(r'^boton_pago/$', views.boton_pago, name='boton_pago'),
	url(r'^acciones_consulta/$', views.acciones_consulta, name='acciones_consulta'),
	
	url(r'^escribir_receta/$', views.escribir_receta, name='escribir_receta'),
	url(r'^ing_receta/$', views.ing_receta, name='ing_receta'),

	url(r'^citas_medico/$', views.citas_medico, name='citas_medico'),
	url(r'^conteo_citas/$', views.conteo_citas, name='conteo_citas'),
	url(r'^citas_previas/$', views.citas_previas, name='citas_prev'),
	url(r'^citas_proxima/$', views.citas_proximas, name='citas_prox'),
	url(r'^ver_tarifas/', views.ver_tarifas, name='ver_tarifas'),
	url(r'^ver_paquetes/', views.ver_paquetes, name='ver_paquetes'),
	url(r'^ing_paquete/$', views.ingresar_paquete, name='ing-paquete'),
	url(r'^ing_tarifa/$', views.ingresar_tarifa, name='ing-tarifa'),
	url(r'^ing_medico/$', views.ingresar_medico, name='ing-medico'),
	url(r'^ver_medico/', views.ver_medico, name='ver_medico'),
	url(r'^ing_horario/$', views.ingresar_horario, name='ing-horario'),
	url(r'^registro/', views.registro, name='registro'),
	url(r'^paciente/$', views.index_paciente, name='index_paciente'),
	url(r'^medico/$', views.index_medico, name='index_medico'),
	url(r'^administrador/', views.index_admin, name='index_admin'),
	url(r'^agendar_cita/$', views.agendar_cita, name='ag-cita'),
	#url(r'^seleccionar_agendar_cita/$', views.medicos_agendar_cita, name='selec-cita'),
	url(r'^confirmar_cita/$', views.confirmar_agendar_cita, name='confi-cita'),
	url(r'^guardar_cita/$', views.guardar_cita, name='guardar_cita'),

	url(r'^ingresar_publicidad/$', views.publicidad_ingresar, name='ing-publicidad'),
	url(r'^ver_publicidad/$', views.ver_publicidad, name='ver-publicidad'),

	url(r'^reporte_medico/$', views.reporte_medico, name='r_medico'),
	url(r'^reporte_paciente/$', views.reporte_paciente, name='r_paciente'),
	url(r'^reporte_especialidad/$', views.reporte_especialidad, name='r_especialidad'),
	url(r'^reporte_paquete/$', views.reporte_paquete, name='r_paquete'),

	url(r'^ingresar_especialidad/$', views.ingresar_especialidad, name='ingresar_especialidad'),
	url(r'^ver_especialidad/', views.ver_especialidad, name='ver_especialidad'),
	url(r'^match_especialidad/$', views.match_especialidad, name='match_especialidad'),

	url(r'^valores_cobrar/$', views.valores_cobrar, name='valores_cobrar'),
	url(r'^pagos_realizado/$', views.pagos_realizado, name='pagos_realizado'),
	url(r'^pagos_realizados_admin/$', views.pagos_realizados_admin, name='pagos_realizados_admin'),
	url(r'^pagos_pendientes_admin/$', views.pagos_pendientes_admin, name='pagos_pendientes_admin'),
	url(r'^realizar_pago/$', views.realizar_pago, name='realizar_pago'),

	url(r'^auth_zoom/$', views.auth_zoom, name='auth_zoom'),
	url(r'^prueba_auth/$', views.zoom_redirect, name='prueba_auth'),
]