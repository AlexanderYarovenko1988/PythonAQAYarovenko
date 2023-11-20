from lesson.hw_lesson_25.core.base_locators import BaseLocators


class CategoryLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.check_box_ready_to_ship_locator = ("xpath", "//a[contains(text(),'Готовий до відправки')]")
        self.product_locator = ("xpath", "//div[@class='product-card']")
        self.header_locator = ("xpath", "//h1[contains(text(),'Смартфони Xiaomi')]")
        self.price_list_locator = ("xpath", "//li[@class='view-mode__item view-mode__item--pricelist']")
        self.new_locator = ("xpath", "//li[@title='новинки']")
        self.sort_current_locator = ("xpath", "//span[@class='sort-by__current']")
