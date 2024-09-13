from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    logout_xpath = "(//mat-icon[normalize-space()='logout'])[1]"

    def logout(self):
        log_out = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.logout_xpath)))
        log_out.click()

    def type_into_element(self, text, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        element.send_keys(text)

    def element_click(self, locator_name, locator_value):
        element = self.get_element(locator_name, locator_value)
        # element.is_displayed()
        element.click()

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.endswith("_xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.endswith("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.endswith("_linktext"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.endswith("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.endswith("_classname"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        return element
    #
    # def get_element(self, locator_name, locator_value, timeout=10):
    #     element = None
    #     locator_strategy = self.get_locator_strategy(locator_name)
    #
    #     if locator_strategy:
    #         try:
    #             element = WebDriverWait(self.driver, timeout).until(
    #                 EC.presence_of_element_located((locator_strategy, locator_value))
    #             )
    #         except Exception as e:
    #             print(f"Element not found within {timeout} seconds. Error: {e}")
    #
    #     return element
    #
    # def get_locator_strategy(self, locator_name):
    #     locator_name = locator_name.lower()
    #
    #     if locator_name.endswith("_xpath"):
    #         return By.XPATH
    #     elif locator_name.endswith("_name"):
    #         return By.NAME
    #     elif locator_name.endswith("_linktext"):
    #         return By.LINK_TEXT
    #     elif locator_name.endswith("_id"):
    #         return By.ID
    #     elif locator_name.endswith("_classname"):
    #         return By.CLASS_NAME
    #
    #     return None
