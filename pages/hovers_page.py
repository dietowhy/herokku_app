from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class HoversPage(BasePage):
    FIGURES = (By.CSS_SELECTOR, ".figure")
    FIGURE_NAME = (By.CSS_SELECTOR, ".figcaption h5")
    FIGURE_LINK = (By.CSS_SELECTOR, ".figcaption a")

    def open_page(self):
        self.open("/hovers")

    def hover_figure(self, index: int) -> str:
        figures = self.find_all(self.FIGURES)
        ActionChains(self.driver).move_to_element(figures[index]).perform()
        name = figures[index].find_element(*self.FIGURE_NAME).text
        return name

    def click_figure_link(self, index: int):
        figures = self.find_all(self.FIGURES)
        figures[index].find_element(*self.FIGURE_LINK).click()