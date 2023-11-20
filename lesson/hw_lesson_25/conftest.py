from selenium.webdriver import Firefox
import pytest

from lesson.hw_lesson_25.pages.dashboard import Dashboard


@pytest.fixture()
def driver():
    driver = Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture()
def dashboard(driver):
    driver.get("https://allo.ua/")
    driver.execute_script("window.localStorage['some stuff to store'] = 'Gem'")
    print(driver.execute_script("return window.localStorage['tADu '];"))
    yield Dashboard(driver)
