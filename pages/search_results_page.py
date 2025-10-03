from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page



class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, '[id*="addToCartButtonOrTextIdFor"]')
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, '[class*="styles_fontSize4__FN7fp styles_noMargin__uTxpX"]')
    ADD_TO_CART_SIDE_NAVIGATION = (By.CSS_SELECTOR, '[data-test="shippingButton"]')
    VIEW_CART_BTN = (By.CSS_SELECTOR, 'a[class*="ndsButtonSecondary__iSf2I"]')



    def verify_search_results(self, product):
        self.verify_partial_text(product, *self.SEARCH_RESULTS_TXT)

    def verify_product_url(self, product):
        # self.verify_url(f'https://www.target.com/s?searchTerm={product}')
        self.verify_partial_url(f'searchTerm={product}')


    def click_add_to_cart_btn(self):
        sleep(5)
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)

    def store_product_name(self):
        self.find_element(*self.SIDE_NAV_PRODUCT_NAME)

    def click_add_to_cart_btn_sidenav(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_SIDE_NAVIGATION)

    def open_cart_page(self):
        self.wait_until_clickable_click(*self.VIEW_CART_BTN)

