from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')


@when('Search for {search_word}')
def search_for(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(5)


@when('Click Account button')
def click_account_button(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()
    sleep(2)


@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(4)

