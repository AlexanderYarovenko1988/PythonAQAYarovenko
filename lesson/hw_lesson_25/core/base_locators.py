class BaseLocators:
    def __init__(self):
        self.login = ("xpath", "//div[@class='mh-profile']")
        self.banner = ("xpath", "//a[@class='v-logo']")
        self.contacts = ("xpath", "//div[@class='mh-phone']")
