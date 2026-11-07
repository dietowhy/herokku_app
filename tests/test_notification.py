import sys
import pytest
from pages.notification_page import NotificationPage


@pytest.mark.advanced
@pytest.mark.skipif(sys.platform == "win32", reason="Демонстрация skipif: пропускается только на Windows")
def test_notification_message(browser):
    page = NotificationPage(browser)
    page.open_page()
    page.click_to_show_notification()

    flash = page.get_flash_text()
    assert flash in (
        "Action successful",
        "Action unsuccesful, please try again",
    )


@pytest.mark.advanced
@pytest.mark.xfail(reason="Демонстрация xfail: тест заведомо падает, так как ожидается неверный текст")
def test_notification_wrong_text(browser):
    page = NotificationPage(browser)
    page.open_page()
    page.click_to_show_notification()

    flash = page.get_flash_text()
    assert flash == "This text is never shown"