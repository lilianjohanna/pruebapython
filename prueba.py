import requests
import urllib.parse

id='4'
nombre='eos est animi quis'
URL = 'https://jsonplaceholder.typicode.com/comments?postId='+id+'&name='+nombre
response = requests.get(URL)

if response.status_code == 200:
    print('Solicitud exitosa')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)