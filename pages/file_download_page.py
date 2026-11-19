from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FileDownloadPage(BasePage):
    def open_page(self):
        self.open("/download")

    def click_file_by_name(self, filename: str):
        xpath = f"//a[text()='{filename}']"
        self.wait.until(
            lambda d: d.find_element(By.XPATH, xpath).is_displayed()
        )
        self.find((By.XPATH, xpath)).click()