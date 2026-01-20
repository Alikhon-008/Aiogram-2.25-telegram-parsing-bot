import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv



def texno(category):
    list_data = []
    load_dotenv()
    URL = os.getenv("URL")
    HOST = os.getenv("HOST")
    HEADERS = {
        'USER-AGENT': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Mobile Safari/537.36'

    }
    html =requests.get(URL + category, headers=HEADERS)
    soup = BeautifulSoup(html.text, 'html.parser')


    products = soup.find_all('div', class_="col-3")

    for product in products:
        images_a = product.find('a', class_='product-link')
        images = images_a.find('img').get('data-src')
        title = product.find('h2').text
        credit_price = product.find('div', class_='installment-price').get_text(strip=True)
        price = product.find('div', class_='product-price__current').get_text(strip=True)
        link = HOST + product.find('a').get('href')
        # print(images)

        list_data.append({
            'image': images,
            'title': title,
            'price': price,
            'credit_price': credit_price,
            'link': link,
        })

    return list_data



texno("katalog/televizory-lg/")