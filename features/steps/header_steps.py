from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep






@when('Search for {search_word}')
def search_for(context, search_word):
    context.app.header.search_product(search_word)


@when('Click Account button')
def click_account_button(context):
    context.app.header.click_acct_btn()



@when('Click on Cart icon')
def click_cart_icon(context):
    context.app.header.click_cart()

