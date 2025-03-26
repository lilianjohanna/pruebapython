import requests
import urllib.parse

parametro='1'
parametro2='5'
URL = 'https://jsonplaceholder.typicode.com/comments?postId='+parametro+'&id='+parametro2
response = requests.get(URL, parametro)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)