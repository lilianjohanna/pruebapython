import requests
import urllib.parse

parametro = 7
URL = 'https://jsonplaceholder.typicode.com/users'+urllib.parse.urlencode(parametro)
response = requests.get(URL, params=parametro)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)