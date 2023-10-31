import requests
from config import *

url = "https://api-ssl.bitly.com/v4/user"
headers = {
    'Authorization': f'Bearer {os.environ["BITLY_TOKEN"]}'
}
response = requests.get(url, headers=headers)
response.raise_for_status()
print(response.text)

