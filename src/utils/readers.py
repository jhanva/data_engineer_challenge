"""Módulo con las funciones necesarias para realizar lectura de archivos."""

# External libraries
from datetime import datetime
from typing import Union

import orjson
import pandas as pd


def read_json_file(
    path: str, transformation: bool = False
) -> Union[pd.DataFrame, list]:
    """Lee un archivo JSON y lo convierte en un DataFrame de Pandas.

    Args:
        path (str): Ruta del archivo JSON.
        transformation (bool): Indica si se quiere hacer otra transformación.

    Returns:
        pd.DataFrame: DataFrame que contiene los datos del archivo JSON.

    """
    tmp = []

    if transformation:
        with open(path, mode="rb") as file:
            for line in file:
                data = orjson.loads(line)
                user = data['user']['username']
                date_str = data['date'].split('T')[0]
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                tmp.append((date, user))
        data = tmp
    else:
        with open(path, mode="rb") as file:
            for line in file:
                tmp.append(orjson.loads(line))

        data = pd.DataFrame(tmp)
        data['user'] = data['user'].apply(lambda x: x['username'])
        data['date'] = pd.to_datetime(data['date'])

    return data
