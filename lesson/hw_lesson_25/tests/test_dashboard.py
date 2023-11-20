import time


def test_click_on_smartphones_and_phones_category(dashboard):
    dashboard.choose_smartphones_and_phones_category()


def test_search_for_smartphones_and_phones_category(dashboard):
    dashboard.send_text_to_search_field("Xiaomi 13T 8/256 Alpine Black")


def test_open_the_product_on_the_home_page(dashboard):
    dashboard.open_the_product_on_the_home_page()


def test_open_xiaomi_category(dashboard):
    dashboard.open_xiaomi_category()


def test_click_on_shares(dashboard):
    dashboard.open_shares()


def test_buy_a_product(dashboard):
    dashboard.adding_item_to_cart("Xiaomi 13T 8/256 Alpine Black")


def test_click_filter_charging_stations(dashboard):
    dashboard.filter_charging_stations()


def test_all_results_products(dashboard):
    dashboard.all_results_products("Xiaomi 13T 8/256 Alpine Black")


def test_change_city(dashboard):
    dashboard.change_city_location("Баб'янка")
