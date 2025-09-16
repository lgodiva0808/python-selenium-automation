from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@when('Click on Cart icon')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'[data-test="@web/CartLink"]').click()
    sleep(4)

@then('Cart is empty')
def verify_empty_cart(context):
    expected = 'Your cart is empty'
    actual = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    assert expected == actual, f'Expected {expected} did not match {actual}'
    sleep(2)