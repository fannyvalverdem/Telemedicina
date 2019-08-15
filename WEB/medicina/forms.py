from django import forms

#creating our forms
class SignupForm(forms.Form):
	email = forms.EmailField(label='',max_length=100,widget= forms.EmailInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))

class RegistroForm(forms.Form):
	name = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Nombre'}))
	apellido = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Apellido'}))
	phone = forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'placeholder':'Telefono'}))
	email = forms.EmailField(label='',max_length=100, widget= forms.EmailInput(attrs={'placeholder':'Email'}))
	password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'placeholder':'Contrasena'}))