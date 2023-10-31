import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse

load_dotenv()
header = {"Authorization": f"Bearer {os.environ['BITLY_TOKEN']}"}


def is_bitlink(url):
    parsed = urlparse(url)
    bitlink = parsed.netloc + parsed.path
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}", headers=header)
    return response.ok


def shorten_link(url):
    data = {"long_url": url}
    response = requests.post("https://api-ssl.bitly.com/v4/bitlinks", headers=header, json=data)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(url):
    parsed = urlparse(url)
    bitlink = parsed.netloc + parsed.path
    params = {
        "unit": "day",
        "units": -1}
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
                            headers=header, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    url = input("Введите URL\n")
    try:
        if is_bitlink(url):
            print('Вы ввели действующий битлинк, считаю клики...')
            click_counter = count_clicks(url)
            print('Количество кликов по ссылке {0} = {1}'.format(url, click_counter))
        else:
            print('Вы ввели URL, создаю битлинк...')
            bitlink = shorten_link(url)
            print('Битлинк для адреса {0}: {1}'.format(url, bitlink))
    except requests.exceptions.RequestException() as err:
        exit('Error, check input link. Error message: {0}'.format(err))
