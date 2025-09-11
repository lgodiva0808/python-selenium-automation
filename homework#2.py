from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/')

sleep(2)
# click account button
driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

#click SignIn btn from side navigation
driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

sleep(2)
# verify 'Sign in or create account' page opened
expected ='Sign in or create account'
actual = driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
assert expected == actual, f'Expected {expected} did not match {actual}'


driver.quit()

