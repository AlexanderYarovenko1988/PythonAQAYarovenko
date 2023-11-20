import time

from lesson.hw_lesson_25.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys
from lesson.hw_lesson_25.core.dashboard_locators import DashBoardLocators
from lesson.hw_lesson_25.pages.category_page import CategoryPage


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = DashBoardLocators()

    def choose_smartphones_and_phones_category(self):
        self._click(self.locators.smartphones_and_phones_locator)

    def send_text_to_search_field(self, text):
        self._send_keys(self.locators.search_locator, text)
        self._send_keys(self.locators.search_locator, Keys.ENTER)

    def open_the_product_on_the_home_page(self):
        self._click(self.locators.product_on_home_page_locator)

    def open_xiaomi_category(self):
        self._click(self.locators.smartphones_and_phones_locator)
        self._click(self.locators.smartphones_xiaomi_locator)
        return CategoryPage(self._driver)

    def open_shares(self):
        self._click(self.locators.shares_locator)

    def adding_item_to_cart(self, text):
        self._send_keys(self.locators.search_locator, text)
        self._send_keys(self.locators.search_locator, Keys.ENTER)
        self._click(self.locators.button_product_locator)

    def filter_charging_stations(self):
        self._click(self.locators.charging_stations_locator)

    def all_results_products(self, text):
        self._send_keys(self.locators.search_locator, text)
        self._click(self.locators.search_locator)
        self._click(self.locators.all_results_locator)

    def change_city_location(self, text):
        self._click(self.locators.locations_locator)
        self._send_keys(self.locators.city_search_locator, text)
        self._click(self.locators.city_title_locator)
