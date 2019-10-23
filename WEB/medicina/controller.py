import requests,json

def Add(entidad,registro):
	response=requests.post('http://127.0.0.1:8000/api/'+entidad+'/',registro)
	return response

def Listar(entidad):
	response = requests.get('http://127.0.0.1:8000/api/'+entidad+'/')
	data = response.json()
	return data

def listar_meeting(usuario):
	url = "https://api.zoom.us/v2/users/"+usuario+"/meetings"

	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ2ZXIiOiI2IiwiY2xpZW50SWQiOiJXZ0NvMk1vOFJrdXBrQUFOTThXeGRnIiwiY29kZSI6IlRtMjJjUTFwV25fSm5vcVVqZ2lRN2FicjA2UTAzb0tDdyIsImlzcyI6InVybjp6b29tOmNvbm5lY3Q6Y2xpZW50aWQ6V2dDbzJNbzhSa3Vwa0FBTk04V3hkZyIsImF1dGhlbnRpY2F0aW9uSWQiOiJhNDQ3MmEzZTYzMjk4M2YyZTgxNDdkYzAxYjEyNWNiYSIsImVudiI6W251bGxdLCJ1c2VySWQiOiJKbm9xVWpnaVE3YWJyMDZRMDNvS0N3IiwiZ3JvdXBOdW1iZXIiOjAsImF1ZCI6Imh0dHBzOi8vb2F1dGguem9vbS51cyIsImFjY291bnRJZCI6ImFhQ0hMWl9lUlVpT2NPX3VfR1RqNGciLCJuYmYiOjE1NzA3NTE4MzUsImV4cCI6MTU3MDc1NTQzNSwidG9rZW5UeXBlIjoiYWNjZXNzX3Rva2VuIiwiaWF0IjoxNTcwNzUxODM1LCJqdGkiOiI3ZmQ3ZTdkZi1kMWFjLTRhYjktYjMwNy0wMjA4OWEzNDg3MTYiLCJ0b2xlcmFuY2VJZCI6MH0.mSlmgHSk8HRp-tdCzUtb72ZEu7NxcgU8W378ih-gH6lGp-CCtrEawvi2MWtNnd1DRt19HvHQ4opbnvxjqeKxIA"
	    }
	
	querystring = {"page_number":"1","page_size":"30","type":"live"}

	response = requests.request("GET", url, headers=headers, params=querystring)


