"""Módulo con las funciones necesarias para realizar lectura de archivos."""

# External libraries
import orjson
import pandas as pd


def read_json_file(path: str) -> pd.DataFrame:
    """Lee un archivo JSON y lo convierte en un DataFrame de Pandas.

    Args:
        path (str): Ruta del archivo JSON.

    Returns:
        pd.DataFrame: DataFrame que contiene los datos del archivo JSON.

    """
    tmp = []
    with open(path, mode="rb") as file:
        for line in file:
            tmp.append(orjson.loads(line))

    data = pd.DataFrame(tmp)
    data['user'] = data['user'].apply(lambda x: x['username'])
    data['date'] = pd.to_datetime(data['date'])

    return data
