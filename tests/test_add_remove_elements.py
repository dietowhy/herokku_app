import pytest
from pages.add_remove_page import AddRemovePage


@pytest.mark.basic
def test_add_two_elements_delete_one(browser):
    page = AddRemovePage(browser)
    page.open_page()

    page.add_element()
    page.add_element()
    assert page.delete_buttons_count() == 2

    page.delete_element()
    assert page.delete_buttons_count() == 1