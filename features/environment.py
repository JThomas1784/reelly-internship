# from app.application import Application
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options


# def before_all(context):
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--window-size=1920,1080")
#     chrome_options.add_argument("--no-sandbox")
#     chrome_options.add_argument("--disable-dev-shm-usage")
#
#     context.driver = webdriver.Chrome(options=chrome_options)
#     context.driver.maximize_window()
#     print(f"Running in headless mode: {chrome_options.arguments}")
#
#     context.application = Application(context.driver)
#
# def after_all(context):
#     context.driver.quit()

# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
#
# def before_all(context):
#     firefox_options = Options()
#     firefox_options.add_argument("--headless")
#     firefox_options.add_argument("--window-size=1920,1080")
#
#     context.driver = webdriver.Firefox(options=firefox_options)
#     context.driver.maximize_window()
#
# def after_all(context):
#     context.driver.quit()

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# BrowserStack credentials
username = "jamontethomas_KpvXqZ"
access_key = "tqCSbysrv3uquAuKCHVY"

desired_cap = {
'browser': 'Chrome',
'browser_version': 'latest',
'os': 'Windows',
'os_version': '10',
'name': 'Python Selenium BrowserStack Test'
}

url = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"

@pytest.fixture(scope="function")
defdriver():
    driver = webdriver.Remote(
        command_executor=url,
        desired_capabilities=desired_cap
)
yield driver
    driver.quit()

deftest_browserstack(driver):
    driver.get("https://www.browserstack.com")

assert"BrowserStack"in driver.title
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("Selenium Python")
    search_box.send_keys(Keys.RETURN)

assert"Selenium"in driver.page_source