import json

import requests
from bs4 import BeautifulSoup
from time import sleep

# '''Первая часть, делаем запрос и сохраняем страницу, чтобы не терроризировать сайт'''
# url = "https://danne.ru/"
#
# headers = {'User-Agent':
#                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
# }
#
# response = requests.get(url, headers=headers )
# src = response.text
#
# with open('index.html', 'w') as file:
#     file.write(src)
# '''Часть вторая, теперь открываем наш фаил и делаем запросы у него'''
with open('index.html') as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')
all_prod_href = soup.find('article')
# all_prod_href = data.find_all('article')
# all_prod_name = data.find_all('article')

# print(all_prod_href)
# '''Создаем словарь и файл JSON'''
for item in all_prod_href:
    item_name = item.text
    item_href = item.find('a').get('href')
    print(f'{item_name} : {item_href}')
# all_categories_dict = {}
#
# for items in all_products_name:
#     item_name = items.text
#
#
#     for item in all_products_href:
#         item_href = item.get('href')
#
#     all_categories_dict[item_name] = item_href
#
#
#     with open('all_categories_dict.json', 'w') as file:
#         json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)
#
#     '''Теперь заходим в каждую ссылку'''
#
# with open('all_categories_dict.json') as file:
#     all_categories = json.load(file)
#
#
# for line_name, line_href in all_categories.items():
#     response = requests.get(url=line_href, headers=headers)
#     src = response.text
#
#     with open(f'line/{line_name}.html', 'w') as file:
#         file.write(src)
#
#         with open(f'line/{line_name}.html') as file:
#             src = file.read()
#             soup = BeautifulSoup(src, 'lxml')
#             # name = soup.find(class_='product-category product').find('a').find_all('h2')
#             all_line_name = soup.find_all(class_='woocommerce-loop-category__title')
#             all_line_href = soup.find_all(class_='product-category product')
#
#             all_lines_dict = {}
#
#             for items in all_line_name:
#                 item_name = items.text
#
#
#                 for item in all_line_href:
#                     item_href = item.get('href')
#
#                 all_lines_dict[item_name] = item_href
#
#                 with open('all_lines_dict.json', 'w') as file:
#                     json.dump(all_lines_dict, file, indent=4, ensure_ascii=False)

















