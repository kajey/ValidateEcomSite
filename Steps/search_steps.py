from behave import given, when, then
from ValidateEcomSite.pages.homepage import Homepage

@given('the user is on the homepage')
def step_given_user_on_homepage(context):
    context.driver.get("https://www.amazon.co.in")
    context.homepage = Homepage(context.driver)

@when('the user searches for "{product_name}"')
def step_when_user_searches_for_product(context, product_name):
    context.homepage.search_for_product(product_name)

@then('the search results page displays relevant products')
def step_then_search_results_display(context):
    assert context.homepage.is_search_results_displayed(), "Search results are not displayed."
