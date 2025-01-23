import allure
from appium.webdriver.extensions import settings
from behave import given, when, then
from pages.main_page import MainPage
from pages.settings_page import SettingsPage

@given("the user is on the main page")
@allure.step("the user is on the main page")
def step_open_main_page(context):
    context.main_page = MainPage(context.driver)
    context.main_page.open()

@when("the user logs in with valid credentials")
def step_user_logs_in(context):
    context.application.main_page.login("jamonte.thomas17@gmail.com", "9#p9PW6bLVCF8gt")

@when('the user clicks on "settings" in the left menu')
@allure.step("the user clicks on 'settings' in the left menu")
def step_user_clicks_settings(context):
    context.settings_page = SettingsPage(context.driver)
    context.application.settings_page.open_settings()

@when('the user clicks on the "verification" option')
def step_user_clicks_verification(context):
    context.settings_page.open_verification()

@then("the verification page should open")
def step_verify_verification_page(context):
    assert context.settings_page.is_verification_page_open(), "Verification page did not open."

@then('"upload image" and "Next step" buttons should be available')
def step_verify_buttons(context):
    assert context.settings_page.are_buttons_present(), "'Upload image' or 'Next step' buttons are missing."
