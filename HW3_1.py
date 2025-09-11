from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

options = Options()
options.add_argument('--incognito')

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.maximize_window()

# open the url
driver.get('https://stackoverflow.com/users/signup')

sleep(3)

driver.find_element(By.CSS_SELECTOR, 'h1.fs-headline1.ws-nowrap')

sleep(2)

driver.find_element(By.CSS_SELECTOR, '.js-terms.fs-caption')
driver.find_element(By.CSS_SELECTOR, '#email')
driver.find_element(By.CSS_SELECTOR, '#password')

# password eye
driver.find_element(By.CSS_SELECTOR, 'svg.c-pointer.js-show-password')

driver.find_element(By.CSS_SELECTOR, '#submit-button')
driver.find_element(By.CSS_SELECTOR, 'button.s-btn__google.bc-black-225')
driver.find_element(By.CSS_SELECTOR, 'button[data-provider="google"]')
driver.find_element(By.CSS_SELECTOR, '[href*="content=public-sign-up"]')