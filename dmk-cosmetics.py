import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}


def get_url():
    sleep(1)
    url = 'https://danne.ru/products/dmk-cosmetics/'
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
        try:
            response = requests.get(url=url_line, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('ul', class_='products columns-4')
            all_url = data.find_all('a')
            for i in all_url:
                name_url = i.find('h2').text
                url_cat = i.get('href')

                # print(url_cat, name_url)
                yield url_cat
        except Exception as ex:
            continue







def get_next2_url():
    sleep(1)
    for url_cat in get_next_url():
        try:
            response = requests.get(url=url_cat, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('ul', class_='products columns-4')
            all_url = data.find_all('a')
            for i in all_url:
                name_url = i.find('h2').text
                url_cat_next = i.get('href')

                yield url_cat_next
                # print(url_cat_next)
        except Exception as ex:
            continue

def get_next3_url():
    sleep(1)
    for url_cat_next in get_next2_url():
        try:
            response = requests.get(url=url_cat_next, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find('ul', class_='products columns-4')
            all_url = data.find_all('a')
            for i in all_url:
                name_url = i.find('h2').text
                url_cat_next2 = i.get('href')

                # yield url_cat_next2
                print(url_cat_next2)
        except Exception as ex:
            continue





# def array_cosmetics():
#     sleep(1)
#     for url_cat in get_next_url():
#         try:
#             response = requests.get(url=url_cat, headers=headers)
#             soup = BeautifulSoup(response.text, 'lxml')
#             data = soup.find('main', class_='site-main')
#             name = data.find('h1', class_='product_title entry-title').text
#             short_desc = data.find('div', class_='woocommerce-product-details__short-description').text
#             description = data.find('div', class_='summary entry-summary').text
#             src = data.find('div', class_='woocommerce-product-gallery__image').find('a').get('href')
#
#             # yield name, short_desc, description, src
#             print(name, short_desc, description, src)
#         except Exception as ex:
#             continue
#
# def array_cosmetics2():
#     sleep(1)
#     for url_cat_next2 in get_next3_url():
#         try:
#             response = requests.get(url=url_cat_next2, headers=headers)
#             soup = BeautifulSoup(response.text, 'lxml')
#             data = soup.find('main', class_='site-main')
#             name = data.find('h1', class_='product_title entry-title').text
#             short_desc = data.find('div', class_='woocommerce-product-details__short-description').text
#             description = data.find('div', class_='summary entry-summary').text
#             src = data.find('div', class_='woocommerce-product-gallery__image').find('a').get('href')
#
#                         # yield name, short_desc, description, src
#             print(name, short_desc, description, src)
#         except Exception as ex:
#             continue
# get_url()
# get_next_url()
# get_next2_url()
# get_next3_url()
# array_cosmetics()
# array_cosmetics2()