from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ContextMenuPage(BasePage):
    HOT_SPOT = (By.ID, "hot-spot")

    def open_page(self):
        self.open("/context_menu")

    def right_click_hot_spot(self):
        element = self.find(self.HOT_SPOT)
        ActionChains(self.driver).context_click(element).perform()

    def get_alert_text(self) -> str:
        return self.driver.switch_to.alert.text

    def accept_alert(self):
        self.driver.switch_to.alert.accept()