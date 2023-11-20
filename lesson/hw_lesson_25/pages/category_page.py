from lesson.hw_lesson_25.core.category_locators import CategoryLocators
from lesson.hw_lesson_25.pages.base_page import BasePage
from lesson.hw_lesson_25.pages.product_page import ProductPage


class CategoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = CategoryLocators()


    def checkbox_ready_to_ship(self):
        self._click(self.locators.check_box_ready_to_ship_locator)

    def click_one_product(self):
        self._click(self.locators.product_locator)
        return ProductPage(self._driver)

    def click_price_list(self):
        self._click(self.locators.price_list_locator)

    def click_sort_new(self):
        self._click(self.locators.sort_current_locator)
        self._click(self.locators.sort_current_locator)
        self._click(self.locators.new_locator)
