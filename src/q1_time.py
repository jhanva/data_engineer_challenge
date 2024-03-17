"""Script con solución al problema del top 10 fechas donde hay más tweets."""

# External libraries
from datetime import datetime
from typing import List, Tuple

import pandas as pd

# Own libraries
from src.utils import read_json_file


def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    try:
        table = read_json_file(file_path)
    except FileNotFoundError:
        raise FileNotFoundError('El archivo especificado no se encuentra.')

    date = [pd.Grouper(key='date', freq='D')]
    aggregate = {'url': 'count', 'user': lambda x: x.value_counts().index[0]}
    table = table.groupby(date, as_index=False).agg(aggregate)

    table = table.sort_values(by='url', ascending=False)

    table['date'] = table['date'].apply(lambda x: x.date())

    date_list = list(zip(table['date'], table['user']))

    return date_list
