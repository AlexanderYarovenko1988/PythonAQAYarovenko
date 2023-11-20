# base_page.py

from abc import ABC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage(ABC):
    def __init__(self, driver):
        self._driver = driver
        self.web_driver_wait = WebDriverWait(self._driver, 10)
        self.cookies = Cookies(self._driver)
        self.local_storage = LocalStorage(self._driver)

    def wait_until_element_appears(self, locator):
        return self.web_driver_wait.until(EC.presence_of_element_located(locator))

    def _click(self, locator):
        return self.wait_until_element_appears(locator).click()

    def _send_keys(self, locator, text):
        return self.wait_until_element_appears(locator).send_keys(text)

# cookies.py

class Cookies(BasePage):
    def __init__(self, driver):
        self.driver = driver

    def set_cookie(self, name, value):
        try:
            self.driver.add_cookie({'name': name, 'value': value})
        except Exception as e:
            print(f"Error setting cookie: {e}")

    def get_cookie(self, name):
        try:
            return self.driver.get_cookie(name)
        except Exception as e:
            print(f"Error getting cookie: {e}")

# local_storage.py

class LocalStorage:
    def __init__(self, driver):
        self.driver = driver

    def set_item(self, key, value):
        try:
            self.driver.execute_script(f"localStorage.setItem('{key}', '{value}')")
        except Exception as e:
            print(f"Error setting local storage item: {e}")

    def get_item(self, key):
        try:
            return self.driver.execute_script(f"return localStorage.getItem('{key}')")
        except Exception as e:
            print(f"Error getting local storage item: {e}")
