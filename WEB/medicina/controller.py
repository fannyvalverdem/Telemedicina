import requests,json

def Add(entidad,registro):
	response=requests.post('http://127.0.0.1:8000/api/'+entidad+'/',registro)
	return response

def Listar(entidad):
	response = requests.get('http://127.0.0.1:8000/api/'+entidad+'/')
	data = response.json()
	return data