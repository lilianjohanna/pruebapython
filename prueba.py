import requests
import urllib.parse

URL = 'https://jsonplaceholder.typicode.com/users/9'
response = requests.get(URL)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)