import requests

# Usamos JSONPlaceholder, un servicio de API falso para pruebas y prototipos
url = 'https://jsonplaceholder.typicode.com/posts'

try:
    # Realizamos la solicitud GET
    response = requests.get(url)
    # Si la solicitud es exitosa, response.status_code será 200
    if response.status_code == 200:
        data = response.json()
        # Imprimimos los primeros 5 posts para verificar que la respuesta es correcta
        print(data[:5])
    else:
        print(f"Error en la solicitud: {response.status_code}")
except requests.exceptions.TooManyRedirects:
    print("Demasiadas redirecciones. Por favor, verifica la URL o reduce el número de redirecciones permitidas.")
except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")
