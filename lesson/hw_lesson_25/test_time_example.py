import time
from selenium.webdriver import Firefox
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.wheel_actions import WheelActions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def test_01():
    driver = Firefox()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get("https://allo.ua/")
    btn_locator_xpath = "//div[@class='ct-button']"
    btn_click = driver.find_element("xpath", btn_locator_xpath)
    btn_click.click()
    driver.quit()

def test_02():
    driver = Firefox()
    driver.maximize_window()
    web_driver_wait = WebDriverWait(driver, 10)

    driver.get("https://allo.ua/")
    btn_locator_xpath = "//div[@class='ct-button']"
    btn_click = web_driver_wait.until(EC.presence_of_element_located(("xpath", btn_locator_xpath)))
    btn_click.click()
    driver.quit()
