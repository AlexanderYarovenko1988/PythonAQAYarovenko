from lesson.hw_lesson_25.core.base_locators import BaseLocators


class DashBoardLocators(BaseLocators):
    def __init__(self):
        super().__init__()
        self.top_products = ("xpath", "//a[@class='v-pt__link'][contains(text(),'ТОП товари')]")
        self.washing_machines = ("xpath", "//a[@aria-label='Пральні машини']")
        self.TVs = ("xpath", "//div[@data-products-type='top']//a[@aria-label='Телевізори'][contains(text(),'Телевізори')]")
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

