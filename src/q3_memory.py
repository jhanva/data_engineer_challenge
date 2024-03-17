"""Script con solución al problema del top 10 usuarios influyentes."""

# External libraries
from typing import List, Tuple

# Own libraries
from src.utils import read_json_file


def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    """Lee un archivo JSON y devuelve una lista de tuplas con las 10 menciones
     de usuarios más frecuentes y su conteo.

    Args:
        file_path (str): Ruta del archivo JSON que contiene los datos.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas donde cada tupla contiene una
          mención de usuario y su conteo correspondiente.

    """
    data = read_json_file(file_path)

    mentions = data['content'].str.split().explode()

    mentions = mentions.str.extract(r'@(\w+)').dropna()[0]

    mentions = mentions.value_counts().head(10)

    date_list = list(zip(mentions.index, mentions.values))

    return date_list
