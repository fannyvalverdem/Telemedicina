import requests,json
from django.shortcuts import redirect

def Add(entidad,registro):
	response=requests.post('http://127.0.0.1:8000/api/'+entidad+'/',registro)
	return response

def Listar(entidad):
	response = requests.get('http://127.0.0.1:8000/api/'+entidad+'/')
	data = response.json()
	return data

def listar_meeting(usuario,token):
	url = "https://api.zoom.us/v2/users/"+usuario+"/meetings"

	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer "+token+""
	    }
	
	querystring = {"page_number":"1","page_size":"30","type":"upcoming"}

	response = requests.request("GET", url, headers=headers, params=querystring)
	print(response.text)


def add_meeting(usuario,nombre,fecha,hora,dia,token):
	url = "https://api.zoom.us/v2/users/"+usuario+"/meetings"
	print(">>>>>>>>>"+fecha)
	print(">>>>>>>>>"+hora)
	payload = "{\"topic\":\""+nombre+"\",\"type\":\"8\",\"start_time\":\""+fecha+"T"+hora+"\",\"duration\":\"15\",\"timezone\":\"America/Bogota\",\"recurrence\":{\"type\":\"2\",\"repeat_interval\":\"1\",\"weekly_days\":\""+dia+"\",\"end_times\": \"12\"},\"settings\":{\"join_before_host\":\"false\",\"auto_recording\":\"local\",\"use_pmi\":\"true\"}}"

	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer "+token+""
	    }

	response = requests.request("POST", url, data=payload, headers=headers)
	data_json=response.json()
	#print(response.text)
	return data_json


def get_meeting(id_cita,token):
	url = "https://api.zoom.us/v2/meetings/"+id_cita+""

	headers = {'authorization': "Bearer "+token+""
	}

	response = requests.request("GET", url, headers=headers)

	print(response.text)

def add_user(email,nombre,apellido,token):
	url = "https://api.zoom.us/v2/users"

	payload = "{\"action\":\"create\",\"user_info\":{\"email\":\""+email+"\",\"type\":1,\"first_name\":\""+nombre+"\",\"last_name\":\""+apellido+"\"}}"
	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer "+token+""
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)

def crear_citas(token,horarios,fecha,email):
	for horario in horarios:
		entrada=horario.hora_entrada
		salida=horario.hora_salida
		minutos=datetime.timedelta(minutes=15)
		actual=entrada
		dia=horario.dias.nombre
		dianum=0
		if dia=='Domingo':
			dianum='1'
		if dia=='Lunes':
			dianum='2'
		if dia=='Martes':
			dianum='3'
		if dia=='Miercoles':
			dianum='4'
		if dia=='Jueves':
			dianum='5'
		if dia=='Viernes':
			dianum='6'
		if dia=='Sabado':
			dianum='7'
		today = date.today()
		fecha = today.strftime("%Y-%m-%d")
		actualstr=actual.strftime("%H:%M:%S")
		add_meeting(email,'Cita',fecha,actualstr,dianum,token)
		while(actual!=salida):
			actual=(datetime.datetime.combine(datetime.date(1,1,1),actual) + minutos).time()
			stractual=actual.strftime("%H:%M:%S")
			add_meeting(email,'Cita',fecha,stractual,dianum,token)

def guardar_citas(email,token):
	data=listar_meeting(email,token)