from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

TOTAL_TXT = (By.CSS_SELECTOR, '[data-test="cart-summary-item-count"]')

@then('Cart is empty')
def verify_empty_cart(context):
    expected = 'Your cart is empty'
    actual = context.driver.find_element(By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]').text
    assert expected == actual, f'Expected {expected} did not match {actual}'
    sleep(2)

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(*TOTAL_TXT).text
    assert f'{amount} item' in cart_summary, f'Expected {amount} items but got {cart_summary}'

