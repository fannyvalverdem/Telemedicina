from django import forms

#creating our forms
CHOICES=[
    (1,'Si'),
    (2,'No'),
]

DOC_ID=[
	(1,'Cedula'),
	(2,'Pasaporte'),
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
	especialidad=forms.ChoiceField(required=False, choices=DOC_ID, label='Especialidad')
	descripcion=forms.CharField(label='Descripcion del paquete: ', widget=forms.Textarea())
	citas=forms.IntegerField(label='Numero de citas: ')
	examenes=forms.ChoiceField(required=False, choices=CHOICES)

class TarifaForm(forms.Form):
	nombre=forms.CharField(label='Nombre: ',max_length=100,widget=forms.TextInput())
	precio=forms.FloatField(label='Precio: ')

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
	documentos=forms.FileField(label='Documentos:')