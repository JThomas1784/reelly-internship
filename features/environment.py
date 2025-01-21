from app.application import Application
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_all(context):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    context.driver = webdriver.Chrome(options=chrome_options)
    context.driver.maximize_window()
    print(f"Running in headless mode: {chrome_options.arguments}")

    context.application = Application(context.driver)

def after_all(context):
    context.driver.quit()

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