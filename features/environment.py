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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# BrowserStack credentials
BROWSERSTACK_USERNAME = "jamontethomas_KpvXqZ"
BROWSERSTACK_ACCESS_KEY = "tqCSbysrv3uquAuKCHVY"

def get_browserstack_capabilities():
    return {
        "bstack:options": {
            "os": "Windows",
            "osVersion": "10",
            "local": "false",
            "seleniumVersion": "4.8.0",
            "userName": BROWSERSTACK_USERNAME,
            "accessKey": BROWSERSTACK_ACCESS_KEY
        },
        "browserName": "Chrome",
        "browserVersion": "latest"
    }


def before_scenario(context, scenario):
    options = Options()
    capabilities = get_browserstack_capabilities()
    for key, value in capabilities.items():
        options.set_capability(key, value)

    context.driver = webdriver.Remote(
        command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
        options=options
    )
    context.driver.maximize_window()


def after_scenario(context, scenario):
        if context.driver:
            context.driver.quit()