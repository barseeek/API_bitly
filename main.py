import requests
import os
from dotenv import load_dotenv
from urllib.parse import urlparse


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
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


def is_bitlink(token, url):
    header = {"Authorization": f"Bearer {os.environ['BITLY_TOKEN']}"}
    parsed_url = urlparse(url)
    bitlink = parsed_url.netloc + parsed_url.path
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}", headers=header)
    return response.ok


def shorten_link(token, url):
    header = {"Authorization": f"Bearer {os.environ['BITLY_TOKEN']}"}
    long_url = {"long_url": url}
    response = requests.post("https://api-ssl.bitly.com/v4/bitlinks", headers=header, json=long_url)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, url):
    header = {"Authorization": f"Bearer {os.environ['BITLY_TOKEN']}"}
    parsed_url = urlparse(url)
    bitlink = parsed_url.netloc + parsed_url.path
    params = {
        "unit": "day",
        "units": -1}
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
                            headers=header, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    main()
