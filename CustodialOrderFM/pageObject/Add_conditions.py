from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.BasePage import BasePage


class AddConditions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    click_navi_condi_tab_xpath = "//div[contains(text(),'Conditions')]"
    click_add_condi_xpath = "//span[normalize-space()='Add Conditions']"
    condi_category_xpath = "(//input[@id='code'])[1]"
    select_category_lov_xpath = "(//div[@class='lov-option-row']//div)[1]"
    click_retreive_condi_xpath = "//span[normalize-space()='Retrieve']"
    select_one_condi_xpath = "(//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin'])[2]"
    save_condi_xpath = "//s4-button[@name='crtschdleclr']"
    # success_msg_xpath = "//h3[text()='Success!']"
    retreive_toast_msg = "//div[@class='toastContainer ng-star-inserted']//p[1]"


    def add_conditions(self):
        self.element_click("click_navi_condi_tab_xpath", self.click_navi_condi_tab_xpath)
        self.custom_sleep(2)
        self.element_click("click_add_condi_xpath", self.click_add_condi_xpath)
        self.custom_sleep(2)
        self.element_click("condi_category_xpath", self.condi_category_xpath)
        self.custom_sleep(2)
        self.element_click("select_category_lov_xpath", self.select_category_lov_xpath)
        self.custom_sleep(2)
        self.element_click("click_retreive_condi_xpath", self.click_retreive_condi_xpath)
        self.custom_sleep(4)
        self.element_click("select_one_condi_xpath", self.select_one_condi_xpath)
        self.custom_sleep(2)
        self.element_click("save_condi_xpath", self.save_condi_xpath)
        self.custom_sleep(2)

    def custom_sleep(self, seconds):
        time.sleep(seconds)

    def success_message(self):
        toast_msg = self.driver.find_element(By.XPATH, self.retreive_toast_msg).text
        return toast_msg

