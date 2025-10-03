from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In button')
def click_sign_in_button(context):
    context.app.header.click_sign_btn()


@then('SignIn page opened')
def sign_in_page_opened(context):
    context.app.sign_in_page.verify_sign_in_page()