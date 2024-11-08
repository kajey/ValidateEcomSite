from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options
import time
import logging

# Set up logging to capture errors
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Setup WebDriver
@given('I visit the ecommerce site')
def step_impl(context):
    try:
        context.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
        context.driver.get("http://www.example-ecommerce-site.com")
        context.driver.maximize_window()
        logger.info("Successfully opened the ecommerce site.")
    except WebDriverException as e:
        logger.error(f"Error initializing WebDriver: {e}")
        raise AssertionError("WebDriver initialization failed.")
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}")
        raise AssertionError("An unexpected error occurred while visiting the ecommerce site.")

# Guest User Checkout
@when('I browse products and add them to the cart')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//a[text()='Product Category']").click()
        time.sleep(2)
        context.driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click()
        logger.info("Added products to the cart successfully.")
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}")
        raise AssertionError("Product category or add-to-cart button not found.")
    except Exception as e:
        logger.error(f"Unexpected error occurred while adding products to the cart: {e}")
        raise AssertionError("An unexpected error occurred while browsing products or adding to the cart.")

@when('I proceed to checkout as a guest')
def step_impl(context):
    try:
        context.driver.find_element(By.XPATH, "//button[text()='Checkout']").click()
        context.driver.find_element(By.XPATH, "//button[text()='Continue as Guest']").click()
        logger.info("Proceeded to checkout as a guest.")
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}")
        raise AssertionError("Checkout or continue as guest button not found.")
    except TimeoutException as e:
        logger.error(f"Timeout while waiting for element: {e}")
        raise AssertionError("Timeout while trying to proceed to checkout.")
    except Exception as e:
        logger.error(f"Unexpected error during checkout: {e}")
        raise AssertionError("An unexpected error occurred while proceeding to checkout as a guest.")

@then('I should see the order summary page')
def step_impl(context):
    try:
        # Check that the "Order Summary" page is displayed
        assert "Order Summary" in context.driver.title
        logger.info("Successfully navigated to the order summary page.")
    except AssertionError:
        logger.error("Order summary page not found.")
        raise AssertionError("Order summary page not found after checkout.")
    except Exception as e:
        logger.error(f"Unexpected error during order summary validation: {e}")
        raise AssertionError("An unexpected error occurred while validating the order summary page.")

# Registered User Checkout
@given('I am a registered user')
def step_impl(context):
    try:
        context.driver.get("http://www.example-ecommerce-site.com/login")
        logger.info("Navigated to the login page.")
    except WebDriverException as e:
        logger.error(f"Error opening login page: {e}")
        raise AssertionError("Error opening login page.")

@when('I log in with valid credentials')
def step_impl(context):
    try:
        context.driver.find_element(By.ID, "username").send_keys("testuser")
        context.driver.find_element(By.ID, "password").send_keys("password123")
        context.driver.find_element(By.ID, "login-button").click()
        logger.info("Logged in successfully.")
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}")
        raise AssertionError("Username, password field or login button not found.")
    except TimeoutException as e:
        logger.error(f"Timeout while logging in: {e}")
        raise AssertionError("Timeout while attempting to log in.")
    except Exception as e:
        logger.error(f"Unexpected error during login: {e}")
        raise AssertionError("An unexpected error occurred during login.")

@then('I should see the order summary page with pre-filled details')
def step_impl(context):
    try:
        assert "Order Summary" in context.driver.title
        assert "testuser" in context.driver.page_source
        logger.info("Order summary page with pre-filled details is displayed.")
    except AssertionError:
        logger.error("Order summary page or pre-filled details not found.")
        raise AssertionError("Order summary page or pre-filled details not found after login.")
    except Exception as e:
        logger.error(f"Unexpected error during validation of order summary page: {e}")
        raise AssertionError("An unexpected error occurred while validating the order summary page with pre-filled details.")

# Search for Product
@when('I search for "{product}"')
def step_impl(context, product):
    try:
        search_box = context.driver.find_element(By.NAME, "search")
        search_box.send_keys(product)
        search_box.send_keys(Keys.RETURN)
        logger.info(f"Searched for {product}.")
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}")
        raise AssertionError("Search box not found.")
    except Exception as e:
        logger.error(f"Unexpected error during search: {e}")
        raise AssertionError(f"An unexpected error occurred while searching for {product}.")

@then('I should see a list of matching products')
def step_impl(context):
    try:
        assert "wireless headphones" in context.driver.page_source
        logger.info("Matching products found in the search results.")
    except AssertionError:
        logger.error("Matching products not found in the search results.")
        raise AssertionError("No matching products found for the search query.")
    except Exception as e:
        logger.error(f"Unexpected error during search results validation: {e}")
        raise AssertionError("An unexpected error occurred while validating the search results.")

# Apply Invalid Coupon Code
@when('I apply an invalid coupon code')
def step_impl(context):
    try:
        context.driver.find_element(By.ID, "coupon_code").send_keys("INVALIDCODE")
        context.driver.find_element(By.ID, "apply_coupon").click()
        logger.info("Applied invalid coupon code.")
    except NoSuchElementException as e:
        logger.error(f"Element not found: {e}")
        raise AssertionError("Coupon code input or apply button not found.")
    except TimeoutException as e:
        logger.error(f"Timeout while applying coupon: {e}")
        raise AssertionError("Timeout while attempting to apply coupon.")
    except Exception as e:
        logger.error(f"Unexpected error while applying coupon: {e}")
        raise AssertionError("An unexpected error occurred while applying the coupon code.")

@then('I should see an error message saying "Invalid coupon code"')
def step_impl(context):
    try:
        error_message = context.driver.find_element(By.CLASS_NAME, "error-message").text
        assert "Invalid coupon code" in error_message
        logger.info("Error message for invalid coupon code is displayed.")
    except NoSuchElementException as e:
        logger.error(f"Error message element not found: {e}")
        raise AssertionError("Error message element not found.")
    except AssertionError:
        logger.error("Invalid coupon code error message not displayed.")
        raise AssertionError('Error message "Invalid coupon code" not found.')
    except Exception as e:
        logger.error(f"Unexpected error during invalid coupon validation: {e}")
        raise AssertionError("An unexpected error occurred while validating the invalid coupon code error message.")

# Close the browser after test completion
@then('I close the browser')
def step_impl(context):
    try:
        context.driver.quit()
        logger.info("Browser closed successfully.")
    except WebDriverException as e:
        logger.error(f"Error closing WebDriver: {e}")
        raise AssertionError("Error closing the browser.")
    except Exception as e:
        logger.error(f"Unexpected error occurred while closing the browser: {e}")
        raise AssertionError("An unexpected error occurred while closing the browser.")
