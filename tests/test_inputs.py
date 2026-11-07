import pytest
from selenium.webdriver.common.keys import Keys
from pages.inputs_page import InputsPage


@pytest.mark.basic
@pytest.mark.parametrize("value, expected", [
    ("123", "123"),
    ("abc", ""),
    ("!@#", ""),
])
def test_input_different_values(browser, value, expected):
    page = InputsPage(browser)
    page.open_page()

    page.type_value(value)
    assert page.current_value() == expected


@pytest.mark.basic
def test_arrow_up_down(browser):
    page = InputsPage(browser)
    page.open_page()

    page.type_value("5")
    page.press_arrow(Keys.ARROW_UP)
    assert page.current_value() == "6"

    page.press_arrow(Keys.ARROW_DOWN)
    assert page.current_value() == "5"