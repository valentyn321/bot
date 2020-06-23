import requests
from bs4 import BeautifulSoup
from db import init_db, add_item
import time

URL = 'https://us.puma.com/en/us/men/sale/shoes'
HEADERS = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:77.0) Gecko/20100101 Firefox/77.0',
            'accept': '*/*'
}
BEGIN_OF_URL = 'https://us.puma.com'

def parse_number_of_items(url):
    html = get_html(url)
    if html.status_code == 200:
        soup = BeautifulSoup(html.text, 'lxml')
        number = soup.find('span', class_='category-result-count-value').get_text().replace('(', '').replace(')', '')
        return number

def update_url(url, number):
    return url+'&pagesize='+str(number)



def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'lxml')
    sale = soup.find_all('div', class_='col-6 col-sm-4 col-md-3')
    
    items = []
    for item in sale:
        items.append({
            'title': item.find('a', class_='product-tile-link link').get_text(),
            'link': BEGIN_OF_URL + item.find('a', class_='product-tile-image-link tile-image-link').get('href'),
           # 'photo': item.find('img', class_='product-tile-image product-tile-image--default tile-image').get('data-src'),
            'price_usd': item.find('span', class_='value').get_text(),
        })
    return items

def push_content_to_the_db(dict_of_items):
    for item in dict_of_items:
        add_item(
            title=item['title'],
            link=item['link'],
           # photo=item['photo'],
            price_usd=item['price_usd'],
        )

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        items = get_content(html.text)
        init_db(force=True)
        push_content_to_the_db(items)
        
    else:
        print("Error!")


parse()
