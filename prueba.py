import requests
print("Ingrese el id")
id=input()
print("Ingrese el correo electrónico")
nombre=input()
URL = 'https://jsonplaceholder.typicode.com/comments?postId='+id+'&email='+nombre
response = requests.get(URL)

if response.status_code == 200:
    print('Registro encontrado:')
    print('Data:', response.json())
else:
    print('Error en la solicitud, detalles:', response.text)