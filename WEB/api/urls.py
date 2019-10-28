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
	url(r'^administrador/$', views.AdministradorViewset.as_view(), name='administrador_api'),
	url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls'))
]