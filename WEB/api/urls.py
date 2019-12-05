from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^personas/$', views.PersonaViewset.as_view(), name='personas_api'),
	url(r'^especialidad/$', views.EspecialidadViewset.as_view(), name='especialidad_api'),
	url(r'^doctor/$', views.DoctorViewset.as_view(), name='doctor_api'),
	url(r'^paquete/$', views.PaqueteViewset.as_view(), name='paquete_api'),
	url(r'^tarifas/$', views.TarifaViewset.as_view(), name='tarifa_api'),
	url(r'^consulta/$', views.ConsultaViewset.as_view(), name='consulta_api'),
	url(r'^usuario/$', views.UsuarioViewset.as_view(), name='usuario_api'),
	url(r'^horario/$', views.HorarioViewset.as_view(), name='horario_api'),
	url(r'^publicidad/$', views.PublicidadViewset.as_view(), name='publicidad_api'),
	url(r'^administrador/$', views.AdministradorViewset.as_view(), name='administrador_api'),
	url(r'^match_especialidades/$', views.MatchEspecialidadesViewset.as_view(), name='match_espe_api'),
	url(r'^detalles_paquetes/$', views.DetallesPaquetesViewset.as_view(), name='detalles_paquetes_api'),
	url(r'^pagos_paciente/$', views.PagosViewset.as_view(), name='pagos_paciente_api'),
	url(r'^detalles_especialidad/$', views.DetallesEspecialidadViewset.as_view(), name='detalles_especialidad_api'),
	url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
	url(r'^autenticar/', views.AutenticarUsuario.as_view())
]