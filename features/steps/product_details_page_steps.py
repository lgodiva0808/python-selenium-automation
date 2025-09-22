from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, 'li[class*="CarouselItem"] img')
SELECTED_COLOR = (By.CSS_SELECTOR, '[data-test="@web/VariationComponent"] div')

@given('Open target product A-91269719 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-bootcut-jeans/-/A-91269719?preselect=90919092#lnk=sametab')
    sleep(10)


@then('Verify user can click through colors')
def click_and_verify_colors(context):
    expected_colors = ['Dark Wash','Dark Indigo','Light Indigo']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for c in colors:
        c.click()
        sleep(2)


        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)


    assert expected_colors == actual_colors, f"expected {expected_colors} but got {actual_colors}"

