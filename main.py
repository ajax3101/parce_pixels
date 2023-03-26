import requests
from tqdm import tqdm
from dotenv import load_dotenv
import json
import math
import os


load_dotenv()


def scrap_pexels(query=""):
    """Your API Key
    Keyword arguments:
    argument -- description
    Return: return_description
    """

    headers = {"Authorization:" f'{os.getenv("API_KEY")}'}
    query_str = f"https://api.pexels.com/v1/search?query={query}&per_page=40&orientation=landscape"

    response = requests.get(url=query_str, headers=headers)

    if response.status_code != 200:
        return f"Ошибка: Статус кода - {response.status_code}, {response.json()}"


def main():
    scrap_pexels(query="hacker")


if __name__ == "__main__":
    main()
