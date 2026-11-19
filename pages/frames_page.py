from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FramesPage(BasePage):
    IFRAME = (By.ID, "mce_0_ifr")
    CONTENT = (By.CSS_SELECTOR, "body p")

    def open_page(self):
        self.open("/iframe")

    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.find(self.IFRAME))

    def switch_to_default(self):
        self.driver.switch_to.default_content()

    def get_content_text(self) -> str:
        return self.find(self.CONTENT).text.strip()