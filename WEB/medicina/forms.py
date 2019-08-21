from django import forms

#creating our forms
CHOICES=[
    (1,'Si'),
    (2,'No'),
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
	especialidad=forms.CharField(label='Especialidad: ',max_length=100,widget=forms.TextInput())
	descripcion=forms.CharField(label='Descripcion del paquete: ', widget=forms.Textarea())
	citas=forms.IntegerField(label='Numero de citas: ')
	examenes=forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=CHOICES)