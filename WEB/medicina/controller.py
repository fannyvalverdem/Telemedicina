import requests,json

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


def add_meeting(usuario,nombre,fecha,hora,token):
	url = "https://api.zoom.us/v2/users/"+usuario+"/meetings"

	payload = "{\"topic\":\""+nombre+"\",\"type\":\"2\",\"start_time\":\"["+fecha+"-"+hora+"]\",\"duration\":\"30\",\"timezone\":\"GMT-5:00\",\"settings\":{\"host_video\":\"true\",\"participant_video\":\"false\",\"join_before_host\":\"true\",\"auto_recording\":\"local\"}}"
	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer "+token+""
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)


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