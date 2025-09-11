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
driver.get('https://www.amazon.com/')

sleep(2)

driver.find_element(By.XPATH, '//*[@alt="Continue shopping"]').click()

sleep(2)

#Access SignIn page
driver.find_element(By.XPATH, '//*[@aria-controls="nav-flyout-accountList"]').click()

sleep(2)

# amazon logo
driver.find_element(By.XPATH, '//*[@aria-label="Amazon"]')

#email field
driver.find_element(By.ID, 'ap_email_login')

#continue button
driver.find_element(By.XPATH, '//*[@aria-labelledby="continue-announce"]')

#Conditions of use link
driver.find_element(By.XPATH, '//a[contains(@href, "ap_signin_notification_condition_of_use")]')

#Privacy Notice link
driver.find_element(By.XPATH, '//a[contains(@href, "ap_signin_notification_privacy_notice")]')

#Need help link
driver.find_element(By.XPATH, '//a[contains(@href, "unified_claim_collection")]')

#Forgot your password link
#N/A

#Other issues with Sign-In link
#N/A

#Create free business account
driver.find_element(By.ID, 'ab-registration-ingress-link')

