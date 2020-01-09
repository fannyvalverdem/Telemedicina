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

	url(r'^grupofamiliar/$', views.GrupoFamiliarViewset.as_view(), name='grupofamiliar'),
	url(r'^recetas_consulta/$', views.RecetasViewset.as_view(), name='recetas_api'),

	url(r'^info_medica/$', views.InfoMedicaViewset.as_view(), name='info_medica_api'),

	url(r'^consejos/$', views.ConsejosViewset.as_view(), name='consejos_api'),
	url(r'^noticias/$', views.NoticiasViewset.as_view(), name='noticias_api'),

	url(r'^medico_favorito/$', views.MedicoFavViewset.as_view(), name='medico_favorito_api'),


	url(r'^medi_consulta/$', views.MedicamentosViewset.as_view(), name='medi_api'),
	url(r'^recetar_consulta/$', views.RecetarMedicamentoViewset.as_view(), name='recetar_api'),
	url(r'^examenes_consulta/$', views.ExamenesViewset.as_view(), name='examenes_api'),


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