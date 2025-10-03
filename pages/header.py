from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page



class Header(Page):
    CART_ICON = (By.CSS_SELECTOR, '[data-test="@web/CartLink"]')
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, '[data-test="@web/Search/SearchButton"]')
    ACCT_ICON = (By.XPATH, "//*[@data-test='@web/AccountLink']")
    SIGNIN_BTN = (By.XPATH, "//*[@data-test='accountNav-signIn']")

    def search_product(self, search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(9)

    def click_cart(self):
        self.wait_until_clickable_click(*self.CART_ICON)

    def click_acct_btn(self):
        sleep(2)
        self.wait_until_clickable_click(*self.ACCT_ICON)

    def click_sign_btn(self):
        self.wait_until_clickable_click(*self.SIGNIN_BTN)