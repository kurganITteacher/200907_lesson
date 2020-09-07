import random

import requests

print(random.random())

response = requests.get('https://ya.ru')
print(response)
print(response.content)

"""
ДЗ:
1. методы http: get, post, put, delete  
# https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol#Request_methods

2. списки (как бы массивы): lists  
# https://habr.com/ru/post/319164/
# https://www.w3schools.com/python/python_lists.asp

3. циклы в python: while, for in
# https://www.w3schools.com/python/python_while_loops.asp
# https://www.w3schools.com/python/python_for_loops.asp
"""
