from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


BENEFIT_CELLS = (By.CSS_SELECTOR, '[data-test="@web/slingshot-components/CellsComponent/Link"]')


@then('Verify page has at least {expected_amount} benefit cells')
def verify_page_has_at_least_benefit_cells(context, expected_amount):
    expected_amount = int(expected_amount)
    cells = context.driver.find_elements(*BENEFIT_CELLS)
    print(f'Cells {cells}')
    assert min(cells) == expected_amount, f'Expected {expected_amount} benefit cells, but found {min(cells)}'

