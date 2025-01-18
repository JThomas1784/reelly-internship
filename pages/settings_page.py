from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class SettingsPage(BasePage):
    SETTINGS_MENU = (By.XPATH, "//*[@id='w-node-_99a5c496-8f77-9959-16dd-e8eb9b22b68b-9b22b68b']/div[1]/div[2]/div/a[15]/div[2]")
    VERIFICATION_OPTION = (By.XPATH, "/html/body/div[3]/div[2]/a[11]/div[2]")
    UPLOAD_IMAGE_BUTTON = (By.XPATH, "/html/body/div[3]/div/div[4]/label")
    NEXT_STEP_BUTTON = (By.XPATH, "/html/body/div[3]/div/a/div")

    def open_settings(self):
        self.driver.find_element(*self.SETTINGS_MENU).click()

    def open_verification(self):
        self.driver.find_element(*self.VERIFICATION_OPTION).click()

    def is_verification_page_open(self):
        return self.driver.current_url == "https://soft.reelly.io/verification/step-0"

    def are_buttons_present(self):
        upload_image_present = self.is_element_present(self.UPLOAD_IMAGE_BUTTON)
        next_step_present = self.is_element_present(self.NEXT_STEP_BUTTON)
        return upload_image_present and next_step_present
