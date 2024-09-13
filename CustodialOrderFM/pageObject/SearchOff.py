from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.core import driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

from pageObject.BasePage import BasePage


class SearchOff(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    search_button_xpath = "//mat-icon[normalize-space()='search']"
    enter_lastname_xpath = "//input[@id='SBlnme']"
    enter_firstname_xpath = "//input[@id='SBfnme']"
    click_search_xpath = "//button[@id='SBsrchbtn']"
    add_cust_xpath = "//button[@class='court-btn controls-btn add-btn']"
    off_lastnme_xpath = "//span[@id='HBlnme']"

    def click_on_search(self):
        self.element_click("search_button_xpath", self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()

    def enter_lastname(self, lastname):
        self.type_into_element(lastname, "enter_lastname_xpath", self.enter_lastname_xpath)

        # self.driver.find_element(By.XPATH, self.enter_lastname_xpath).send_keys(lastname)

    def enter_firstname(self, firstname):
        self.type_into_element(firstname, "enter_firstname_xpath", self.enter_firstname_xpath)

        # self.driver.find_element(By.XPATH, self.enter_firstname_xpath).send_keys(firstname)

    def search_offender(self):
        self.element_click("click_search_xpath", self.click_search_xpath)

        # self.driver.find_element(By.XPATH, self.click_search_xpath).click()

    def assert_add_button(self):
        self.element_click("add_cust_xpath", self.add_cust_xpath)

        # self.driver.find_element(By.XPATH, self.add_cust_xpath).click

    def retreive_actual_name(self):
        act_lstname = self.driver.find_element(By.XPATH, self.off_lastnme_xpath).text
        return act_lstname

