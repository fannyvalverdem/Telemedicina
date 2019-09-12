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

def add_registro(request): 
	usuario=Listar("usuario")
	persona=Listar("personas")
	context= {'usuario': usuario, 'personas':persona}
	if form.is_valid():
	        username =form.cleaned_data['email']
	        email =form.cleaned_data['email']
	        password = form.cleaned_data['password']
	        nombre = form.cleaned_data['nombre']
	        apellido = form.cleaned_data['apellido']
	        telefono = form.cleaned_data['telefono']
	if request.method == "POST":
	  	insertarpersona={"nombre": nombre, "apellido":apellido, "telefono":telefono}
	  	Add(insertarpersona)
	  	insertarusuario = {"email": email, "username":username, "password":password, "persona_id":insertarpersona}
	  	Add(insertarusuario)
	  	return redirect('index_paciente')  
	else:    
		return render(request, 'add.html', context)

def registro(request):
	if request.method == 'POST':
		print("POST")
	usuario=Listar("usuario")
	context= {'usuario': usuario}
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
		#user = User.objects.create_user(username=email,email=email,password=password)
		insertarpersona={"nombre": str(nombre), "apellido":str(apellido), "telefono":str(telefono)}
		insertarusuario = {"email": str(email), "username":str(username), "password":str(password), "persona_id":insertarpersona}
		Add('usuario',insertarusuario)
		#print(user,"<<<<<<<<<<<<<<<<<<")
		#user = authenticate(username=username, password=password)
		#auth_login(request=request, user=user)
		dictionary = dict(request=request) 
		dictionary.update(csrf(request))
		return render(request,'index_paciente.html', context)
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
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		return render(request,'tarifas.html', dictionary)
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
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		return render(request,'tarifas.html', dictionary)
	else:
	#creating a new form
		form = TarifaForm()
			#returning form 
	return render(request, 'ingresar_tarifa.html', {'form':form});

def ingresar_medico(request):
	if request.method == 'POST':
		print("POST")
	form = DoctorForm(request.POST)
	
	#checking the form is valid or not 
	if form.is_valid():
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		return render(request,'index_admin.html', dictionary)
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
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		return render(request,'index_admin.html', dictionary)
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
	        	for i in range(0,len(data_doctor)):
	        		if username==data_doctor[i]['user_id']['email'] and password==data_doctor[i]['user_id']['password']:
	        			return render(request, "index_doctor.html",{'form':form})
	        		else:
	        			return render(request, "index_paciente.html",{'form':form})
	        else:
	        	msg_to_html = custom_message('Invalid Credentials', TagType.danger)
	        	dictionary = dict(request=request, messages = msg_to_html)
	        	dictionary.update(csrf(request))
	        return render(request,'inicio_sesion.html', dictionary)
