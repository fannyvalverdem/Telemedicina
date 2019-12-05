from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm

#creating our forms
CHOICES=[
    (1,'Si'),
    (2,'No'),
]

DOC_ID=[
	(1,'Cedula'),
	(2,'Pasaporte'),
]

HORA=[
	(1,'01'),
	(2,'02'),
	(3,'03'),
	(4,'04'),
	(5,'05'),
	(6,'06'),
	(7,'07'),
	(8,'08'),
	(9,'09'),
	(10,'10'),
	(11,'11'),
	(12,'12'),
	(13,'13'),
	(14,'14'),
	(15,'15'),
	(16,'16'),
	(17,'17'),
	(18,'18'),
	(19,'19'),
	(20,'20'),
	(21,'21'),
	(22,'22'),
	(23,'23'),
	(0,'00'),
]

MINUTOS_CITAS=[
	(1,'00'),
	(2,'15'),
	(3,'30'),
	(4,'45'),
]


MINUTOS=[
	(0,'00'),
	(5,'05'),
	(10,'10'),
	(15,'15'),
	(20,'20'),
	(25,'25'),
	(30,'30'),
	(35,'35'),
	(40,'40'),
	(45,'45'),
	(50,'50'),
	(55,'55'),
]

ZONE=[
	(1,'am'),
	(2,'pm'),
]

class SignupForm(forms.Form):
	email = forms.EmailField(label='',max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))

class PersonaForm(forms.Form):
	name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
	apellido = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
	phone = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
	
class RegistroForm(UserCreationForm):
	class Meta:
		model = Usuario
		fields = ['username', 'email', 'password1', 'password2']
		
	# name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
	# apellido = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
	# phone = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
	email = forms.EmailField(label='',max_length=100, widget= forms.EmailInput(attrs={'placeholder':'Email'}))
	username = forms.EmailField(label='',max_length=100, widget= forms.EmailInput(attrs={'placeholder':'Username'}))
	password1 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))
	password2 = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))
	# password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))
	
class PaqueteForm(forms.Form):
	nombre=forms.CharField(label='Nombre: ',max_length=100,widget=forms.TextInput())
	precio=forms.FloatField(label='Precio: ')
	especialidad=forms.ModelChoiceField(label='Especialidad',queryset=Especialidad.objects.all(),required=False)
	descripcion=forms.CharField(label='Descripcion del Paquete: ', widget=forms.Textarea())
	duracion=forms.IntegerField(label='Duración de paquetes: ')

class TarifaForm(forms.Form):
	nombre=forms.CharField(label='Nombre: ',max_length=100,widget=forms.TextInput())
	precio=forms.FloatField(label='Precio: ')
	descripcion=forms.CharField(label='Descripcion de la Tarifa: ', widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))

class DoctorForm(forms.Form):
	name = forms.CharField(label='Nombre:',max_length=100,widget=forms.TextInput())
	apellido = forms.CharField(label='Apellido:',max_length=100,widget=forms.TextInput())
	documento_id=forms.ChoiceField(required=False, choices=DOC_ID, label='Tipo de Documento:')
	num_doc=forms.CharField(label='Numero de Documento:',max_length=100,widget=forms.TextInput())
	email = forms.EmailField(label='Email:',max_length=100, widget= forms.EmailInput())
	password = forms.CharField(label='Contraseña:',widget=forms.PasswordInput())
	direccion=forms.CharField(label='Dirección:',max_length=100,widget=forms.TextInput())
	ciudad=forms.CharField(label='Ciudad:',max_length=100,widget=forms.TextInput())
	phone = forms.CharField(label='Teléfono:',max_length=100,widget=forms.TextInput())
	celular=forms.CharField(label='Celular:',max_length=100,widget=forms.TextInput())
	especialidad=forms.ModelChoiceField(required=False,queryset=Especialidad.objects.all(), label='Especialidad:')
	tarifa=forms.ModelChoiceField(required=False,queryset=Tarifa.objects.all(), label='Tarifa:')
	licencia_med=forms.CharField(label='Número de licencia médica:',max_length=100,widget=forms.TextInput())
	#foto=forms.FileField(label='Foto:')
	#documentos=forms.FileField(label='Documentos:',widget=forms.ClearableFileInput(attrs={'multiple': True}))


class HorarioForm(forms.Form):
	mensual=forms.BooleanField(required=False)
	lunes=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction()'}))
	martes=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction2()'}))
	miercoles=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction3()'}))
	jueves=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction4()'}))
	viernes=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction5()'}))
	sabado=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction6()'}))
	domingo=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction7()'}))
	hora_entrada_lunes=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_entrada_lunes=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_salida_lunes=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_salida_lunes=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_entrada_martes=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_entrada_martes=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_salida_martes=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_salida_martes=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_entrada_miercoles=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_entrada_miercoles=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_salida_miercoles=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_salida_miercoles=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_entrada_jueves=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_entrada_jueves=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_salida_jueves=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_salida_jueves=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_entrada_viernes=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_entrada_viernes=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_salida_viernes=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_salida_viernes=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_entrada_sabado=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_entrada_sabado=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_salida_sabado=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_salida_sabado=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_entrada_domingo=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_entrada_domingo=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	hora_salida_domingo=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos_salida_domingo=forms.ChoiceField(required=True, choices=MINUTOS,label='')

class CitasForms(forms.Form):
	especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all())
	#especialidad=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Especialidad'}))
	date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
	hora=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos=forms.ChoiceField(required=True, choices=MINUTOS_CITAS,label='')
	zona=forms.ChoiceField(required=True, choices=ZONE,label='')

class Especialidades(forms.Form):
	especialidad=forms.CharField(label='Especialidad:',max_length=100,widget=forms.TextInput())

class MatchEspecialidad(forms.Form):
	opciones = forms.ModelMultipleChoiceField(
                       widget = forms.CheckboxSelectMultiple,
                       queryset = Doctor.objects.all()
               )

class RecetaForm(forms.Form):
	name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
	apellido = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
	cedula=forms.CharField(label='Cedula:',max_length=100,widget=forms.TextInput())
	especialidad = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Especialidad'}))
	descripcion=forms.CharField(label='Descripcion de la receta: ', widget=forms.Textarea(attrs={'cols': 10, 'rows': 5}))
	medicamentos = forms.ModelMultipleChoiceField(
                       widget = forms.SelectMultiple,
                       queryset = Medicamento.objects.all()
               )

class EditarPerfilForm(forms.Form):
	nombres = forms.CharField(required=False,label='Nombre',max_length=100,widget=forms.TextInput())
	apellido = forms.CharField(required=False,label='Apellido',max_length=100,widget=forms.TextInput())
	tipo_doc=forms.ChoiceField(required=False, choices=DOC_ID, label='Tipo de Documento:')
	num_doc=forms.CharField(required=False,label='Cedula:',max_length=100,widget=forms.TextInput())
	genero=forms.CharField(required=False,label='Género:',max_length=100,widget=forms.TextInput())
	edad=forms.IntegerField(required=False,label='Edad:')
	fecha_nac=forms.DateField(required=False,label='Fecha de Nacimiento:')
	pais=forms.CharField(required=False,label='País:',max_length=100,widget=forms.TextInput())
	ciudad=forms.CharField(required=False,label='Ciudad:',max_length=100,widget=forms.TextInput())
	direccion=forms.CharField(required=False,label='Dirección:',max_length=100,widget=forms.TextInput())

class ImageForm(forms.ModelForm):
   class Meta:
      model = Publicidad
      fields = ['imagen','name','dueno','precio','telefono','ciudad','direccion']