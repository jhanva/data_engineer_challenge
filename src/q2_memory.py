"""Script con solución al problema del top 10 emojis mas usados."""

# External libraries
from collections import Counter
from memory_profiler import profile
from typing import List, Tuple

# Own libraries
from src.utils import count_emoji, read_json_file


@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    """Lee un archivo JSON y devuelve una lista de tuplas con los 10 emojis
     más frecuentes y su conteo.

    Args:
        file_path (str): Ruta del archivo JSON que contiene los datos.

    Returns:
        List[Tuple[str, int]]: Lista de tuplas donde cada tupla contiene un
        emoji y su conteo correspondiente.

    """
    data = read_json_file(file_path, transformation='content_list')

    emojis = Counter()

    for _, _, content in data:
        emojis.update(count_emoji(content))

    top_emojis = emojis.most_common(10)

    return top_emojis
