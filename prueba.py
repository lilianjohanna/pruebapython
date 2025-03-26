import requests
import urllib.parse

params = {
  'id': 7,
  'username': 'Delphine'
}
URL = 'https://jsonplaceholder.typicode.com/users/'+urllib.parse.urlencode(params)
response = requests.get(URL, params=params)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)