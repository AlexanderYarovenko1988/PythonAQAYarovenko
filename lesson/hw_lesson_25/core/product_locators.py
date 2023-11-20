from lesson.hw_lesson_25.core.base_locators import BaseLocators


class ProductLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.by_button_locator = ("xpath", "//button[@id='product-buy-button']")
        self.stock_label_locator = ("xpath", "//p[@class='p-trade__stock-label']")