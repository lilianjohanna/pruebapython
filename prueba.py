import requests
import urllib.parse

URL = 'https://jsonplaceholder.typicode.com/users?'
params = {
  'id': 7,
  'username': 'Delphine'
}
response = requests.get(URL, params=params)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)