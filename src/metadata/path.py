"""Módulo de metadata con las definiciones de las rutas del preyecto."""

# External libraries
import os


class Path:
    """Objeto que almacena las rutas necesarias para el proyecto."""

    data = os.path.join('data')
    """Ruta a los datos necesarios para ejecutar el proyecto."""

    info_proyecto = os.path.join('input', 'challenge.yaml')
    """Archivo YAML con los datos del desafio."""

    tweets = os.path.join('data', 'farmers-protest-tweets-2021-2-4.json')
    """Ruta al archivo JSON con tweets."""
