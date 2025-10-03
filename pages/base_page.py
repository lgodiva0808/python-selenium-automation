from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Page:
    def __init__(self,drive):
        self.driver = drive
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self,*locator):
        self.driver.find_element(*locator).click()

    def input_text(self,text,*locator):
        self.driver.find_element(*locator).send_keys(text)

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable.'
        ).click()

    def wait_until_element_appear(self, *locator):
         element = self.wait.until(
             EC.visibility_of_element_located(locator),
             message=f'Element by {locator} did not appear.'
         )
         return element


    def wait_until_element_disappear(self, *locator):
         self.wait.until(
             EC.invisibility_of_element(locator),
             message=f'Element by {locator} did not disappear.'
         )

    def verify_text(self, expected_text,*locator):
        actual_text = self.find_element(*locator).text
        assert expected_text ==actual_text,\
             f'Expected {expected_text} did not match {actual_text}'

    def verify_partial_text(self, expected_partial_text,*locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text ==actual_text,\
             f'Expected {expected_partial_text} not in {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url,\
             f'Expected {expected_url} did not match {actual_url}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url == actual_url,\
             f'Expected {expected_partial_url} did not match {actual_url}'


