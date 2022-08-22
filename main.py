import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent':
               'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'}
url = 'https://danne.ru/'

def get_first_url():
    sleep(1)
    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find_all('article', class_='goods-collection__item')
    for i in data:
        name = i.find('div', class_='goods-collection__title-box').text
        url_line = i.find('a').get('href')
        yield url_line, name_line

        print(name + '\n' + url_line)

def get_line_url():
    sleep(1)
    for url_line in get_first_url():
        response = requests.get(url=url_line, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        data = soup.find_all('div', class_='prog-nav')
        for i in data:
            line_urls = i.find_all('a')
            for ii in line_urls:
                line_name = ii.text
                line_url = ii.get('href')
                # yield line_url, line_name
                print(line_url, line_name)

def get_products_url():
    sleep(1)
    for line_url in get_line_url():
        response = requests.get(url=line_url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        datas = soup.find_all('ul', class_='products columns-4')
        for data in datas:
            prods_url = data.find_all('a')
            for prod_url in prods_url:
                product_name = prod_url.text
                product_url = prod_url.get('href')
                yield product_url
                # print(f'{product_name} : {product_url}')

def get_products_descr():
    for product_url in get_products_url():
        response = requests.get(url=product_url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        datas = soup.find('main', class_='site-main')
        name = datas.find('h1', class_='product_title entry-title')
        print(name)
        # for data in datas:
        #     all_data = data.find('h1', class_='product_title entry-title')
        #     print(all_data)




def main():
    get_first_url()
    get_line_url()
    # get_products_url()
    # get_products_descr()

if __name__ == "__main__":
    main()