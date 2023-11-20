from lesson.hw_lesson_25.core.product_locators import ProductLocators
from lesson.hw_lesson_25.pages.base_page import BasePage



class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ProductLocators()

    def click_on_buy_button(self):
        self._click(self.locators.by_button_locator)

    def return_buy_button(self):
        return self.wait_until_element_appears(self.locators.by_button_locator)

    def return_in_stock_span(self):
        return self.wait_until_element_appears(self.locators.stock_label_locator)



