from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CheckboxesPage(BasePage):
    CHECKBOXES = (By.CSS_SELECTOR, "[type='checkbox']")

    def open_page(self):
        self.open("/checkboxes")

    def get_checkboxes(self):
        return self.find_all(self.CHECKBOXES)

    def is_checked(self, index: int) -> bool:
        return self.get_checkboxes()[index].is_selected()

    def click_checkbox(self, index: int):
        self.get_checkboxes()[index].click()