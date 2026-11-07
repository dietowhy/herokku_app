import pytest
from pages.hovers_page import HoversPage


@pytest.fixture(scope="class")
def hovers_page(class_browser):
    page = HoversPage(class_browser)
    page.open_page()
    return page


@pytest.mark.advanced
class TestHovers:
    def test_hover_shows_name(self, hovers_page):
        name = hovers_page.hover_figure(0)
        assert name == "name: user1"

    def test_hover_click_no_404(self, hovers_page):
        hovers_page.hover_figure(0)
        hovers_page.click_figure_link(0)

        assert "404" not in hovers_page.driver.title
        assert hovers_page.driver.current_url != f"{hovers_page.BASE_URL}/hovers"