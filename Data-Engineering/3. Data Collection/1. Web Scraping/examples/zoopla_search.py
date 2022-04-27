#%%
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

# This is an example of how a script should not look like
# Try to refactor it, and make a class instead of a bunch of functions


house_characteristics = {'Price': [], 'Bedrooms': [], 'Address': []}
URL = "https://www.zoopla.co.uk"
driver = webdriver.Chrome('./chromedriver')
driver.get(URL)
cookies_button = driver.find_element_by_xpath('//*[@id="cookie-consent-form"]/div/div/div/button[2]')
cookies_button.click()
# %%
# search_bar = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div[2]/div')
# search_bar.click()
search_bar = driver.find_element_by_xpath('//*[@id="__next"]/main/div[1]/div[2]/div[2]/div')
search_bar.click()
search_bar.send_keys('Manchester')
search_bar.send_keys(Keys.RETURN)
# %%
