import time

import requests
import json
from bs4 import BeautifulSoup
# from My_Progect.hh_pars.main import varInput
url = "https://best.aliexpress.ru/?gatewayAdapt=glo2rus"
headers = {'User-agent': 'your bot 0.1'}
response = requests.get(url=url, headers=headers)
print(response.status_code)

dictionary = []
dictionary_end = []


time.sleep(2)
if response.status_code == 200:
    content = response.content
    # print(content)
    # with open(file='new.html', mode="wb") as file:
    #     file.write(content)
    content1 = BeautifulSoup(response.text, 'lxml')

    print(content1)
    text = content1.find_all('a', class_="CategoriesMenu_styles__title__znldk")
    print(text)