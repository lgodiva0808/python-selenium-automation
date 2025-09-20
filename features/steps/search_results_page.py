from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextIdFor"]')
ADD_TO_CART_SIDE_NAVIGATION = (By.CSS_SELECTOR, '[data-test="shippingButton"]')
VIEW_CART_BTN = (By.CSS_SELECTOR, 'a[class*="ndsButtonSecondary__iSf2I"]')
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[class*="styles_fontSize4__FN7fp styles_noMargin__uTxpX"]')
PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    actual_text = context.browser.find_element(*SEARCH_RESULTS_TXT).text
    assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'


@when('Click on Add to Cart button')
def click_add_to_cart(context):
    sleep(7)
    context.driver.find_element(*ADD_TO_CART_BTN).click()

# @when('Store product name')
# def store_product_name(context):
#     context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
#     print('Product name stored:', context.product_name)

@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart_side_navigation(context):
    context.driver.find_element(*ADD_TO_CART_SIDE_NAVIGATION).click()
    sleep(5)


@when ('Open cart page')
def open_cart_page(context):
    context.driver.find_element(*VIEW_CART_BTN).click()
    sleep(5)

# @then('Verify cart has correct product')
# def verify_product_name(context):
#     product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
#     print('Name in cart: ', product_name_in_cart)
#
#     assert context.product_name[:20] == product_name_in_cart[:20],
#         f'Expected {context.product_name[:20]} but got {product_name_in_cart[:20]}'