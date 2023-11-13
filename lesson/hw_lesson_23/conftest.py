from selenium.webdriver import Firefox
import pytest

from lesson.hw_lesson_23.pages.dashboard import Dashboard



@pytest.fixture()
def driver():
    driver = Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def dashboard(driver):
    driver.get("https://allo.ua/")
    yield Dashboard(driver)
