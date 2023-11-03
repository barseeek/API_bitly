import requests
import os
import argparse
from dotenv import load_dotenv
from urllib.parse import urlparse


def main():
    load_dotenv()
    token = os.environ['BITLY_TOKEN']
    args = create_arg_parser()
    url = agrs.url
    try:
        if is_bitlink(token,url):
            print('Вы ввели действующий битлинк, считаю клики...')
            click_counter = count_clicks(token,url)
            print('Количество кликов по ссылке {url} = {count}'.format(url=url, count=click_counter))
        else:
            print('Вы ввели URL, создаю битлинк...')
            bitlink = shorten_link(token,url)
            print('Битлинк для адреса {url}: {short_link}'.format(url=url, short_link=bitlink))
    except requests.exceptions.RequestException() as err:
        print('Error, check input link. Error message: {error}'.format(error=err))


def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help = 'Введите URL')
    args = parser.parse_args()
    return args

def is_bitlink(token, url):
    header = {"Authorization": f"Bearer {token}"}
    parsed_url = urlparse(url)
    bitlink = '{netloc}{path}'.format(netloc=parsed_url.netloc,path=parsed_url.path)
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}", headers=header)
    return response.ok


def shorten_link(token, url):
    header = {"Authorization": f"Bearer {token}"}
    long_url = {"long_url": url}
    response = requests.post("https://api-ssl.bitly.com/v4/bitlinks", headers=header, json=long_url)
    response.raise_for_status()
    return response.json()['id']


def count_clicks(token, url):
    header = {"Authorization": f"Bearer {token}"}
    parsed_url = urlparse(url)
    bitlink = '{netloc}{path}'.format(netloc=parsed_url.netloc,path=parsed_url.path)
    params = {
        "unit": "day",
        "units": -1}
    response = requests.get(f"https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary",
                            headers=header, params=params)
    response.raise_for_status()
    return response.json()['total_clicks']


if __name__ == '__main__':
    main()
