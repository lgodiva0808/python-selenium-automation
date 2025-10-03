from time import sleep

from selenium.webdriver.common.by import By


from pages.base_page import Page


class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, '[data-test="boxEmptyMsg"]')
    TOTAL_TXT = (By.XPATH, "//span[@class='styles_cart-summary-span__4h9y1']")
    PRODUCT_NAME = (By.CSS_SELECTOR, '[data-test="cartItem-title"]')


    def verify_cart_empty_msg(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)


    def verify_cart_items(self):
        sleep(2)
        elements = self.find_elements(*self.TOTAL_TXT)
        text = elements[1].text
        assert '1' in text, "expected 1 but found {}".format(text)

    def verify_product_name(self):
        text = self.find_element(*self.PRODUCT_NAME).text
        assert 'mug' in text.lower(), "expected mug but found {}".format(text)