def add_meeting(usuario):
	url = "https://api.zoom.us/v2/users/"+usuario+"/meetings"

	#data.json
	payload = "{\"topic\":\"string\",\"type\":\"integer\",\"start_time\":\"string [date-time]\",\"duration\":\"integer\",\"timezone\":\"string\",\"password\":\"string\",\"agenda\":\"string\",\"recurrence\":{\"type\":\"integer\",\"repeat_interval\":\"integer\",\"weekly_days\":\"integer\",\"monthly_day\":\"integer\",\"monthly_week\":\"integer\",\"monthly_week_day\":\"integer\",\"end_times\":\"integer\",\"end_date_time\":\"string [date-time]\"},\"settings\":{\"host_video\":\"boolean\",\"participant_video\":\"boolean\",\"cn_meeting\":\"boolean\",\"in_meeting\":\"boolean\",\"join_before_host\":\"boolean\",\"mute_upon_entry\":\"boolean\",\"watermark\":\"boolean\",\"use_pmi\":\"boolean\",\"approval_type\":\"integer\",\"registration_type\":\"integer\",\"audio\":\"string\",\"auto_recording\":\"string\",\"enforce_login\":\"boolean\",\"enforce_login_domains\":\"string\",\"alternative_hosts\":\"string\",\"global_dial_in_countries\":[\"string\"]}}"

	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ2ZXIiOiI2IiwiY2xpZW50SWQiOiJXZ0NvMk1vOFJrdXBrQUFOTThXeGRnIiwiY29kZSI6IklYTFhKUDR5RnFfSm5vcVVqZ2lRN2FicjA2UTAzb0tDdyIsImlzcyI6InVybjp6b29tOmNvbm5lY3Q6Y2xpZW50aWQ6V2dDbzJNbzhSa3Vwa0FBTk04V3hkZyIsImF1dGhlbnRpY2F0aW9uSWQiOiIxZDhkMzBmMTU3NDc4YTdhMWM0OGU2MmEyZjg2YjU5MSIsImVudiI6W251bGxdLCJ1c2VySWQiOiJKbm9xVWpnaVE3YWJyMDZRMDNvS0N3IiwiZ3JvdXBOdW1iZXIiOjAsImF1ZCI6Imh0dHBzOi8vb2F1dGguem9vbS51cyIsImFjY291bnRJZCI6ImFhQ0hMWl9lUlVpT2NPX3VfR1RqNGciLCJuYmYiOjE1NzA3NTA5OTcsImV4cCI6MTU3MDc1NDU5NywidG9rZW5UeXBlIjoiYWNjZXNzX3Rva2VuIiwiaWF0IjoxNTcwNzUwOTk3LCJqdGkiOiIyNzQwNDg3NC03OWEyLTQ5NTAtOTE0MS1iMjE1MDkxMDNmY2UiLCJ0b2xlcmFuY2VJZCI6MH0.F4CWhKYTYQiQMemQfJvY9xcQEJTWkOO0yv74prN7EkhAEGIc79UzWy65WYiujHXr0vH_vmcGEcNOdGOq2UCzNg"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)


def add_user():
	url = "https://api.zoom.us/v2/users"

	payload = "{\"action\":\"create\",\"user_info\":{\"email\":\"dhjdfkghdskjf@fgkjfdlgjfkd.gh\",\"type\":1,\"first_name\":\"Terry\",\"last_name\":\"Jones\"}}"
	headers = {
	    'content-type': "application/json",
	    'authorization': "Bearer eyJhbGciOiJIUzUxMiJ9.eyJ2ZXIiOiI2IiwiY2xpZW50SWQiOiJXZ0NvMk1vOFJrdXBrQUFOTThXeGRnIiwiY29kZSI6IlRtMjJjUTFwV25fSm5vcVVqZ2lRN2FicjA2UTAzb0tDdyIsImlzcyI6InVybjp6b29tOmNvbm5lY3Q6Y2xpZW50aWQ6V2dDbzJNbzhSa3Vwa0FBTk04V3hkZyIsImF1dGhlbnRpY2F0aW9uSWQiOiJhNDQ3MmEzZTYzMjk4M2YyZTgxNDdkYzAxYjEyNWNiYSIsImVudiI6W251bGxdLCJ1c2VySWQiOiJKbm9xVWpnaVE3YWJyMDZRMDNvS0N3IiwiZ3JvdXBOdW1iZXIiOjAsImF1ZCI6Imh0dHBzOi8vb2F1dGguem9vbS51cyIsImFjY291bnRJZCI6ImFhQ0hMWl9lUlVpT2NPX3VfR1RqNGciLCJuYmYiOjE1NzA3NTE4MzUsImV4cCI6MTU3MDc1NTQzNSwidG9rZW5UeXBlIjoiYWNjZXNzX3Rva2VuIiwiaWF0IjoxNTcwNzUxODM1LCJqdGkiOiI3ZmQ3ZTdkZi1kMWFjLTRhYjktYjMwNy0wMjA4OWEzNDg3MTYiLCJ0b2xlcmFuY2VJZCI6MH0.mSlmgHSk8HRp-tdCzUtb72ZEu7NxcgU8W378ih-gH6lGp-CCtrEawvi2MWtNnd1DRt19HvHQ4opbnvxjqeKxIA"
	    }

	response = requests.request("POST", url, data=payload, headers=headers)

	print(response.text)