import requests
from bs4 import BeautifulSoup
from .db import init_db, add_item
import time

URL = 'https://www.lamoda.ua/c/477/clothes-muzhskaya-odezhda/?brands=1061%2C1163%2C4869%2C4189%2C6158%2C23679%2C3777%2C2047%2C1107%2C1063%2C18583%2C573%2C25571&display_locations=outlet&is_sale=1'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'accept': '*/*'
}
BEGIN_OF_URL = 'https://www.lamoda.ua'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    # sale = soup.find('div', class_='products-catalog__list')
    sale = soup.find_all('div', class_='products-list-item')

    
    items = []
    for item in sale:
       items.append({
            'title': item.find('span', class_='products-list-item__type').get_text().replace('\n                    ', '').replace('\n                ', ''),
            'link': BEGIN_OF_URL + item.find('a', class_='products-list-item__link link').get('href'),
        #       'photo': item.find('img', class_='product-tile-image product-tile-image--default tile-image').get('data-src'),
            'price_uah': item.find('span', class_='price__new').get_text(),
        })
    return items

def push_content_to_the_db(dict_of_items):
    for item in dict_of_items:
        add_item(
            title=item['title'],
            link=item['link'],
           # photo=item['photo'],
            price_uah=item['price_uah'],
            name_of_table='lamoda_clothes.db'
        )

def parse_cl():
    html = get_html(URL)
    if html.status_code == 200:
        items = get_content(html.text)
        init_db(name_of_table='lamoda_clothes.db', force=True)
        push_content_to_the_db(items)          
    else:
        print("Error!")

parse_cl()