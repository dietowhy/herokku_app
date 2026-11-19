import pytest
from pages.frames_page import FramesPage


@pytest.mark.basic
def test_iframe_content(browser):
    page = FramesPage(browser)
    page.open_page()

    page.switch_to_iframe()
    assert page.get_content_text() == "Your content goes here."

    page.switch_to_default()