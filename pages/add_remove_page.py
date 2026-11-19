from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class AddRemovePage(BasePage):
    ADD_BUTTON = (By.XPATH, "//button[text()='Add Element']")
    DELETE_BUTTON = (By.XPATH, "//button[text()='Delete']")

    def open_page(self):
        self.open("/add_remove_elements/")

    def add_element(self):
        self.find(self.ADD_BUTTON).click()

    def delete_element(self):
        self.find(self.DELETE_BUTTON).click()

    def delete_buttons_count(self) -> int:
        return len(self.find_all(self.DELETE_BUTTON))