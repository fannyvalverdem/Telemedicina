from django import forms
from .models import *

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
]

MINUTOS_CITAS=[
	(1,'00'),
	(2,'15'),
	(3,'30'),
	(4,'45'),
]


MINUTOS=[
	(1,'00'),
	(2,'05'),
	(3,'10'),
	(4,'15'),
	(5,'20'),
	(6,'25'),
	(7,'30'),
	(8,'35'),
	(9,'40'),
	(10,'45'),
	(11,'50'),
	(12,'55'),
]

ZONE=[
	(1,'am'),
	(2,'pm'),
]

class SignupForm(forms.Form):
	email = forms.EmailField(label='',max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))

class RegistroForm(forms.Form):
	name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
	apellido = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
	phone = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
	email = forms.EmailField(label='',max_length=100, widget= forms.EmailInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))

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
	especialidad=forms.ChoiceField(required=False, choices=DOC_ID, label='Especialidad:')
	tarifa=forms.ChoiceField(required=False, choices=DOC_ID, label='Tarifa:')
	licencia_med=forms.CharField(label='Número de licencia médica:',max_length=100,widget=forms.TextInput())
	foto=forms.FileField(label='Foto:')
	documentos=forms.FileField(label='Documentos:',widget=forms.ClearableFileInput(attrs={'multiple': True}))


class HorarioForm(forms.Form):
	mensual=forms.BooleanField(required=False)
	lunes=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction()'}))
	martes=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction2()'}))
	miercoles=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction3()'}))
	jueves=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction4()'}))
	viernes=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction5()'}))
	sabado=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction6()'}))
	domingo=forms.BooleanField(required=False,widget=forms.CheckboxInput(attrs={'onclick':'myFunction7()'}))
	hora=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos=forms.ChoiceField(required=True, choices=MINUTOS,label='')
	zona=forms.ChoiceField(required=True, choices=ZONE,label='')

class CitasForms(forms.Form):
	especialidad = forms.ModelChoiceField(queryset=Especialidad.objects.all())
	#especialidad=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Especialidad'}))
	date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
	hora=forms.ChoiceField(required=True, choices=HORA,label='')
	minutos=forms.ChoiceField(required=True, choices=MINUTOS_CITAS,label='')
	zona=forms.ChoiceField(required=True, choices=ZONE,label='')