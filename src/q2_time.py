"""Script con solución al problema del top 10 emojis mas usados."""

# External libraries
from typing import List, Tuple

# Own libraries
from src.utils import count_emoji, read_json_file


def q2_time(file_path: str) -> List[Tuple[str, int]]:
    """Lee un archivo JSON y devuelve una lista de tuplas con los 10 emojis
     más frecuentes y su conteo.

    Args:
        file_path (str): Ruta del archivo JSON que contiene los datos.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas donde cada tupla contiene
         un emoji y su conteo correspondiente.

    """
    data = read_json_file(file_path)

    emojis = data['content'].apply(count_emoji)

    df_exploded = emojis.explode('content')

    data_serie = df_exploded.value_counts().head(10)

    date_list = list(zip(data_serie.index, data_serie.tolist()))

    return date_list
