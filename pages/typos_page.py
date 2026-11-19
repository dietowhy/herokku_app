from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TyposPage(BasePage):
    PARAGRAPH = (By.TAG_NAME, "p")

    def open_page(self):
        self.open("/typos")

    def get_second_paragraph(self) -> str:
        return self.find_all(self.PARAGRAPH)[1].text.strip()

    def refresh(self):
        self.driver.refresh()