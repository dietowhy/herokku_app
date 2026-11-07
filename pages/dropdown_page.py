from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class DropdownPage(BasePage):
    DROPDOWN = (By.ID, "dropdown")

    def open_page(self):
        self.open("/dropdown")

    def get_options(self):
        return Select(self.find(self.DROPDOWN)).options

    def select_by_index(self, index: int):
        Select(self.find(self.DROPDOWN)).select_by_index(index)

    def selected_option_text(self) -> str:
        return Select(self.find(self.DROPDOWN)).first_selected_option.text