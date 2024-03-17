"""Módulo con funciones necesarias para encontrar características en texto."""

# External libraries
import re

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


def find_mentions(comment: str) -> list:
    """Encuentra todas las menciones de usuarios en un comentario.

    Args:
        comment (str): El comentario en el que se buscarán las menciones.

    Returns:
        list: Una lista de nombres de usuario mencionados en el comentario.

    """
    regex = re.findall(r'@(\w+)', comment)

    return regex

