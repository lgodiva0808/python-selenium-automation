from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class TargetAppPage(Page):
    PP_LINK = (By.CSS_SELECTOR, '[aria-label="privacy policy - opens in a new window"]')


    def open_target_app(self):
        self.open_url('https://www.target.com/orders?lnk=acct_nav_my_account')


    def click_privacy_link(self):
        self.click(*self.PP_LINK)