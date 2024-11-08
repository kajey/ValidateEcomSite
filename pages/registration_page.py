from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_field = (By.ID, "email")
        self.password_field = (By.ID, "password")
        self.submit_button = (By.ID, "submit")

    def fill_registration_form(self, email, password):
        self.driver.find_element(*self.email_field).send_keys(email)
        self.driver.find_element(*self.password_field).send_keys(password)

    def submit_form(self):
        self.driver.find_element(*self.submit_button).click()
