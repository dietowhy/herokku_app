import pytest
from pages.dropdown_page import DropdownPage


@pytest.mark.basic
def test_dropdown_options_and_selection(browser):
    page = DropdownPage(browser)
    page.open_page()

    options = page.get_options()
    assert len(options) >= 3
    texts = [opt.text for opt in options]
    assert "Please select an option" in texts

    page.select_by_index(1)
    assert page.selected_option_text() == texts[1]

    page.select_by_index(2)
    assert page.selected_option_text() == texts[2]