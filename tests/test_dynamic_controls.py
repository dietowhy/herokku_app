import pytest
from pages.dynamic_controls_page import DynamicControlsPage


@pytest.mark.basic
def test_remove_checkbox(browser):
    page = DynamicControlsPage(browser)
    page.open_page()

    assert page.is_checkbox_present() is True

    page.click_remove()
    page.wait_checkbox_message("It's gone!")

    assert page.is_checkbox_present() is False


@pytest.mark.basic
def test_enable_input(browser):
    page = DynamicControlsPage(browser)
    page.open_page()

    assert page.get_input().is_enabled() is False

    page.click_enable()
    page.wait_input_message("It's enabled!")

    assert page.get_input().is_enabled() is True