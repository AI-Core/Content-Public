from pathlib import Path
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from base64 import b64decode


class GoogleImageScraper():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def search(self, query):
        self.driver.get(f"https://www.google.com/search?q={query}&tbm=isch")

    def accept_form(self):
        accept_button = self.driver.find_element(
            By.XPATH, "//button[@aria-label='Accept all']")

        accept_button.click()
        print(accept_button)

    def get_all_images(self, query):
        self.search(query)
        self.accept_form()
        container = self.driver.find_element(By.ID, "islrg")
        image_containers = container.find_elements(By.XPATH, "div/div")

        for img_container in image_containers:
            title = img_container.find_element(
                By.TAG_NAME, "h3").text.lower().replace(' ', '-')
            print(title)
            img = img_container.find_element(By.XPATH, "a/div/img")
            img_src = img.get_attribute('src')
            query_dir = f"images/{query}"
            Path(query_dir).mkdir(parents=True, exist_ok=True)
            fp = f"{query_dir}/{title}.jpg"
            if "data:image/jpeg;base64," in img_src:
                img_data = self.get_img_bytes_from_b64(img_src)
            else:
                img_data = self.get_img_bytes_from_url(img_src)
            with open(fp, 'wb') as handler:
                handler.write(img_data)

    def get_img_bytes_from_url(self, img_url):
        return requests.get(img_url).content

    def get_img_bytes_from_b64(self, b64_string):
        b64_string = b64_string.replace('data:image/jpeg;base64,', '')
        b64_bytes = b64decode(b64_string)
        print(b64_bytes)
        return b64_bytes


scraper = GoogleImageScraper()
query = "new york"
scraper.get_all_images(query)

# aria-label = "Accept all"

# driver.quit()
# img_container = html.find_all(id="islrg")
# print(len(img_container))
