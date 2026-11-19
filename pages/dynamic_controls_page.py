from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DynamicControlsPage(BasePage):
    CHECKBOX_INPUT = (By.CSS_SELECTOR, "#checkbox input[type='checkbox']")
    REMOVE_BUTTON = (By.XPATH, "//button[text()='Remove']")
    CHECKBOX_MESSAGE = (By.CSS_SELECTOR, "#checkbox-example #message")

    INPUT = (By.CSS_SELECTOR, "#input-example input")
    ENABLE_BUTTON = (By.XPATH, "//button[text()='Enable']")
    INPUT_MESSAGE = (By.CSS_SELECTOR, "#input-example #message")

    def open_page(self):
        self.open("/dynamic_controls")

    def click_remove(self):
        self.find(self.REMOVE_BUTTON).click()

    def wait_checkbox_message(self, text: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.CHECKBOX_MESSAGE, text)
        )

    def is_checkbox_present(self) -> bool:
        return len(self.driver.find_elements(*self.CHECKBOX_INPUT)) > 0

    def get_input(self):
        return self.find(self.INPUT)

    def click_enable(self):
        self.find(self.ENABLE_BUTTON).click()

    def wait_input_message(self, text: str):
        self.wait.until(
            EC.text_to_be_present_in_element(self.INPUT_MESSAGE, text)
        )