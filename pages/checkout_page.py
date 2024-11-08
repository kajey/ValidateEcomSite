from selenium.webdriver.common.by import By

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.ID, "cart")
        self.checkout_button = (By.ID, "checkout")
        self.order_confirmation = (By.CLASS_NAME, "order-confirmation")

    def add_items_to_cart_and_checkout(self):
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.checkout_button).click()

    def is_checkout_successful(self):
        return len(self.driver.find_elements(*self.order_confirmation)) > 0
