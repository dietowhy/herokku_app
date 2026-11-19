from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class TablesPage(BasePage):
    def open_page(self):
        self.open("/tables")

    def cell_text(self, table: int, row: int, col: int) -> str:
        xpath = f"//table[{table}]//tbody/tr[{row}]//td[{col}]"
        return self.find((By.XPATH, xpath)).text.strip()