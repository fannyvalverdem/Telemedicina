from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth import authenticate 
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login as auth_login
from .forms import *
from .models import *
from django.contrib.auth.models import User
from .controller import Listar, Add, listar_meeting,add_meeting,add_user,crear_citas,guardar_citas
import requests,json
from .utility import *
from django.http import QueryDict
from django.shortcuts import redirect
from django.contrib import messages
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from datetime import date
import time
import datetime


import base64
import json
import requests

# Create your views here.
@csrf_exempt 
def base(request):
  dictionary = dict(request=request) 
  dictionary.update(csrf(request)) 
  return render(request,'base.html', dictionary)

def cerrar_sesion(request):
	logout(request)
	return redirect(inicio)
	

def inicio(request):
	if request.user.is_authenticated:
		return redirect(inicio_pacientes)
	
	if request.method == 'POST':
		print("POST")
	form = SignupForm(request.POST)
	
	#checking the form is valid or not 
	if form.is_valid():
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		return redirect(inicio_pacientes)
	else:
	#creating a new form
		form = SignupForm()
			#returning form 
	return render(request, 'inicio_sesion.html', {'form':form});

def match_especialidad(request):
	if request.method == 'POST':
		print("POST")
	form= MatchEspecialidad(request.POST)
	if form.is_valid():
		opciones = form.cleaned_data.get('opciones')
		especialidad=Especialidad.objects.last()
		print(opciones[0],"<<<<<<<<<<<<<<")
		for doctor in opciones:
			match=MatchEspecialidades(
				especialidad=especialidad,
				doctor=doctor,
			)

			match.save()
		return redirect('index_admin')
	else:
		form=MatchEspecialidad()
	return render(request, 'match_especialidad.html', {'form':form});

def ingresar_especialidad(request):
	if request.method == 'POST':
		print("POST")
	form= Especialidades(request.POST)
	if form.is_valid():
		nombre =form.cleaned_data['especialidad']
		especialidad=Especialidad(
			nombre=nombre
			)
		especialidad.save()
		return redirect('match_especialidad')
	else:
		form=Especialidades()
	return render(request, 'ingresar_especialidad.html', {'form':form});

