"""Script para el envío del desafio."""

# Own libraries
from src.metadata.path import Path
from src.utils import read_yaml
from src.utils import post_request


if __name__ == '__main__':
    data = read_yaml(Path.info_proyecto)
    print(data)

    post_request(data=data, url='https://advana-challenge-check-api-cr-k4hdbggvoq-uc.a.run.app/data-engineer')
