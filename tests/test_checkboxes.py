import pytest
from pages.checkboxes_page import CheckboxesPage


@pytest.mark.basic
def test_checkboxes_flow(browser):
    page = CheckboxesPage(browser)
    page.open_page()

    assert not page.is_checked(0)
    page.click_checkbox(0)
    assert page.is_checked(0)

    assert page.is_checked(1)
    page.click_checkbox(1)
    assert not page.is_checked(1)