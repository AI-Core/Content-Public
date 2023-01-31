import requests
from bs4 import BeautifulSoup
from uuid import uuid4


class ProductScraper():

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

    def get_product_data(self, product):
        id = product.attrs["id"]

        data = product.find_all('td')
        img = data.pop()
        img_src = img.img.attrs["src"]

        img_src = self.page_url[:-16] + img_src[3:]
        print(img_src)
        self.download_img(img_src, f"images/{id}.jpg")

        data = [feature.text for feature in data]
        title, description, price = data

        product_data = {
            "id": id,
            "name": title,
            "description": description,
            "price": price,
            # "img": local_img_filepath
        }


if __name__ == "__main__":
    scraper = ProductScraper()
    scraper.get_all_product_data()
