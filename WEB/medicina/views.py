from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.template.context_processors import csrf
from django.contrib.auth import logout
from django.contrib.auth import authenticate 
from django.http import HttpResponseRedirect
from django.urls import reverse 
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import login as auth_login
from .forms import *
from .models import *
from django.contrib.auth.models import User
from .controller import Listar, Add
import requests,json
from .utility import *
from django.http import QueryDict
from .models import Persona, Paquete,Dias,Doctor
from django.shortcuts import redirect

# Create your views here.
@csrf_exempt 
def base(request):
  dictionary = dict(request=request) 
  dictionary.update(csrf(request)) 
  return render(request,'base.html', dictionary)

def cerrar_sesion(request):
	logout(request)
	form = SignupForm(request.POST)
	return render(request, "inicio_sesion.html", {'form':form})

def inicio(request):
	if request.user.is_authenticated:
		return render(request, "index_paciente.html")
	
	if request.method == 'POST':
		print("POST")
	form = SignupForm(request.POST)
	
	#checking the form is valid or not 
	if form.is_valid():
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		return render(request,'index_paciente.html', dictionary)
	else:
	#creating a new form
		form = SignupForm()
			#returning form 
	return render(request, 'inicio_sesion.html', {'form':form});


def registro(request):
	if request.method == 'POST':
		print("POST")
	usuario=Listar("usuario")
	persona=Listar("personas")
	context= {'usuario':usuario,'persona':persona}
	form = RegistroForm(request.POST)
	print("<<<<<<<<<<<<<<<<<<")
	#checking the form is valid or not 
	if form.is_valid():
		username =form.cleaned_data['email']
		email =form.cleaned_data['email']
		password = form.cleaned_data['password']
		nombre = form.cleaned_data['name']
		apellido = form.cleaned_data['apellido']
		telefono = form.cleaned_data['phone']
		print(username,email,password,nombre,apellido,telefono,"<###")
		persona=Persona(
			nombre=nombre,
			apellido=apellido,
			telefono=telefono,
		)
		persona.save()
		usuario=Usuario(
			username=username,
			email=email,
			password=password,
			persona_id=persona
		)
		usuario.save()
		user = User.objects.create_user(username=email,email=email,password=password)
		user = authenticate(username=username, password=password)
		auth_login(request=request, user=user)
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
		form = RegistroForm()
			#returning form 
	return render(request, 'registro.html', {'form':form});

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

def confirmacion_cita(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'confirmar_cita.html', dictionary)

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

		paquete=Paquete(
			nombre=nombre,
			precio=precio,
			descripcion=descripcion,
			especialidad=especialidad,
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
		insertartarifa={"nombre":str(nombre),"descripcion":str(descripcion),"precio":float(precio)}
		Add('tarifas',insertartarifa)
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

		user.save()

		User.objects.create_user(username=email,email=email,password=password)

		doc=Doctor(
			identificador_medico=licencia_med,
			user_id=user,
			especialidad=especialidad
		)

		doc.save()
		return redirect('ing-horario')
	else:
	#creating a new form
		form = DoctorForm()
			#returning form 
	return render(request, 'ingresar_medico.html', {'form':form});

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

		return redirect('index_admin')
	else:
	#creating a new form
		form = HorarioForm()
			#returning form 
	return render(request, 'ingresar_horario_medico.html', {'form':form});


def agendar_cita(request):
	list_especialidades = Especialidad.objects.all()
	
	if request.method == 'POST':
		print("POST")
	form = CitasForms(request.POST)
	if form.is_valid():
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		text = form.cleaned_data['especialidad']
		d = {'form':form, 'text':text}
		
		return render(request,'seleccionar_medico.html', d)
	else:
	#creating a new form
		form = CitasForms()
			#returning form 
	context = {'especialidades': list_especialidades, 'form':form}
	return render(request, 'agendar_cita.html', context );

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
	        if user is not None:
	        	auth_login(request=request,user=user)
	        	response_doctor = requests.get('http://127.0.0.1:8000/api/doctor/')
	        	data_doctor = response_doctor.json()
	        	response_admin = requests.get('http://127.0.0.1:8000/api/administrador/')
	        	data_admin = response_admin.json()
	        	for i in range(0,len(data_doctor)):
	        		print(data_doctor[i]['user_id']['email'])
	        		if username==str(data_doctor[i]['user_id']['email']) and password==str(data_doctor[i]['user_id']['password']):
	        			return redirect('index_medico')
	        	for i in range(0,len(data_admin)):
	        		if username==str(data_admin[i]['user_id']['email']) and str(password==data_admin[i]['user_id']['password']):
	        			return redirect('index_admin')
	        	
	        	return redirect('index_paciente')


	        else:
	        	form = SignupForm()
	        	msg_to_html = custom_message('Invalid Credentials', TagType.danger)
	        	dictionary = dict(request=request, messages = msg_to_html)
	        	dictionary.update(csrf(request))
	        return render(request,'inicio_sesion.html', {'form':form})
