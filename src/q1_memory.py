"""Script con solución al problema del top 10 fechas donde hay más tweets."""

# External libraries
from datetime import datetime
from typing import List, Tuple

# Own libraries
from src.utils import read_json_file


def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    """Lee un archivo JSON y devuelve una lista de tuplas que contiene la
     fecha y el usuario más activo para cada día.

    Args:
        file_path (str): Ruta del archivo JSON.

    Returns:
        List[Tuple[datetime.date, str]]: Lista de tuplas donde cada tupla
         contiene la fecha (como objeto datetime.date) y el usuario más activo
         para ese día.

    """
    data = read_json_file(file_path, transformation='date_list')

    user_counts = {}
    date_user = {}

    for date, user in data:
        if date not in date_user:
            date_user[date] = {}
        date_user[date][user] = date_user[date].get(user, 0) + 1

    for date, users in date_user.items():
        user_counts[date] = max(users, key=users.get)

    sorted_user_counts = sorted(
        user_counts.items(), key=lambda x: x[1], reverse=True
    )

    return sorted_user_counts
