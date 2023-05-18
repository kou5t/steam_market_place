import json
import re
import requests
import time


def request_prices(url):
    response = requests.get(url)
    result_search = re.search(r'var line1=(.+);', response.text).group(1)
    prices = json.loads(result_search)
    file_name = url[url.rfind("/") + 1:]
    with open(f'{file_name}.txt', 'w', encoding='UTF-8') as file:
        file.write('ДАТА, ЦЕНА В $, КОЛИЧЕСТВО\n')
        for line in prices:
            data, price, value = line
            file.write(f"'{data}', {price}, '{value}'\n")
        print(f'Все успешно записано в файл: {file_name}.txt')


def request_items():
    response = requests.get('https://steamcommunity.com/market/search?appid=730#p1_popular_desc')
    result_search = re.findall(r'<a class="market_listing_row_link" href="(.*)" id="resultlink_.">', response.text)
    for url in result_search:
        request_prices(url)
        time.sleep(5)


request_items()
