import requests
import urllib.parse

parametro = '8'
URL = 'https://jsonplaceholder.typicode.com/users/'+parametro
response = requests.get(URL, parametro)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)