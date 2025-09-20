from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In button')
def click_sign_in_button(context):
    context.driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()
    sleep(2)

@then('SignIn page opened')
def sign_in_page_opened(context):
    expected = 'Sign in or create account'
    actual = context.driver.find_element(By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]").text
    assert expected == actual, f'Expected {expected} did not match {actual}'