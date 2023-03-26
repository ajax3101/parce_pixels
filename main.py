import os
import requests
from tqdm import tqdm
from dotenv import load_dotenv
import json
import math



load_dotenv()


def scrap_pexels(query=''):
    """Your API Key"""

    headers = {"Authorization": f'{os.getenv("API_KEY")}'}
    print(headers)
    query_str = f'https://api.pexels.com/v1/search?query={query}&per_page=40&orientation=landscape'

    response = requests.get(url=query_str, headers=headers, proxies=None)

    if response.status_code != 200:
        return f'Ошибка: Статус кода - {response.status_code}, {response.json()}'


def main():
    scrap_pexels(query='parsing')


if __name__ == '__main__':
    main()
