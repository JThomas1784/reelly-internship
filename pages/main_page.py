from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    URL = "https://soft.reelly.io"
    LOGIN_USERNAME = (By.XPATH, "//*[@id='email-2']")
    LOGIN_PASSWORD = (By.XPATH, "//*[@id='field']")
    LOGIN_BUTTON = (By.ID, "//*[@id='wf-form-Sign-up']/a")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        self.driver.find_element(*self.LOGIN_USERNAME).send_keys(username)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
