from pages.main_page import MainPage
from pages.settings_page import SettingsPage

class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.settings_page = SettingsPage(self.driver)
