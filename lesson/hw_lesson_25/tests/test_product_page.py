import time


def test_buy_product(dashboard):
    open_xiaomi = dashboard.open_xiaomi_category()
    product = open_xiaomi.click_one_product()
    product.add_cookie_brownie()
    product.click_on_buy_button()

def test_product_in_stock_and_buy_button_exist(dashboard):
    open_xiaomi = dashboard.open_xiaomi_category()
    product = open_xiaomi.click_one_product()
    assert product.return_buy_button().text == "Купити"
    assert product.return_in_stock_span().text == "✓ У магазинах Алло"

def test_cookies_and_local_storage(dashboard):
    open_xiaomi = dashboard.open_xiaomi_category()
    product = open_xiaomi.click_one_product()

    # Приклад встановлення та отримання кукі
    product.cookies.set_cookie('example_cookie', 'cookie_value')
    retrieved_cookie = product.cookies.get_cookie('example_cookie')
    print(f"Retrieved cookie value: {retrieved_cookie['value']}")
    assert retrieved_cookie['value'] == 'cookie_value'

    # Приклад встановлення та отримання значення з локального сховища
    product.local_storage.set_item('example_key', 'example_value')
    retrieved_value = product.local_storage.get_item('example_key')
    print(f"Retrieved value from local storage: {retrieved_value}")
    assert retrieved_value == 'example_value'