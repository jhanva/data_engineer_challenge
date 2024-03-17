"""Módulo con las funciones necesarias para realizar lectura de archivos."""

# External libraries
import os
import zipfile
from datetime import datetime
from typing import Union

import gdown
import orjson
import pandas as pd
import yaml


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


def download_and_extract_gdrive(file_id: str, target_dir: str) -> None:
    """Descarga un archivo de Google Drive y lo descomprime en un directorio
     especificado.

    Args:
        file_id (str): ID del archivo en Google Drive.
        target_dir (str): Directorio de destino para la descarga y extracción.

    Returns:
        None

    Raises:
        ValueError: Si el ID del archivo o el directorio de destino no son
         válidos.
        FileNotFoundError: Si el archivo descargado no se encuentra.

    """
    download_url = f'https://drive.google.com/uc?id={file_id}'

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    output_file = os.path.join(target_dir, 'archivo.zip')

    gdown.download(download_url, output_file, quiet=False)

    with zipfile.ZipFile(output_file, 'r') as zip_ref:
        zip_ref.extractall(target_dir)

    os.remove(output_file)

    print('Archivo descargado y descomprimido con éxito.')


def read_yaml(file_path: str) -> dict:
    """Lee un archivo YAML y devuelve su contenido como un diccionario.

    Args:
        file_path (str): Ruta del archivo YAML.

    Returns:
        dict: Contenido del archivo YAML como un diccionario.

    Raises:
        FileNotFoundError: Si no se encuentra el archivo YAML especificado.

    """
    try:
        with open(file_path, 'r') as file:
            yaml_data = yaml.safe_load(file)
        return yaml_data

    except FileNotFoundError:
        raise FileNotFoundError(
            f'No se encontró el archivo en la ruta especificada: {file_path}')
