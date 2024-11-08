Ecommerce Test Automation Framework
This project is a test automation framework for an eCommerce website, built using Selenium WebDriver and Behave (a BDD framework). It automates key eCommerce functionalities like user login, guest checkout, searching products, applying discount coupons, and order confirmation.

Features
BDD Testing with Behave: Test cases written in Gherkin syntax for easy collaboration with non-developers.
Selenium WebDriver: Automates the browser interactions with real user scenarios.
Multiple Browsers Support: Works with any browser that Selenium WebDriver supports (e.g., Chrome, Firefox).
Headless Mode: Can run tests in headless mode for faster execution on CI servers.
Project Structure
bash
Copy code
ecommerce-test-framework/
│
├── features/
│   ├── steps/
│   │   └── test_steps.py    # Step definitions (Python implementation)
│   └── ecommerce.feature    # Gherkin test cases
├── drivers/
│   └── chromedriver         # WebDriver executable (e.g., ChromeDriver)
├── config/
│   └── settings.py          # Configuration file for WebDriver, URLs, etc.
└── requirements.txt         # Required packages (Selenium, Behave, etc.)
Prerequisites
Python 3.x: The framework is built using Python.
WebDriver: Ensure that the appropriate WebDriver for your browser (e.g., ChromeDriver for Chrome) is downloaded and available in the drivers/ folder.
Packages: This framework requires several Python packages, which can be installed via pip.
Setup Instructions
1. Install Python Packages
Before running the tests, you need to install the required dependencies. Run the following command to install all required packages:

bash
Copy code
pip install -r requirements.txt
If you don't have the requirements.txt file, you can manually install the necessary packages with:

bash
Copy code
pip install selenium behave
2. Download WebDriver
Ensure that the WebDriver executable for your browser is available in the drivers/ folder.

ChromeDriver: Download ChromeDriver
GeckoDriver: Download GeckoDriver
Place the downloaded driver in the drivers/ folder, or update the path in test_steps.py where the driver is initialized.

3. Configure WebDriver Settings (Optional)
You can configure WebDriver options (e.g., headless mode) in config/settings.py. By default, the Chrome WebDriver is used, but you can switch to another browser if necessary.

4. Set Up Your Environment Variables (Optional)
If you plan to use environment-specific configurations (such as different URLs or credentials), you can store them in environment variables or configuration files.

Running the Tests
1. Running All Tests
To run all the tests, simply use the following command from the root of the project:

bash
Copy code
behave
This will run all the tests defined in the features/ folder.

2. Running Specific Feature
To run a specific feature (e.g., the ecommerce feature), you can specify the feature file like so:

bash
Copy code
behave features/ecommerce.feature
3. Running Tests in Headless Mode (Optional)
To run the tests in headless mode (i.e., without opening a browser window), modify the test_steps.py file to include the --headless flag in the Chrome options. Here's an example:

python
Copy code
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--headless")
context.driver = webdriver.Chrome(executable_path="drivers/chromedriver", options=options)
Alternatively, you can configure headless mode directly from the config/settings.py file.

Writing Tests
Test cases are written in Gherkin syntax in .feature files located in the features/ folder. Each test case consists of Given, When, and Then steps.

Example:
features/ecommerce.feature
gherkin
Copy code
Feature: Ecommerce site validation

  Scenario: Guest User Checkout
    Given I visit the ecommerce site
    When I browse products and add them to the cart
    And I proceed to checkout as a guest
    Then I should see the order summary page

  Scenario: Registered User Login and Checkout
    Given I am a registered user
    And I log in with valid credentials
    When I browse products and add them to the cart
    And I proceed to checkout
    Then I should see the order summary page with pre-filled details
Step Definitions
Each step from the .feature file is implemented as a function in test_steps.py. Here’s an example of how to define the step for a scenario where the user visits the eCommerce site:

features/steps/test_steps.py
python
Copy code
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Given step: Visit the ecommerce site
@given('I visit the ecommerce site')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="drivers/chromedriver")
    context.driver.get("http://www.example-ecommerce-site.com")
    context.driver.maximize_window()

# When step: Add products to cart
@when('I browse products and add them to the cart')
def step_impl(context):
    context.driver.find_element(By.XPATH, "//a[text()='Product Category']").click()
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[text()='Add to Cart']").click()

# Then step: Verify the order summary page
@then('I should see the order summary page')
def step_impl(context):
    assert "Order Summary" in context.driver.title
    context.driver.quit()
Running the Tests in Parallel (Optional)
For faster execution, you can run tests in parallel using the pytest-xdist plugin. For example:

bash
Copy code
pip install pytest-xdist
pytest -n 4
This will run the tests using 4 processes in parallel, reducing the overall execution time.

Test Reporting
You can generate test reports in various formats (e.g., HTML, JSON) by configuring Behave to use a formatter.

bash
Copy code
behave --format html --outfile report.html
Contribution Guidelines
Feel free to contribute to this project! Here’s how you can help:

Fork the repository.
Clone your fork.
Create a feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -am 'Add your feature').
Push to the branch (git push origin feature/your-feature).
Create a new pull request.
License
This project is licensed under the MIT License - see the LICENSE file for details.

