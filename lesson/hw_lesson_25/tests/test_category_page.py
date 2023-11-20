import time


def test_click_checkbox_ready_to_ship(dashboard):
    open_xiaomi = dashboard.open_xiaomi_category()
    open_xiaomi.checkbox_ready_to_ship()

def test_click_one_product(dashboard):
    open_xiaomi = dashboard.open_xiaomi_category()
    open_xiaomi.click_one_product()

def test_click_price_list(dashboard):
    open_xiaomi = dashboard.open_xiaomi_category()
    open_xiaomi.click_price_list()

def test_click_sort_new(dashboard):
    open_xiaomi = dashboard.open_xiaomi_category()
    open_xiaomi.click_sort_new()