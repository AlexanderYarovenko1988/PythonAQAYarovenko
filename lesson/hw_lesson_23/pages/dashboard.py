import time

from lesson.hw_lesson_23.pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys


class Dashboard(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.smartphones_and_phones_locator = ("xpath", "(//a[@class='mm__a'])[2]")
        self.search_locator = ("xpath", "//input[@id='search-form__input']")
        self.product_on_home_page_locator = ("xpath", "(//div[@class='h-pc'])[1]")
        self.smartphones_xiaomi_locator = ("xpath", "(//a[@title='Xiaomi'][normalize-space()='Xiaomi'])[1]")
        self.shares_locator = ("xpath", "//a[@class='mh-button'][contains(text(),'Акції')]")
        self.button_product_locator = ("xpath", "//button[@id='product-buy-button']")
        self.charging_stations_locator = ("xpath", "//a[@aria-label='Зарядні станції']")
        self.all_results_locator = ("xpath", "//button[contains(text(),'Всі результати пошуку')]")
        self.locations_locator = ("xpath", "//button[@data-geo-label='Київ']")
        self.city_search_locator = ("xpath", "//input[@id='city']")
        self.city_title_locator = ("xpath", "//li[@title='Баб'янка']")

    def choose_smartphones_and_phones_category(self):
        self._click(self.smartphones_and_phones_locator)

    def send_text_to_search_field(self, text):
        self._send_keys(self.search_locator, text)
        self._send_keys(self.search_locator, Keys.ENTER)

    def open_the_product_on_the_home_page(self):
        self._click(self.product_on_home_page_locator)

    def open_xiaomi_category(self):
        self._click(self.smartphones_and_phones_locator)
        self._click(self.smartphones_xiaomi_locator)

    def open_shares(self):
        self._click(self.shares_locator)

    def adding_item_to_cart(self, text):
        self._send_keys(self.search_locator, text)
        self._send_keys(self.search_locator, Keys.ENTER)
        self._click(self.button_product_locator)

    def filter_charging_stations(self):
        self._click(self.charging_stations_locator)

    def all_results_products(self, text):
        self._send_keys(self.search_locator, text)
        self._click(self.search_locator)
        self._click(self.all_results_locator)

    def change_city_location(self, text):
        self._click(self.locations_locator)
        self._send_keys(self.city_search_locator, text)
        self._click(self.city_title_locator)
