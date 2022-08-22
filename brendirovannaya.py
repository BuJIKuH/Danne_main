import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def get_url():
    sleep(1)
    url = 'https://danne.ru/products/brendirovannaya-produktsiya-dmk/'
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('ul', class_='products columns-4')
    all_url = data.find_all('a')
    for i in all_url:
        url_line = i.get('href')
        yield url_line
    #
    #     print(url_line)


def get_next_url():
    sleep(1)
    for url_line in get_url():
        response = requests.get(url=url_line, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find('ul', class_='products columns-4')
        all_url = data.find_all('a')
        for i in all_url:
            url_cat = i.get('href')
            yield url_cat
            # print(url_cat)


def array_brendirovannaya():
    sleep(1)
    for url_cat in get_next_url():
        try:
            response = requests.get(url=url_cat, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('main', class_='site-main')
            name = data.find('h1', class_='product_title entry-title').text
            try:
                short_desc = data.find('div', class_='woocommerce-product-details__short-description').text
            except:
                short_desc = 'Нет описания'
            try:
                description = data.find('div', class_='summary entry-summary').text
            except:
                description = 'Нет описания'
            src = data.find('div', class_='woocommerce-product-gallery__image').find('a').get('href')

            print(name)
            yield name, short_desc, description, src

        except Exception as ex:
            continue






# get_url()
# get_next_url()
# array_brendirovannaya()