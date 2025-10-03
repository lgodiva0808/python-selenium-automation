from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep









@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)
    context.app.search_results_page.verify_product_url(product)

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    # context.driver.find_element(*ADD_TO_CART_BTN).click()
    # context.driver.wait.until(
    #     EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
    #     message='Side navigation product did not appear'
    # )
    context.app.search_results_page.click_add_to_cart_btn()


@when('Store product name')
def store_product_name(context):
    # context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    # print('Product name stored:', context.product_name)
    context.app.search_results_page.store_product_name()


@when('Confirm Add to Cart button from side navigation')
def confirm_add_to_cart_side_navigation(context):
    # context.driver.find_element(*ADD_TO_CART_SIDE_NAVIGATION).click()
    # sleep(5)
    context.app.search_results_page.click_add_to_cart_btn_sidenav()


@when ('Open cart page')
def open_cart_page(context):
    # context.driver.find_element(*VIEW_CART_BTN).click()
    # sleep(5)
    context.app.search_results_page.open_cart_page()


@then('Verify cart has correct product')
def verify_product_name(context):
    # product_name_in_cart = context.driver.find_element(*PRODUCT_NAME).text
    # print('Name in cart: ', product_name_in_cart)

    # assert context.product_name[:20] == product_name_in_cart[:20], \
    #     f'Expected {context.product_name[:20]} but got {product_name_in_cart[:20]}'
    context.app.cart_page.verify_product_name()