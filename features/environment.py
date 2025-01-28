import os
from selenium import webdriver
from browserstack.local import Local

bs_local = None


def before_all(context):
    """
    Setup steps to be executed before all scenarios.
    This includes initializing BrowserStack, Allure, and Selenium configurations.
    """
    global bs_local


    allure_environment_path = os.path.join(os.getcwd(), "allure_reports", "environment.properties")
    os.makedirs(os.path.dirname(allure_environment_path), exist_ok=True)
    with open(allure_environment_path, "w") as env_file:
        env_file.write("Browser=Chrome\n")
        env_file.write("Device=Nexus 5\n")
        env_file.write("Platform=Local\n")


    if os.getenv("USE_BROWSERSTACK", "false").lower() == "true":

        desired_cap = {
            'os': os.getenv("BROWSERSTACK_OS", "Windows"),
            'os_version': os.getenv("BROWSERSTACK_OS_VERSION", "10"),
            'browser': os.getenv("BROWSERSTACK_BROWSER", "Chrome"),
            'browser_version': os.getenv("BROWSERSTACK_BROWSER_VERSION", "latest"),
            'name': 'BStack-[Behave] Test',
            'browserstack.local': os.getenv("BROWSERSTACK_LOCAL", "false").lower(),
            'browserstack.debug': 'true',
            'browserstack.video': 'true'
        }


        if desired_cap['browserstack.local'] == "true":
            bs_local = Local()
            bs_local_args = {"key": os.getenv("BROWSERSTACK_ACCESS_KEY")}
            bs_local.start(**bs_local_args)


        context.driver = webdriver.Remote(
            command_executor=f"http://{os.getenv('BROWSERSTACK_USERNAME')}:{os.getenv('BROWSERSTACK_ACCESS_KEY')}@hub.browserstack.com/wd/hub",
            desired_capabilities=desired_cap
        )
        print("Running tests on BrowserStack...")

    else:

        mobile_emulation = {"deviceName": os.getenv("MOBILE_DEVICE", "Pixel 2")}
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)


        context.driver = webdriver.Chrome(options=chrome_options)
        print("Running tests locally with mobile emulation...")


def before_scenario(context, scenario):
    """
    Actions to perform before each scenario.
    Custom driver configurations based on scenario tags.
    """
    if "mobile" in scenario.tags:
        print(f"Mobile emulation enabled for scenario: {scenario.name}")
    else:
        print(f"Running scenario: {scenario.name}")


def after_scenario(context, scenario):
    """
    Tear down after each scenario.
    Capture screenshots for failed scenarios and attach to Allure reports.
    """
    if scenario.status == "failed":
        screenshot_path = f"screenshots/{scenario.name.replace(' ', '_')}.png"
        context.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved to: {screenshot_path}")


def after_all(context):
    """
    Tear down steps to be executed after all scenarios.
    Close WebDriver and stop BrowserStack Local.
    """
    if context.driver:
        context.driver.quit()
        print("WebDriver closed.")

    global bs_local
    if bs_local and bs_local.isRunning():
        bs_local.stop()
        print("BrowserStack Local stopped.")
