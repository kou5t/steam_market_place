import json
import re
import requests
import time


def request_prices(url):
    rs = requests.get(url)
    m = re.search(r'var line1=(.+);', rs.text)
    data_str = m.group(1)
    data = json.loads(data_str)
    file_name = url[url.rfind("/") + 1:]
    with open(f'{file_name}.txt', 'w', encoding='UTF-8') as f:
        f.write('ДАТА, ЦЕНА В $, КОЛИЧЕСТВО \n')
        for line in data:
            data, price, value = line
            f.write(f"'{data}', {price}, '{value}'\n")
        print('Все успешно записано в файл: ' + file_name + '.txt')


def request_items():
    rs = requests.get('https://steamcommunity.com/market/search?appid=730#p1_popular_desc')
    urls = re.findall(r'<a class="market_listing_row_link" href="(.*)" id="resultlink_.">', rs.text)
    for url in urls:
        request_prices(url)
        time.sleep(5)


request_items()
