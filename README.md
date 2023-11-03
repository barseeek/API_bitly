# Bitly Link Shortener

This is a Python script for working with Bitly's URL shortening service. It allows you to:

- Check if a given URL is a Bitly bitlink.
- Shorten a long URL using Bitly.
- Retrieve the total number of clicks on a Bitly link.

## How to install

Before you start using this script, you need to have the following prerequisites in place:

1. Python 3 installed on your system.
2. Use `pip` to install dependencies:
```
pip install -r requirements.txt
```
3. Create a [Bitly](https://app.bitly.com/) account and get an access token. 

## Usage

1. Clone this repository or download the script to your local machine.

2. Create a `.env` file in the same directory as the script with the following content, replacing `YOUR_BITLY_TOKEN` with your actual Bitly access token:
```
BITLY_TOKEN=YOUR_BITLY_TOKEN
```

## Examples

1. Non-bitly URL
```
$ python main.py https://google.com
```
```
Вы ввели URL, создаю битлинк...
Битлинк для адреса https://google.com: bit.ly/45Te3MY
```
2. Bitly URL
```
$ python main.py http://bit.ly/45Te3MY
```
```
Вы ввели действующий битлинк, считаю клики...
Количество кликов по ссылке http://bit.ly/45Te3MY = 2
```
## Project Goals

This code was written for educational purposes as part of an online course for web developers at dvmn.org.

## License

This script is provided under the MIT License - [License](LICENSE.md)
