from behave import given, when, then
from selenium.webdriver.common.by import By
from pages.registration_page import RegistrationPage

@given('the user is on the registration page')
def step_given_user_on_registration_page(context):
    context.driver.get("https://www.example.com/registration")
    context.registration_page = RegistrationPage(context.driver)

@when('the user fills in valid registration details')
def step_when_user_registers(context):
    context.registration_page.fill_registration_form("user@example.com", "password123")
    context.registration_page.submit_form()

@then('the user should be redirected to the welcome page')
def step_then_user_redirected(context):
    assert context.driver.current_url == "https://www.example.com/welcome"
