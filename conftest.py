import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def class_browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()