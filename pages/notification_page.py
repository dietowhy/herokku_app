from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class NotificationPage(BasePage):
    FLASH_BUTTON = (By.LINK_TEXT, "Click here")
    FLASH_MESSAGE = (By.ID, "flash")

    def open_page(self):
        self.open("/notification_message_rendered")

    def click_to_show_notification(self):
        self.find(self.FLASH_BUTTON).click()

    def get_flash_text(self) -> str:
        raw = self.find(self.FLASH_MESSAGE).text
        return raw.replace("×", "").replace("\n", "").strip()