def ver_especialidad(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_especialidad.html', dictionary)

def registro(request):
	if request.method == 'POST':
		print("POST")
	usuario=Listar("usuario")
	persona=Listar("personas")
	context= {'usuario':usuario,'persona':persona}
	form = PersonaForm(request.POST)
	form1 = RegistroForm(request.POST)
	#checking the form is valid or not 
	if form1.is_valid():
		if  form.is_valid():
			nombre = form.cleaned_data['name']
			apellido = form.cleaned_data['apellido']
			telefono = form.cleaned_data['phone']
			persona=Persona(
				nombre=nombre,
				apellido=apellido,
				telefono=telefono,
			)
			persona.save()
		
			print("Persona ok")

		# username =form.cleaned_data['email']
		username = form1.cleaned_data['username']
		email =form1.cleaned_data['email']
		# password = form.cleaned_data['password']
		password1 = form1.cleaned_data['password1']
		password2 = form1.cleaned_data['password2']
		
		print(username,email,password1,password2,nombre,apellido,telefono,"<###")
		persona=Persona.objects.order_by('-id')[0]
		usuario=Usuario(
			username=username,
			email=email,
			persona_id=persona
		)
		usuario.set_password(password1)
		usuario.save()
		paciente=Paciente(
			user_id=usuario
		)	
		paciente.save()
		print("------------------GUARDO---------")
		# user = User.objects.create_user(username=email,email=email,password=password)
		# user = authenticate(username=username, password=password)
		# auth_login(request=request, user=user)
		dictionary = dict(request=request) 
		dictionary.update(csrf(request))
		return render(request,'index_paciente.html', context)
		#user = User.objects.create_user(username=email,email=email,password=password)
		#insertarpersona={"nombre":str(nombre),"apellido":str(apellido),"telefono":str(telefono)}
		#Add('personas',insertarpersona)
		#objeto_persona=None
		#response_persona = requests.get('http://127.0.0.1:8000/api/personas/')
		#data_persona = response_persona.json()
		#qs = Persona.objects.filter(id = len(data_persona))
		#print(qs,"<<<<<<")
		#insertarusuario = {"email": str(email), "username":str(username), "password":str(password),"persona_id":None}
		#insertarusuario['persona_id']=insertarpersona
		#Add('usuario',insertarusuario)
		#print(user,"<<<<<<<<<<<<<<<<<<")
	else:
	#creating a new form
		context['error'] = form1.errors
		print(context['error'])
		form = PersonaForm()
		form1 = RegistroForm()
		context = {'form':form, 'form1':form1}
		print("NO ENTRO")
			#returning form 
	return render(request, 'registro.html', context)

def index_paciente(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'index_paciente.html', dictionary)

def index_admin(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'index_admin.html', dictionary)

def index_medico(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'index_medico.html', dictionary)

def agendar_cita_medico(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'agendar_cita_medico.html', dictionary)

def selec_medico(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'seleccionar_medico.html', dictionary)

def agendar_emergencia(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'agendar_emergencia.html', dictionary)

def selec_med_emergencia(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'seleccionar_medico_emergencia.html', dictionary)

def confirmacion_emergencia(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'confirmar_cita_emergencia.html', dictionary)

def conteo_citas(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'conteo_citas_doctor.html', dictionary)

def tarifas(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'tarifas.html', dictionary)

def ver_tarifas(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_tarifas.html', dictionary)

def ver_paquetes(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_paquete.html', dictionary)

def zoom(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'zoom.html', dictionary)

def citas_medico(request): 
	current_user = request.user
	user_ac_id=current_user.id
	doctor=Doctor.objects.get(user_id=user_ac_id)
	cita_prox=Consulta.objects.filter(doctor_id=doctor.id,estado='agendada')
	print(cita_prox)
	return render(request,"citas_medico.html",{'cita_prox':cita_prox})

def reporte_medico(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'reporte_medico.html', dictionary)

def reporte_paciente(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'reporte_paciente.html', dictionary)

def reporte_especialidad(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'reporte_especialidad.html', dictionary)

def reporte_paquete(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'reporte_paquetes.html', dictionary)

def citas_previas(request):
	current_user = request.user
	user_ac_id=current_user.id
	paciente=Paciente.objects.get(user_id=user_ac_id)
	cita_prev=Consulta.objects.filter(paciente_id=paciente.id,estado='realizada')
	print(cita_prev)
	return render(request,"citas_previas_paciente.html",{'cita_prev':cita_prev})


def citas_proximas(request):
	current_user = request.user
	user_ac_id=current_user.id
	paciente=Paciente.objects.get(user_id=user_ac_id)
	cita_prox=Consulta.objects.filter(paciente_id=paciente.id,estado='agendada')
	print(cita_prox)
	return render(request,"citas_proxima_paciente.html",{'cita_prox':cita_prox})

def ver_publicidad(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_publicidad.html', dictionary)

def publicidad_ingresar(request):
	if request.method == 'GET':
		return render(request, 'ingresar_publicidad.html')
	elif request.method == 'POST':
		form = ImageForm(request.POST, request.FILES)
		if form.is_valid():
			new_image=Publicidad(
				imagen=form.cleaned_data["imagen"],
				name=form.cleaned_data["name"],
				dueno=form.cleaned_data["dueno"],
				precio=form.cleaned_data["precio"],
				telefono=form.cleaned_data["telefono"],
				ciudad=form.cleaned_data["ciudad"],
				direccion=form.cleaned_data["direccion"]
				)
			new_image.save()
			return redirect('index_admin')


def perfil(request):
	current_user = request.user
	user_ac_id=current_user.id
	user_ac_person_id=current_user.persona_id.id
	persona=Persona.objects.get(id=user_ac_person_id)
	usuario=Usuario.objects.get(id=user_ac_id)
	
	persona_nombre=persona.nombre
	persona_apellido=persona.apellido
	persona_telefono=persona.telefono
	persona_tipo_documento=persona.tipo_documento
	persona_numero_documento=persona.numero_documento
	persona_sexo=persona.sexo
	persona_edad=persona.edad
	persona_fecha_nac=persona.fecha_nac
	persona_pais=persona.pais
	persona_ciudad=persona.ciudad
	persona_direccion=persona.direccion

	print(persona_nombre,"<-------")
	if request.method == 'POST':
		print("POST")
	default_data = {'nombres': persona_nombre,'apellido': persona_apellido,'num_doc': persona_numero_documento,'genero': persona_sexo,'edad': persona_edad,'fecha_nac': persona_fecha_nac,'pais': persona_pais,'ciudad': persona_ciudad,'direccion': persona_direccion}
	form= PerfilForm(default_data,request.POST)
	if form.is_valid():
		print("VALIDO")
		current_user = request.user
		user_ac_id=current_user.id
		user_ac_person_id=current_user.persona_id.id
		persona=Persona.objects.get(id=user_ac_person_id)
		usuario=Usuario.objects.get(id=user_ac_id)
		
		form.fields['nombres'].widget.attrs['readonly'] = True
		form.fields['apellido'].widget.attrs['readonly'] = True
		#form.fields['tipo_doc'].widget.attrs['readonly'] = True
		form.fields['num_doc'].widget.attrs['readonly'] = True
		form.fields['genero'].widget.attrs['readonly'] = True
		form.fields['edad'].widget.attrs['readonly'] = True
		form.fields['fecha_nac'].widget.attrs['readonly'] = True
		form.fields['pais'].widget.attrs['readonly'] = True
		form.fields['ciudad'].widget.attrs['readonly'] = True
		form.fields['direccion'].widget.attrs['readonly'] = True
	else:
		form=PerfilForm(request)
	return render(request,"perfil.html",{'form':form,'persona':persona,'usuario':usuario})

def editar_perfil(request):
	current_user = request.user
	user_ac_id=current_user.id
	user_ac_person_id=current_user.persona_id.id
	persona=Persona.objects.get(id=user_ac_person_id)
	usuario=Usuario.objects.get(id=user_ac_id)
	persona_nombre=persona.nombre
	persona_apellido=persona.apellido
	persona_telefono=persona.telefono
	#persona_tipo_documento=persona.tipo_documento
	persona_numero_documento=persona.numero_documento
	persona_sexo=persona.sexo
	persona_edad=persona.edad
	persona_fecha_nac=persona.fecha_nac
	persona_pais=persona.pais
	persona_ciudad=persona.ciudad
	persona_direccion=persona.direccion

	if request.method == 'POST':
		print("POST")
	default_data = {'nombres': persona_nombre,'apellido': persona_apellido,'num_doc': persona_numero_documento,'genero': persona_sexo,'edad': persona_edad,'fecha_nac': persona_fecha_nac,'pais': persona_pais,'ciudad': persona_ciudad,'direccion': persona_direccion}
	form= EditarPerfilForm(request.POST)
	form2= EditarPerfilForm(default_data,request.POST)
	if form.is_valid():
		print("VALIDO")

		current_user = request.user
		user_ac_id=current_user.id
		user_ac_person_id=current_user.persona_id.id
		persona=Persona.objects.get(id=user_ac_person_id)
		usuario=Usuario.objects.get(id=user_ac_id)

		
		if form.cleaned_data['nombres']:
			persona.nombre=form.cleaned_data['nombres']
			print(persona.nombre,"<<<<<<<<")
			persona.save()

		if form.cleaned_data['apellido']:
			persona.apellido=form.cleaned_data['apellido']
			persona.save()

		#if form.cleaned_data['tipo_doc']:
		#	tipo=form.cleaned_data['tipo_doc']
		#	if tipo=="1":
		#		persona.tipo_documento="Cedula"
		#	else:
		#		persona.tipo_documento="Pasaporte"
		#	persona.save()

		if form.cleaned_data['num_doc']:
			persona.tipo_documento="Cedula"
			persona.save()
			persona.numero_documento=form.cleaned_data['num_doc']
			print(persona.numero_documento,"<<<<<<<<")
			persona.save()

		if form.cleaned_data['genero']:
			persona.sexo=form.cleaned_data['genero']
			persona.save()

		if form.cleaned_data['edad']:
			persona.edad=form.cleaned_data['edad']
			persona.save()

		if form.cleaned_data['fecha_nac']:
			persona.fecha_nac=form.cleaned_data['fecha_nac']
			persona.save()

		if form.cleaned_data['pais']:
			persona.pais=form.cleaned_data['pais']
			persona.save()

		if form.cleaned_data['ciudad']:
			persona.ciudad=form.cleaned_data['ciudad']
			persona.save()

		if form.cleaned_data['direccion']:
			persona.direccion=form.cleaned_data['direccion']
			persona.save()
		
		#return redirect('perfil')
		#return render(request,"perfil.html",{'form':form,'persona':persona,'usuario':usuario})

	else:
		form=EditarPerfilForm(default_data,request)
	
	return render(request, 'editar_perfil.html', {'form':form2,'persona':persona,'usuario':usuario});

def crear_grupo_familiar(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	current_user = request.user
	user_ac_person_id=current_user.persona_id.id
	persona=Persona.objects.get(id=user_ac_person_id)
	#return render(request,'grupo_familiar.html', {'persona':persona})
	return redirect('grupo_familiar')

def grupo_familiar(request):
	if request.method == 'POST':
		print("POST")
	current_user = request.user
	user_ac_username=str(current_user.username)
	user_ac_person_id=current_user.persona_id.id
	persona=Persona.objects.get(id=user_ac_person_id)
	form=GrupoFamiliarForm(request.POST)
	if form.is_valid():
		correo_vincular=form.cleaned_data['email']
		#correo_vincular = request.POST['correo_vinculacion']
		#is_private = request.POST['is_private']
		#terms=request.POST['terms']
		
		print("llego aca")
		print(correo_vincular,"correo_vincular")
		usuario=Usuario.objects.get(username=correo_vincular)
		print(usuario,"<---")
		usuario_titular=Usuario.objects.get(persona_id=persona)
		paciente=Paciente.objects.get(user_id=usuario)
		
		print(paciente,"<---")
		grupo_fam=Grupo_Familiar(
			usuario_titular=usuario_titular,
			paciente=paciente
			)
		grupo_fam.save()
		return redirect('perfil')
	
	
	return render(request,'grupo_familiar.html', {'form':GrupoFamiliarForm(),'persona':persona})
	#return redirect('grupo_familiar')
	

def cuentas_vinculadas(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	current_user = request.user
	user_ac_person_id=current_user.persona_id.id
	persona=Persona.objects.get(id=user_ac_person_id)
	return render(request,'cuentas_vinculadas.html', {'persona':persona})

def ingresar_paquete(request):
	if request.method == 'POST':
		print("POST")
	form = PaqueteForm(request.POST)
	
	#checking the form is valid or not 
	if form.is_valid():
		nombre =form.cleaned_data['nombre']
		precio =form.cleaned_data['precio']
		especialidad = form.cleaned_data['especialidad']
		duracion =form.cleaned_data['duracion']
		descripcion = form.cleaned_data['descripcion']
		citas=form.cleaned_data['citas']

		paquete=Paquete(
			nombre=nombre,
			precio=precio,
			descripcion=descripcion,
			especialidad=especialidad,
			citas=citas,
			duracion=duracion
		)

		paquete.save()
		return redirect('ver_paquetes') 
	else:
	#creating a new form
		form = PaqueteForm()
			#returning form 
	return render(request, 'ingreso_paquetes.html', {'form':form});

def ingresar_tarifa(request):
	if request.method == 'POST':
		print("POST")
	form = TarifaForm(request.POST)	
	#checking the form is valid or not 
	if form.is_valid():
		nombre =form.cleaned_data['nombre']
		precio =form.cleaned_data['precio']
		descripcion = form.cleaned_data['descripcion']
		
		tarifa=Tarifa(
			nombre=nombre,
			precio=precio,
			descripcion=descripcion
		)

		tarifa.save()
		return redirect('ver_tarifas') 
	else:
	#creating a new form
		form = TarifaForm()
			#returning form 
	return render(request, 'ingresar_tarifa.html', {'form':TarifaForm()});

def ingresar_medico(request):
	if request.method == 'POST':
		print("POST")
	form = DoctorForm(request.POST)
	
	#checking the form is valid or not 
	if form.is_valid():
		nombre =form.cleaned_data['name']
		apellido =form.cleaned_data['apellido']
		especialidad = form.cleaned_data['especialidad']
		documento_id =form.cleaned_data['documento_id']
		num_doc = form.cleaned_data['num_doc']
		email =form.cleaned_data['email']
		password =form.cleaned_data['password']
		direccion = form.cleaned_data['direccion']
		ciudad =form.cleaned_data['ciudad']
		phone = form.cleaned_data['phone']
		celular =form.cleaned_data['celular']
		tarifa =form.cleaned_data['tarifa']
		licencia_med = form.cleaned_data['licencia_med']


		person=Persona(
			nombre=nombre,
			apellido=apellido,
			tipo_documento=documento_id,
			numero_documento=num_doc,
			telefono=phone,
			ciudad=ciudad,
			direccion=direccion
		)

		person.save()

		user=Usuario(
			email=email,
			username=email,
			password=password,
			persona_id=person
		)

		user.set_password(password)
		user.save()

		doc=Doctor(
			identificador_medico=licencia_med,
			tarifa=tarifa,
			user_id=user
		)

		doc.save()

		matchesp=MatchEspecialidades(
			doctor=doc,
			especialidad=especialidad
		)

		matchesp.save()

		return redirect('ing-horario')
	else:
	#creating a new form
		form = DoctorForm()
			#returning form 
	return render(request, 'ingresar_medico.html', {'form':form});

def ver_medico(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_medico.html', dictionary)

def ingresar_horario(request):
	if request.method == 'POST':
		print("POST")
	form = HorarioForm(request.POST)
	
	#checking the form is valid or not 
	if form.is_valid():
		lunes=form.cleaned_data["lunes"]
		martes=form.cleaned_data["martes"]
		miercoles=form.cleaned_data["miercoles"]
		jueves=form.cleaned_data["jueves"]
		sabado=form.cleaned_data["sabado"]
		domingo=form.cleaned_data["domingo"]
		viernes=form.cleaned_data["viernes"]

		if(lunes==True):
			dia=Dias.objects.get(nombre__iexact='Lunes')
			doctor=Doctor.objects.last()
			hora_entrada_lunes=form.cleaned_data["hora_entrada_lunes"]
			minutos_entrada_lunes=form.cleaned_data["minutos_entrada_lunes"]
			hora_salida_lunes=form.cleaned_data["hora_salida_lunes"]
			minutos_salida_lunes=form.cleaned_data["minutos_salida_lunes"]

			entrada=hora_entrada_lunes+":"+minutos_entrada_lunes+":00"
			salida=hora_salida_lunes+":"+minutos_salida_lunes+":00"

			horario=Horario(
				hora_entrada=entrada,
				hora_salida=salida,
				dias=dia,
				doctor=doctor
			)

			horario.save()

		if(martes==True):
			dia=Dias.objects.get(nombre__iexact='Martes')
			doctor=Doctor.objects.last()
			hora_entrada_martes=form.cleaned_data["hora_entrada_martes"]
			minutos_entrada_martes=form.cleaned_data["minutos_entrada_martes"]
			hora_salida_martes=form.cleaned_data["hora_salida_martes"]
			minutos_salida_martes=form.cleaned_data["minutos_salida_martes"]

			entrada=hora_entrada_martes+":"+minutos_entrada_martes+":00"
			salida=hora_salida_martes+":"+minutos_salida_martes+":00"

			horario2=Horario(
				hora_entrada=entrada,
				hora_salida=salida,
				dias=dia,
				doctor=doctor
			)

			horario2.save()

		if(miercoles==True):
			dia=Dias.objects.get(nombre__iexact='Miercoles')
			doctor=Doctor.objects.last()
			hora_entrada_miercoles=form.cleaned_data["hora_entrada_miercoles"]
			minutos_entrada_miercoles=form.cleaned_data["minutos_entrada_miercoles"]
			hora_salida_miercoles=form.cleaned_data["hora_salida_miercoles"]
			minutos_salida_miercoles=form.cleaned_data["minutos_salida_miercoles"]

			entrada=hora_entrada_miercoles+":"+minutos_entrada_miercoles+":00"
			salida=hora_salida_miercoles+":"+minutos_salida_miercoles+":00"

			horario3=Horario(
				hora_entrada=entrada,
				hora_salida=salida,
				dias=dia,
				doctor=doctor
			)

			horario3.save()

		if(jueves==True):
			dia=Dias.objects.get(nombre__iexact='Jueves')
			doctor=Doctor.objects.last()
			hora_entrada_jueves=form.cleaned_data["hora_entrada_jueves"]
			minutos_entrada_jueves=form.cleaned_data["minutos_entrada_jueves"]
			hora_salida_jueves=form.cleaned_data["hora_salida_jueves"]
			minutos_salida_jueves=form.cleaned_data["minutos_salida_jueves"]

			entrada=hora_entrada_jueves+":"+minutos_entrada_jueves+":00"
			salida=hora_salida_jueves+":"+minutos_salida_jueves+":00"

			horario4=Horario(
				hora_entrada=entrada,
				hora_salida=salida,
				dias=dia,
				doctor=doctor
			)

			horario4.save()

		if(viernes==True):
			dia=Dias.objects.get(nombre__iexact='Viernes')
			doctor=Doctor.objects.last()
			hora_entrada_viernes=form.cleaned_data["hora_entrada_viernes"]
			minutos_entrada_viernes=form.cleaned_data["minutos_entrada_viernes"]
			hora_salida_viernes=form.cleaned_data["hora_salida_viernes"]
			minutos_salida_viernes=form.cleaned_data["minutos_salida_viernes"]

			entrada=hora_entrada_viernes+":"+minutos_entrada_viernes+":00"
			salida=hora_salida_viernes+":"+minutos_salida_viernes+":00"

			horario5=Horario(
				hora_entrada=entrada,
				hora_salida=salida,
				dias=dia,
				doctor=doctor
			)

			horario5.save()

		if(sabado==True):
			dia=Dias.objects.get(nombre__iexact='Sabado')
			doctor=Doctor.objects.last()
			hora_entrada_sabado=form.cleaned_data["hora_entrada_sabado"]
			minutos_entrada_sabado=form.cleaned_data["minutos_entrada_sabado"]
			hora_salida_sabado=form.cleaned_data["hora_salida_sabado"]
			minutos_salida_sabado=form.cleaned_data["minutos_salida_sabado"]

			entrada=hora_entrada_sabado+":"+minutos_entrada_sabado+":00"
			salida=hora_salida_sabado+":"+minutos_salida_sabado+":00"

			horario6=Horario(
				hora_entrada=entrada,
				hora_salida=salida,
				dias=dia,
				doctor=doctor
			)

			horario6.save()

		if(domingo==True):
			dia=Dias.objects.get(nombre__iexact='Domingo')
			doctor=Doctor.objects.last()
			hora_entrada_domingo=form.cleaned_data["hora_entrada_domingo"]
			minutos_entrada_domingo=form.cleaned_data["minutos_entrada_domingo"]
			hora_salida_domingo=form.cleaned_data["hora_salida_domingo"]
			minutos_salida_domingo=form.cleaned_data["minutos_salida_domingo"]

			entrada=hora_entrada_domingo+":"+minutos_entrada_domingo+":00"
			salida=hora_salida_domingo+":"+minutos_salida_domingo+":00"

			horario7=Horario(
				hora_entrada=entrada,
				hora_salida=salida,
				dias=dia,
				doctor=doctor
			)

			horario7.save()

		return redirect('prueba_auth')
	else:
	#creating a new form
		form = HorarioForm()
			#returning form 
	return render(request, 'ingresar_horario_medico.html', {'form':form});


def agendar_cita(request):
	if request.method == 'POST':
		print("POST")
		
	form = CitasForms(request.POST)
	if form.is_valid():
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		especialidad = form.cleaned_data['especialidad']
		fecha_reserva = request.POST.get("fecha_reserva")
		data=fecha_reserva.split(' ')
		fecha=data[0]
		hora=data[1]
		fecha_format=datetime.datetime.strptime(fecha, '%m/%d/%Y').strftime('%Y-%m-%d')
		print(fecha_format)
		citas_m=Citas_Medico.objects.filter(fecha=fecha_format,hora__gte=hora,disponible=True)
		match_doctores=MatchEspecialidades.objects.filter(especialidad=especialidad)
		doctores=Doctor.objects.all()
		doc=doctores.filter(id__in=match_doctores)
		citas=citas_m.filter(doctor_id__in=doc).order_by('hora')
		return render(request,'citas_disponibles_agendar.html', {'citas_disponibles':citas,'especialidad':especialidad})
		#return redirect('index_paciente')
	else:
	#creating a new form
		form = CitasForms()
			#returning form 
	context = {'form':form}
	return render(request, 'agendar_cita.html', context );

def confirmar_agendar_cita(request):
	sku_m = request.GET.get('id')
	sepa=sku_m.split('?')
	sku=sepa[0]
	especialidad = sepa[1].split('=')[1]
	cita=Citas_Medico.objects.get(id=sku)

	return render(request,'confirmar_cita.html', {'cita':cita,'especialidad':especialidad})

def guardar_cita(request):
	sku_m = request.GET.get('id')
	sepa=sku_m.split('?')
	sku=sepa[0]
	esp = sepa[1].split('=')[1]
	especialidad=Especialidad.objects.get(nombre=esp)
	cita=Citas_Medico.objects.get(id=sku)
	today = date.today()
	fecha_reser = today.strftime("%Y-%m-%d")
	cita.disponible=False
	cita.save()
	detalle=Detalle_Consulta(
		fecha_reser=fecha_reser,
		fecha_prog=cita.fecha,
		hora=cita.hora,
		precio=cita.doctor.tarifa.precio,
		calificacion=0,
		especialidad=especialidad,
		zoom=cita
		)
	detalle.save()
	current_user = request.user
	user_ac_id=current_user.id
	paciente=Paciente.objects.get(user_id=user_ac_id)

	consulta=Consulta(
		estado='agendada',
		paciente_id=paciente,
		doctor_id=cita.doctor,
		detalle=detalle
		)

	consulta.save()

	return redirect('citas_prox')

def login(request): 
    print(request.method,"<<<<<<<<<<")
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
	        username =form.cleaned_data['email']
	        password = form.cleaned_data['password']
	        user = authenticate(username=username,password=password)
	        print(username)
	        print(password)
	        print(user)
	        if user is not None:
	        	auth_login(request=request,user=user)
	        	response_doctor = requests.get('http://127.0.0.1:8000/api/doctor/')
	        	data_doctor = response_doctor.json()
	        	response_admin = requests.get('http://127.0.0.1:8000/api/administrador/')
	        	data_admin = response_admin.json()
	        	for i in range(0,len(data_doctor)):
	        		print(data_doctor[i]['user_id']['email'])
	        		if username==str(data_doctor[i]['user_id']['email']):
	        			return redirect('index_medico')
	        	for i in range(0,len(data_admin)):
	        		if username==str(data_admin[i]['user_id']['email']):
	        			return redirect('index_admin')
	        	
	        	return redirect('inicio_pacientes')


	        else:
	        	form = SignupForm()
	        	print("NO VALIDO")
	        	msg_to_html = custom_message('Invalid Credentials', TagType.danger)
	        	messages.error(request, 'Nombre de usuario o contraseña incorrecto')
	        	dictionary = dict(request=request, messages = msg_to_html)
	        	dictionary.update(csrf(request))
	        return render(request,'inicio_sesion.html', {'form':form})

def crear_cita(request):
	return redirect('index_paciente')

@api_view(['GET'])
def auth_zoom(request):


    url = "https://zoom.us/oauth/token"
    payload = {
	"grant_type":"authorization_code",
	"code":request.query_params.get('code'),
	"redirect_uri": "http://127.0.0.1:8000/auth_zoom"
    }
    # Noten la b""     Aqui v
    auth = base64.b64encode(b"WgCo2Mo8RkupkAANM8Wxdg:GEQ5hdNoV7UookqET1ngUojTH22xQZPH")
    headers = {
        'Authorization': "Basic " + auth.decode("utf-8"),
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    data_json=response.json()
    #print(data_json['access_token'])
    token=data_json['access_token']
    doctor=Doctor.objects.last()
    usuario=doctor.user_id
    persona=usuario.persona_id
    #print(doctor.id)
    horarios=Horario.objects.filter(doctor_id =doctor.id)
    #print(horarios)
    print(usuario.email)
    crear_citas(token,horarios,'ivinces@espol.edu.ec',doctor)
    #guardar_citas('ivinces@espol.edu.ec',token,doctor)
    return redirect('index_admin')

def zoom_redirect(request):
	return redirect('https://zoom.us/oauth/authorize?response_type=code&client_id=WgCo2Mo8RkupkAANM8Wxdg&redirect_uri=http://127.0.0.1:8000/auth_zoom')

def test_view(request):
	print(request.session.get("code"))
	return HttpResponse('Adios Mundo')



def boton_pago(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'boton_pago.html', dictionary)

def acciones_consulta(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'acciones_consulta.html', dictionary)

def ing_receta(request):
	current_user = request.user
	user_ac_id=current_user.id
	user_ac_person_id=current_user.persona_id.id
	doctor=Persona.objects.get(id=user_ac_person_id)
	usuario=Usuario.objects.get(id=user_ac_id)
	consulta=Consulta.objects.last() #Cambiar
	paciente=consulta.paciente_id
	detalles=consulta.detalle
	especialidad=detalles.especialidad

	if request.method == 'POST':
		print("POST")

		formset=MedicamentoFormset(request.POST)
		if formset.is_valid():
			for form in formset:
				name = form.cleaned_data.get('nombre')
				cant = form.cleaned_data.get('cantidad')
				des = form.cleaned_data.get('descripcion')
				print(name)
				print(cant)
				print(des)
			return redirect('index_medico')
	else:
		form=RecetaForm()
		formset=MedicamentoFormset()

	return render(request, 'escribir_receta2.html', {'formset':formset,'doctor':doctor,'paciente':paciente,'especialidad':especialidad})


def escribir_receta(request):
	if request.method == 'POST':
		print("POST")
	
	form= RecetaForm(request.POST)

	consulta=Consulta.objects.last()
	field_value = getattr(consulta, 'paciente_id')
	print(field_value,"<<<<<<<")
	#paciente=Paciente.objects.get(id=field_value)
	#field_value1 = getattr(paciente, 'id')
	field_value1 = getattr(field_value, 'id')
	print(field_value1,"<<<<<<<")
	usuario=Usuario.objects.get(id=field_value1)
	field_value2 = getattr(usuario, 'id')
	print(field_value2,"<<<<<<<")
	persona=Persona.objects.get(id=field_value2)
	form= RecetaForm(initial={'name': getattr(persona, 'nombre')})
	
	if form.is_valid():
		consulta=Consulta.objects.last()
		field_value = getattr(consulta, 'id')
		paciente=Paciente.objets.get(user_id=field_value)
		field_value1 = getattr(paciente, 'id')
		usuario=Usuario.objects.get(persona_id=field_value1)
		field_value2 = getattr(usuario, 'id')
		persona=Persona.objects.get(numero_documento=field_value2)

		print(persona,"<><><><>")
		form.cleaned_data['name']=getattr(persona, 'name')
		form.cleaned_data['apellido']=getattr(persona, 'apellido')
		form.cleaned_data['cedula']=getattr(persona, 'cedula')
		cedula=form.cleaned_data['cedula']

		form.cleaned_data['especialidad']='Especialidad'
		descripcion =form.cleaned_data['descripcion']
		medicamentos = form.cleaned_data.get('medicamentos')
		
		# persona=Persona.objects.get(numero_documento=cedula)
		# usuario=Usuario.objects.get(persona_id=persona)
		# paciente=Paciente.objets.get(user_id=usuario)
		# consulta=Consulta.objects.get(paciente_id=paciente)

		receta=Receta(
			descripcion=descripcion,
			consulta_id=consulta
			)
		receta.save()

		for med in medicamentos:
			escribir=RecetarMedicamentos(
				receta=receta,
				medicamento=med,
			)

			escribir.save()

		return redirect('index_medico')
	else:
		form=RecetaForm()
	return render(request, 'escribir_receta.html', {'form':form})

def calificar_medico(request):
	if request.method == 'GET':
		print(request.GET.get("Estrellas"),"<<<<<<<<")
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'calificar_medico.html', dictionary)


def calificar_cita(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'calificar_cita.html', dictionary)

def cambiar_cuenta(request):
	if request.method == 'POST':
		print("POST")
	
	# username =form.cleaned_data['email']
 #    password = form.cleaned_data['password']
 #    user = authenticate(username=username,password=password)
 #    if user is not None:
 #    	auth_login(request=request,user=user)
	# 	return redirect('inicio')
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return redirect('cuentas_vinculadas')

def resumen_consulta(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return redirect('cuentas_vinculadas')

def ver_info_medica(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_info_medica.html', dictionary)

def ingresar_info_medica(request):
	if request.method == 'POST':
		print("POST")
	form = InfoMedicaForm(request.POST)
	
	#checking the form is valid or not 
	if form.is_valid():
		peso =form.cleaned_data['peso']
		talla =form.cleaned_data['talla']
		sys =form.cleaned_data['sys']
		dia = form.cleaned_data['dia']
		pulse =form.cleaned_data['pulse']
		glucosa = form.cleaned_data['glucosa']
		colesterol = form.cleaned_data['colesterol']

		paquete=Info_Medica(
			peso=peso,
			talla=talla,
			sys=sys,
			dia=dia,
			pulse=pulse,
			glucosa=glucosa,
			colesterol=colesterol
		)

		paquete.save()
		return redirect('ver_info_medica') 
	else:
	#creating a new form
		form = InfoMedicaForm()
			#returning form 
	return render(request, 'ingresar_info_manual.html', {'form':form});

def consejos_noticias(request):
	last_tres = Consejos.objects.order_by('-id')[:3]
	last_tres2 = Noticias.objects.order_by('-id')[:3]
	data_consejo=[]
	data_noticia=[]
	for conse in last_tres:		
		ids=conse.id
		imagen=str(conse.imagen)
		titulo=conse.titulo
		descripcion=conse.descripcion
		fuente=conse.fuente
		consejo = {'id':ids,'imagen': imagen,'titulo': titulo,'descripcion': descripcion,'fuente': fuente}
		data_consejo.append(consejo)
	for noti in last_tres2:		
		ids=noti.id
		imagen=str(noti.imagen)
		titulo=noti.titulo
		descripcion=noti.descripcion
		fuente=noti.fuente
		noticia = {'id':ids,'imagen': imagen,'titulo': titulo,'descripcion': descripcion,'fuente': fuente}
		data_noticia.append(noticia)
	context= {'object_list': data_consejo,'object_list2': data_noticia}
	return render(request, 'consejos_noticias.html', context)

def mis_noticias(request):
	noticias = Listar("noticias")
	print(str(noticias[0]['imagen']).split("noticias/")[1],"<<<<<<<<<<")
	for n in noticias:
		n['imagen']=str(n['imagen']).split("noticias/")[1]
	context= {'object_list': noticias}
	return render(request, 'mis_noticias.html', context)

def mis_consejos(request):
	consejos = Listar("consejos")
	print(str(consejos[0]['imagen']).split("consejos/")[1],"<<<<<<<<<<")
	for c in consejos:
		c['imagen']=str(c['imagen']).split("consejos/")[1]
	context= {'object_list': consejos}
	return render(request, 'mis_consejos.html', context)

def ver_consejos(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_consejos.html', dictionary)

def ingresar_consejos(request):
	if request.method == 'GET':
		return render(request, 'ingresar_consejos.html')
	elif request.method == 'POST':
		form = ConsejosForm(request.POST, request.FILES)
		if form.is_valid():
			new_image=Consejos(
				imagen =form.cleaned_data['imagen'],
				titulo =form.cleaned_data['titulo'],
				descripcion = form.cleaned_data['descripcion'],
				fuente =form.cleaned_data['fuente']
				)
			new_image.save()
			return redirect('ver_consejos')

	

def ver_noticias(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_noticias.html', dictionary)

def ingresar_noticias(request):
	if request.method == 'GET':
		return render(request, 'ingresar_noticias.html')
	elif request.method == 'POST':
		form = NoticiasForm(request.POST, request.FILES)
		if form.is_valid():
			new_image=Noticias(
				imagen =form.cleaned_data['imagen'],
				titulo =form.cleaned_data['titulo'],
				descripcion = form.cleaned_data['descripcion'],
				fuente =form.cleaned_data['fuente']
				)
			new_image.save()
			return redirect('ver_noticias')

def paquetes_inicio(request):
	last_tres = Paquete.objects.order_by('-id')[:3]
	data=[]
	for paque in last_tres:
		paque_id=paque.id
		nombre=paque.nombre
		descripcion=paque.descripcion
		citas=paque.citas
		duracion=paque.duracion
		precio=paque.precio
		paquete={'id':paque_id,'nombre': nombre,'descripcion': descripcion,'citas': citas,'duracion': duracion,'precio':precio}
		data.append(paquete)
		print(data)

	context= {'object_list': data}
	return render(request, 'paquetes_inicio.html', context)

def ver_mas_consejo(request):

	sku = request.GET.get('id')
	print(sku)
	conse=Consejos.objects.get(id=sku)
	imagen=str(conse.imagen)
	print(imagen,"<<<<<<<<<<")
	titulo=conse.titulo
	descripcion=conse.descripcion
	fuente=conse.fuente
	data = [{'imagen': imagen,'titulo': titulo,'descripcion': descripcion,'fuente': fuente}]
	context= {'object_list':data}
	return render(request,'detalles_noticia_consejo.html',context)

def ver_mas_noticias(request):
	sku = request.GET.get('ids')
	conse=Noticias.objects.get(id=sku)
	imagen=str(conse.imagen)
	print(imagen,"<<<<<<<<<<")
	titulo=conse.titulo
	descripcion=conse.descripcion
	fuente=conse.fuente
	data = [{'imagen': imagen,'titulo': titulo,'descripcion': descripcion,'fuente': fuente}]
	context= {'object_list':data}
	return render(request,'detalles_noticia_consejo.html',context)

def paquete_pago(request):
	sku = request.GET.get('id')
	print(sku)
	paque=Paquete.objects.get(id=sku)
	print(paque)
	paque_id=paque.id
	nombre=paque.nombre
	descripcion=paque.descripcion
	citas=paque.citas
	duracion=paque.duracion
	precio=paque.precio
	
	data = [{'id':paque_id,'nombre': nombre,'descripcion': descripcion,'citas': citas,'duracion': duracion,'precio':precio}]
	context= {'object_list':data}
	return render(request,'comprar_paquete.html',context)

def ingresar_medico_fav(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ingresar_medico_fav.html', dictionary)

def ver_medico_fav(request):	
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_medico_fav.html', dictionary)

def ingresar_fav(request):
	current_user = request.user

	user_ac_id=current_user.id
	usuario=Usuario.objects.get(id=user_ac_id)
	paciente=Paciente.objects.get(user_id=usuario)
	print(paciente)

	sku = request.GET.get('id')
	doc=Doctor.objects.get(id=sku)
	match_esp=MatchEspecialidades.objects.get(doctor=doc)

	med_fav=Medico_Favorito(
		medico =match_esp,
		paciente =paciente
		)
	med_fav.save()
	#redirect('ver_medico_fav')
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'ver_medico_fav.html', dictionary)

def paquete_confirmacion(request):
	sku = request.GET.get('id')
	paque=Paquete.objects.get(id=sku)

	current_user = request.user
	user_ac_id=current_user.id
	paciente=Paciente.objects.get(user_id=user_ac_id)
	
	paque_pac=Paquete_Paciente(
		citas_disponibles=paque.citas,
		paciente=paciente,
		paquete=paque
		)
	paque_pac.save()

	nombre=paque.nombre
	descripcion=paque.descripcion
	citas=paque.citas
	duracion=paque.duracion
	precio=paque.precio
	
	data = [{'nombre': nombre,'descripcion': descripcion,'citas': citas,'duracion': duracion,'precio':precio}]
	context= {'object_list':data}
	
	return render(request,'confirmacion_paquete.html',context)

def mis_paquetes(request):
	current_user = request.user
	user_ac_id=current_user.id
	paciente=Paciente.objects.get(user_id=user_ac_id)
	paque_pac=Paquete_Paciente.objects.filter(paciente=paciente.id)
	data=[]
	for paque in paque_pac:
		nombre=paque.paquete.nombre
		descripcion=paque.paquete.descripcion
		citas=paque.paquete.citas
		duracion=paque.paquete.duracion
		precio=paque.paquete.precio
		citas_disponibles=paque.citas_disponibles
		paquete={'nombre': nombre,'descripcion': descripcion,'citas': citas,'duracion': duracion,'precio':precio,'faltantes':citas_disponibles}
		data.append(paquete)
		print(data)

	context= {'object_list':data}
	return render(request,'mis_paquetes.html',context)

def valores_cobrar(request):	
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'valores_cobrar.html', dictionary)

def pagos_realizado(request):	
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'pagos_realizados.html', dictionary)

def pagos_realizados_admin(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'pagos_realizados_admin.html', dictionary)

def pagos_pendientes_admin(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'pagos_pendientes_admin.html', dictionary)

def realizar_pago(request):
	sku = request.GET.get('id')
	pago=Pagos_Doctor.objects.get(id=sku)
	pago.estado="pagado"

	pago.save()
	
	return redirect('pagos_realizados_admin')

def inicio_pacientes(request):
	last_tres = Paquete.objects.order_by('-id')[:3]
	data=[]
	for paque in last_tres:
		paque_id=paque.id
		nombre=paque.nombre
		descripcion=paque.descripcion
		citas=paque.citas
		duracion=paque.duracion
		precio=paque.precio
		paquete={'id':paque_id,'nombre': nombre,'descripcion': descripcion,'citas': citas,'duracion': duracion,'precio':precio}
		data.append(paquete)
		print(data)

	last_tres2 = Consejos.objects.order_by('-id')[:3]
	last_tres3 = Noticias.objects.order_by('-id')[:3]
	data_consejo=[]
	data_noticia=[]
	for conse in last_tres2:		
		ids=conse.id
		imagen=str(conse.imagen)
		titulo=conse.titulo
		descripcion=conse.descripcion
		fuente=conse.fuente
		consejo = {'id':ids,'imagen': imagen,'titulo': titulo,'descripcion': descripcion,'fuente': fuente}
		data_consejo.append(consejo)
	for noti in last_tres3:		
		ids=noti.id
		imagen=str(noti.imagen)
		titulo=noti.titulo
		descripcion=noti.descripcion
		fuente=noti.fuente
		noticia = {'id':ids,'imagen': imagen,'titulo': titulo,'descripcion': descripcion,'fuente': fuente}
		data_noticia.append(noticia)
	context= {'object_list': data,'object_list2': data_consejo,'object_list3': data_noticia}
	return render(request, 'inicio_paquetes.html', context)

def nuestros_paquetes(request):
	paquete = Listar("paquete")
	context= {'object_list': paquete}
	return render(request, 'nuestros_paquetes.html', context)


def calificar(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'calificar.html', dictionary)