from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class InputsPage(BasePage):
    INPUT = (By.TAG_NAME, "input")

    def open_page(self):
        self.open("/inputs")

    def get_input(self):
        return self.find(self.INPUT)

    def type_value(self, value: str):
        field = self.get_input()
        field.clear()
        field.send_keys(value)

    def press_arrow(self, key):
        self.get_input().send_keys(key)

    def current_value(self) -> str:
        return self.get_input().get_attribute("value")