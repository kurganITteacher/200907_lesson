import random

import requests

print(random.random())

response = requests.get('https://ya.ru')
print(response)
print(response.content)
