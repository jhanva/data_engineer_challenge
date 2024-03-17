"""Módulo con funciones para hacer requests."""

# External libraries
import requests


def post_request(data: dict, url: str) -> None:
    """Realiza una solicitud POST a una URL especificada con los datos
     proporcionados en un archivo YAML.

    Args:
        data (dict): Datos a enviar.
        url (str): La URL a la que se enviará la solicitud POST.

    Returns:
        None

    Raises:
        FileNotFoundError: Si no se encuentra el archivo YAML especificado.
        requests.RequestException: Si la solicitud POST no se puede completar
         correctamente.

    """
    try:
        response = requests.post(url, json=data)

        if response.status_code == 200:
            print('Solicitud POST exitosa.')
        else:
            print(
                f'Error al realizar la solicitud POST: {response.status_code}'
            )

    except requests.RequestException as e:
        print('Error al realizar la solicitud POST:', e)
