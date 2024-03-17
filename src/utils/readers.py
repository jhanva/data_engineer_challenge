"""Módulo con las funciones necesarias para realizar lectura de archivos."""

# External libraries
from datetime import datetime
from typing import Union

import orjson
import pandas as pd


def read_json_file(
    path: str, transformation: str = 'dataframe'
) -> Union[pd.DataFrame, list]:
    """Lee un archivo JSON y lo convierte en un DataFrame de Pandas.

    Args:
        path (str): Ruta del archivo JSON.
        transformation (bool): Indica si se quiere hacer otra transformación.

    Returns:
        pd.DataFrame: DataFrame que contiene los datos del archivo JSON.

    """
    tmp = []

    if transformation == 'date_list':
        with open(path, mode="rb") as file:
            for line in file:
                data = orjson.loads(line)
                user = data['user']['username']
                date_str = data['date'].split('T')[0]
                date = datetime.strptime(date_str, '%Y-%m-%d').date()
                tmp.append((date, user))
        data = tmp

    elif transformation == 'content_list':
        with open(path, mode="rb") as file:
            for line in file:
                record = orjson.loads(line)
                user = record['user']['username']
                date = record['date']
                content = record['content']
                tmp.append((user, date, content))
        data = tmp

    elif transformation == 'dataframe':
        with open(path, mode="rb") as file:
            for line in file:
                tmp.append(orjson.loads(line))
        data = pd.DataFrame(tmp)
        data['user'] = data['user'].apply(lambda x: x['username'])
        data['date'] = pd.to_datetime(data['date'])

    else:
        msg = (
            'Solo se permite transformaciones de tipo '
            'dataframe, date_list y content_list'
        )
        raise NotImplementedError(msg)

    return data
