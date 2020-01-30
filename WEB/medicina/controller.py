import requests,json
from django.shortcuts import redirect
from .models import *
from datetime import date, timedelta
import time
import datetime

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
	#print(response.text)
	data_json=response.json()
	return data_json


def add_meeting(usuario,nombre,fecha,hora,dia,token):
	url = "https://api.zoom.us/v2/users/"+usuario+"/meetings"
	payload = "{\"topic\":\""+nombre+"\",\"type\":\"8\",\"start_time\":\""+fecha+"T"+hora+"\",\"duration\":\"15\",\"timezone\":\"America/Bogota\",\"recurrence\":{\"type\":\"2\",\"repeat_interval\":\"1\",\"weekly_days\":\""+dia+"\",\"end_times\": \"12\"},\"settings\":{\"join_before_host\":\"true\",\"auto_recording\":\"local\",\"use_pmi\":\"true\"}}"
 
	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer "+token+""
	    }

	response = requests.request("POST", url, data=payload, headers=headers)


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
    
def guardar_citas(email,token,doctor):
	data=listar_meeting(email,token)
	#print(data)
	meet=data['meetings']
	#print(meet)

	for m in meet:
		m_id=m['id']
		m_url=m['join_url']
		m_duration=m['duration']
		m_starttime=m['start_time']
		fecha_hora=m_starttime.split('T')
		fecha=fecha_hora[0]
		hora=(fecha_hora[1].split('Z'))[0]
		fecha_completa=fecha+' '+hora
		horas_resta=datetime.timedelta(hours=5)
		prueba_hora=datetime.datetime.strptime(fecha_completa, '%Y-%m-%d %H:%M:%S')
		actual=prueba_hora - horas_resta
		m_fecha=actual.date()
		m_hora=actual.time()
		meeting=Citas_Medico(
			m_id=m_id,
			m_url=m_url,
			m_duration=m_duration,
			fecha=m_fecha,
			hora=m_hora,
			doctor=doctor
		)

		meeting.save()


def crear_citas(token,horarios,email,doctor):
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

	guardar_citas(email,token,doctor)

def facturacion(tarifa,nombre,apellido,cedula):
	today = date.today()
	fecha = today.strftime("%Y/%m/%d")
	strtarifa=str(tarifa)

	data="{\"api_key\":\"API_1_1_5a4492f2d5137\",\"codigoDoc\":\"01\",\"emisor\":{fecha_emision\":\""+fecha+"\"},\"comprador\":{\"tipo_identificacion\":\"05\",\"identificacion\":\""+cedula+"\",\"razon_social\":\""+nombre+" "+apellido+"\"},\"items\":[{\"codigo_principal\":\"900053\",\"descripcion\":	\"Servicio Medico\",\"tipoproducto\":2,\"tipo_iva\":2,\"precio_unitario\":"+strtarifa+",\"cantidad\":1}],\"pagos\":[{\"tipo\":\"19\"}],}"

	response=requests.post('https://azur.com.ec/plataforma/api/v2/factura/emision',data)
	print(response)