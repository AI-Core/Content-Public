#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# This is an example of how a script should not look like
# Try to refactor it, and make a class instead of a bunch of functions


house_characteristics = {'Price': [], 'Bedrooms': [], 'Address': []}
driver = webdriver.Chrome()
for page_number in range(2, 5):
    URL = f"https://www.zoopla.co.uk/new-homes/property/london/?q=London&results_sort=newest_listings&search_source=new-homes&page_size=10&pn=1&view_type=list&pn={page_number}"
    driver.get(URL)

# cookies_button = driver.find_element_by_xpath('//*[@id="cookie-consent-form"]/div/div/div/button[2]')
# cookies_button.click()
# house_list = driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div[2]/main/div[2]/div[2]')
# house_items = house_list.find_elements_by_xpath('./div')
# n_houses = len(house_items)
# #%%
# for i in range(n_houses):
#     house_list = driver.find_element_by_xpath('//*[@id="__next"]/div[5]/div[2]/main/div[2]/div[2]')
#     house = house_list.find_elements_by_xpath('./div')[i]
#     house.click()
#     time.sleep(1)
#     # price = driver.find_element_by_xpath('//span[@data-testid="price"]').text
#     # house_characteristics['Price'].append(price)
#     driver.back()
#     time.sleep(1)

# driver.quit()
# house = pd.DataFrame(house_characteristics)
# house.to_csv('house.csv')