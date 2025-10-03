from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep




@then('Cart is empty')
def verify_cart_empty_msg(context):
    context.app.cart_page.verify_cart_empty_msg()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    # cart_summary = context.driver.find_element(*TOTAL_TXT).text
    # assert f'{amount} item' in cart_summary, f'Expected {amount} items but got {cart_summary}'
    context.app.cart_page.verify_cart_items()

