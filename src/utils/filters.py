"""Módulo con funciones necesarias para encontrar emojis en texto."""

# External libraries
from emoji import emoji_list


def count_emoji(string: str) -> list:
    """Cuenta la cantidad de emojis en una cadena de texto.

    Args:
        string (str): Cadena de texto que se analizará para contar emojis.

    Returns:
        list: Una lista de emojis encontrados en la cadena.

    """
    result = [dic.get('emoji') for dic in emoji_list(string)]

    return result
