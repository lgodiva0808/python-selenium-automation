from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_TXT = (By.XPATH, "//h1[contains(@class, 'styles_ndsHeading')]")

    def verify_sign_in_page(self):
        self.verify_text('Sign in or create account',*self.SIGNIN_TXT)