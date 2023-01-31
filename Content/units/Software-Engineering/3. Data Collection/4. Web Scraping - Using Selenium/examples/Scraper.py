from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def generate_driver(URL, browser='Chrome', directory='./chromedriver'):
    if browser == 'Firefox':
        driver = webdriver.Firefox(directory)
    elif browser == 'Safari': 
        driver = webdriver.Safari(directory)
    elif browser == 'Ie':
        driver = webdriver.Ie(directory)
    elif browser == 'Chrome':
        driver = webdriver.Chrome(directory)
    else:
        print(f'{browser} not available, defaulting to Chrome')
        driver = webdriver.Chrome(directory)
    driver.get(URL)
    return driver

       
def accept_cookies(driver, xpath):
    cookie_button = driver.find_element_by_xpath(xpath)
    cookie_button.click()

def find_element(driver, xpath):
    element = driver.find_element_by_xpath(xpath)
    return element

def find_items_from(element, xpath):
    items = element.find_elements_by_xpath(xpath)
    return items
