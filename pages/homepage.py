from selenium.webdriver.common.by import By

class Homepage:
    def __init__(self, driver):
        self.driver = driver
        self.search_box = (By.NAME, "q")
        self.search_button = (By.XPATH, "//button[@type='submit']")
        self.search_results = (By.CLASS_NAME, "search-results")

    def search_for_product(self, product_name):
        self.driver.find_element(*self.search_box).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

    def is_search_results_displayed(self):
        return len(self.driver.find_elements(*self.search_results)) > 0
