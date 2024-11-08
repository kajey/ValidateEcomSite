from behave import given, when, then
from ValidateEcomSite.pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage

@given('the user is logged in')
def step_given_user_is_logged_in(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.login("testuser", "password")

@when('the user adds items to the cart and proceeds to checkout')
def step_when_user_adds_items_to_cart(context):
    context.checkout_page = CheckoutPage(context.driver)
    context.checkout_page.add_items_to_cart_and_checkout()

@then('the checkout process is completed successfully')
def step_then_checkout_completed(context):
    assert context.checkout_page.is_checkout_successful(), "Checkout process failed."
