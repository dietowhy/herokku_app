import pytest
from pages.context_menu_page import ContextMenuPage


@pytest.mark.basic
def test_right_click_shows_alert(browser):
    page = ContextMenuPage(browser)
    page.open_page()

    page.right_click_hot_spot()

    assert page.get_alert_text() == "You selected a context menu"

    page.accept_alert()