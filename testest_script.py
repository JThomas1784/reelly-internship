import json
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# BrowserStack credentials
BROWSERSTACK_USERNAME = "jamontethomas_KpvXqZ"
BROWSERSTACK_ACCESS_KEY = "tqCSbysrv3uquAuKCHVY"


desired_cap = {
    'bstack:options': {
        "os": "Windows",
        "osVersion": "11",
        "local": "false",
        "seleniumVersion": "4.8.0",
        "buildName": "BrowserStack_Behave_Build",  # Name of the build
        "sessionName": "Test_Scenario",  # Name of the test session
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    },
    "browserName": "Chrome",
    "browserVersion": "latest"
}

options = webdriver.ChromeOptions()
options.set_capability("bstack:options", desired_capabilities["bstack:options"])
options.set_capability("browserName", desired_capabilities["browserName"])
options.set_capability("browserVersion", desired_capabilities["browserVersion"])

driver = webdriver.Remote(
    command_executor=f"https://{BROWSERSTACK_USERNAME}:{BROWSERSTACK_ACCESS_KEY}@hub-cloud.browserstack.com/wd/hub",
    desired_capabilities=desired_cap
)

executor_object = {
    "action": "setSessionStatus",
    "arguments": {
        "status": "passed",
        "reason": "Test completed successfully."
    }
}

browserstack_executor = 'browserstack_executor: {}'.format(json.dumps(executor_object))
driver.execute_script(browserstack_executor)

driver.quit()