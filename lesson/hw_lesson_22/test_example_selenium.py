import time
from selenium.webdriver import Firefox
import unittest


class TestSauceDemo(unittest.TestCase):

    def test_01_login(self):
        driver = Firefox()
        self.login(driver)
        driver.quit()

    def test_02_sort_by_name(self):
        driver = Firefox()
        btn_sort_name_xpath = "//select[@class='product_sort_container']"
        btn_option_xpath = "//option[@value='lohi']"

        self.login(driver)
        btn_sort = driver.find_element(by="xpath", value=btn_sort_name_xpath)
        btn_option = driver.find_element(by="xpath", value=btn_option_xpath)

        btn_sort.click()
        btn_option.click()
        assert "Price (low to high)" in driver.find_element(by="xpath",
                                                            value="//select[@class='product_sort_container']").text
        driver.quit()

    def test_03_open_product_card(self):
        driver = Firefox()
        product_xpath = "//div[normalize-space()='Sauce Labs Backpack']"

        self.login(driver)
        product = driver.find_element(by="xpath", value=product_xpath)
        product.click()
        assert "Back to products" in driver.find_element(by="xpath", value="//button[@id='back-to-products']").text
        driver.quit()

    def test_04_click_add_cart(self):
        driver = Firefox()
        btn_add_cart_xpath = "//button[@id='add-to-cart-sauce-labs-backpack']"
        self.login(driver)
        product = driver.find_element(by="xpath", value=btn_add_cart_xpath)
        product.click()
        assert "Remove" in driver.find_element(by="xpath", value="//button[@id='remove-sauce-labs-backpack']").text
        driver.quit()

    def test_5_go_to_cart(self):
        driver = Firefox()
        btn_cart_xpath = "//a[@class='shopping_cart_link']"

        self.login(driver)
        btn_cart = driver.find_element(by="xpath", value=btn_cart_xpath)
        btn_cart.click()
        assert "Description" in driver.find_element(by="xpath", value="//div[@class='cart_desc_label']").text
    def login(self, driver):
        driver.get("https://www.saucedemo.com/")
        txt_login_xpath = "//input[@id='user-name']"
        txt_password_xpath = "//input[@id='password']"
        btn_login_xpath = "//input[@id='login-button']"

        login = driver.find_element(by="xpath", value=txt_login_xpath)
        password = driver.find_element(by="xpath", value=txt_password_xpath)
        button_login = driver.find_element(by="xpath", value=btn_login_xpath)
        login.send_keys("standard_user")
        password.send_keys("secret_sauce")
        button_login.click()
        assert "Swag Labs" in driver.find_element(by="xpath", value="//div[@class='app_logo']").text


if __name__ == "__main__":
    unittest.main()
