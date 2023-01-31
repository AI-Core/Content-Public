from distutils.command.sdist import sdist
from this import d
import requests
from bs4 import BeautifulSoup
from uuid import uuid4
import pandas as pd


class ProductScraper():
    def __init__(self):
        self.df = pd.DataFrame(columns=["id", "name", "description", "price"])

    def get_homepage(self):
        self.page_url = "https://pythonscraping.com/pages/page3.html"
        response = requests.get(self.page_url)
        html = response.content
        html = BeautifulSoup(html, 'html.parser')
        print(html.prettify())
        return html

    def get_products(self, html):
        return html.find_all('tr')[2:]

    def download_img(self, img_url, fp):
        img_data = requests.get(img_url).content
        with open(fp, 'wb') as handler:
            handler.write(img_data)

    def get_all_product_data(self):
        html = self.get_homepage()
        products = self.get_products(html)
        for product in products:
            self.get_product_data(product)
        print(self.df)
        self.df.to_csv('tabular_data.csv')

    def get_product_data(self, product):
        id = product.attrs["id"]

        data = product.find_all('td')
        img_tag = data.pop()
        self.download_img_from_tag(img_tag)

        data = self.clean_text_data(data)
        title, description, price = data
        price = self.format_price(price)

        product_data = pd.DataFrame({
            "id": [id],
            "name": [title],
            "description": [description],
            "price": [price],
            # "img": local_img_filepath
        })
        self.df = pd.concat([self.df, product_data])

    def format_price(self, price):
        return float(price[1:].replace(',', ''))

    def download_img_from_tag(self, img_tag):
        img_src = img_tag.img.attrs["src"]

        img_src = self.page_url[:-16] + img_src[3:]
        print(img_src)
        self.download_img(img_src, f"images/{id}.jpg")

    def clean_text_data(self, data):
        data = [feature.text for feature in data]
        data = [text.replace('\n', '') for text in data]
        return data


if __name__ == "__main__":
    scraper = ProductScraper()
    scraper.get_all_product_data()
