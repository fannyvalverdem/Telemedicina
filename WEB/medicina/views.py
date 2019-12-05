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
from .controller import Listar, Add
import requests,json
from .utility import *
from django.http import QueryDict
from django.shortcuts import redirect
from django.contrib import messages
from .controller import zoom_auth

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

def zoom(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'zoom.html', dictionary)

def citas_medico(request):
	dictionary = dict(request=request) 
	dictionary.update(csrf(request)) 
	return render(request,'citas_medico.html', dictionary)

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
			return HttpResponseRedirect('/imagenes/publicidad/')

def perfil(request):
	current_user = request.user
	user_ac_id=current_user.id
	user_ac_person_id=current_user.persona_id.id
	persona=Persona.objects.get(id=user_ac_person_id)
	usuario=Usuario.objects.get(id=user_ac_id)
	return render(request,"perfil.html",{'persona':persona,'usuario':usuario})

def editar_perfil(request):
	if request.method == 'POST':
		print("POST")
	form= EditarPerfilForm(request.POST)
	if form.is_valid():
		print("VALIDO")
		current_user = request.user
		user_ac_id=current_user.id
		user_ac_person_id=current_user.persona_id.id
		persona=Persona.objects.get(id=user_ac_person_id)
		usuario=Usuario.objects.get(id=user_ac_id)

		if form.cleaned_data['nombres']:
			persona.nombre=form.cleaned_data['nombres']
			persona.save()

		if form.cleaned_data['apellido']:
			persona.apellido=form.cleaned_data['apellido']
			persona.save()

		if form.cleaned_data['tipo_doc']:
			tipo=form.cleaned_data['tipo_doc']
			if tipo=="1":
				persona.tipo_documento="Cedula"
			else:
				persona.tipo_documento="Pasaporte"
			persona.save()

		if form.cleaned_data['num_doc']:
			persona.numero_documento=form.cleaned_data['num_doc']
			persona.save()

		if form.cleaned_data['genero']:
			persona.sexo=form.cleaned_data['genero']
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
	else:
		form=EditarPerfilForm()
	
	return render(request, 'editar_perfil.html', {'form':form});

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
	list_especialidades = Especialidad.objects.values_list('nombre',flat=True)
	
	if request.method == 'POST':
		print("POST")
		
	form = CitasForms(request.POST)
	if form.is_valid():
		dictionary = dict(request=request) 
		dictionary.update(csrf(request)) 
		text = form.cleaned_data['especialidad']
		console.log(text)
		d = {'form':form, 'text':text}
		
		return render(request,'agendar_cita.html', d)
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
	        	print("NO VALIDO")
	        	msg_to_html = custom_message('Invalid Credentials', TagType.danger)
	        	messages.error(request, 'Nombre de usuario o contraseña incorrecto')
	        	dictionary = dict(request=request, messages = msg_to_html)
	        	dictionary.update(csrf(request))
	        return render(request,'inicio_sesion.html', {'form':form})

def crear_cita(request):
	return redirect('index_paciente')

def auth_zoom(request):
	zoom_auth()
	request.session["code"] = request.GET.get("code", "NO CODE")
	return HttpResponse('Hola Mundo')

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