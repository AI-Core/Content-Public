from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# This is an example of how a module should not look like
# Try to refactor it, and make a class instead of a bunch of functions

house_characteristics = {'Price': [], 'Bedrooms': [], 'Address': []}
def house_listing():
    house_list = driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div[2]/main/div[2]/div[2]')
    house_items = house_list.find_elements_by_xpath('./div')
    hrefs = []
    for item in house_items:
        link = item.find_element_by_xpath('.//a').get_attribute('href')
        hrefs.append(link)

    for href in hrefs:
        driver.get(href)
        price = driver.find_element_by_xpath('//span[@data-testid="price"]').text
        n_bedrooms = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[2]/div[2]/div/div[1]/span').text
        address = driver.find_element_by_xpath('//*[@id="main-content"]/div[1]/div[2]/div[2]/h1/span[2]').text
        house_characteristics['Price'].append(price)
        house_characteristics['Bedrooms'].append(n_bedrooms)
        house_characteristics['Address'].append(address)
        time.sleep(1)

URL = "https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=10&pn=1&view_type=list"
driver = webdriver.Chrome()
driver.get(URL)
cookies_button = driver.find_element_by_xpath('//*[@id="cookie-consent-form"]/div/div/div/button[2]')
cookies_button.click()
house_listing()

for page_number in range(2, 4):
    URL = f"https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=10&pn={page_number}&view_type=list"
    driver.get(URL)
    house_listing()

driver.quit()
house = pd.DataFrame(house_characteristics)
house.to_csv('house.csv')