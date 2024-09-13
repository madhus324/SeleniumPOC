from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.BasePage import BasePage

class Loginpage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    username_xpath = "//input[@id='lngtxtfld']"
    password_xpath = "//input[@id='lngpwdfld']"
    login_xpath = "(//span[@class='mat-button-wrapper'])[1]"
    main_menu_xpath = "//mat-icon[starts-with(@class,'mat-icon notranslate matIcon')]"
    retreive_invalid_login_cred_xpath = "//div[@class='toastContainer ng-star-inserted']//p[1]"
    # retreive_invalid_login_cred_xpath = "// h3[text() = 'Error!']"
    inmatecsmg_xpath = "(//span[@class='mat-line dynamic-menu-text'][normalize-space()='Modules'])[1]"
    inmatecsmg_modules_xpath = "(//a)[13]"
    legals_modules_xpath = "//span[contains(text(),'Legals/Sentence Calculation')]"
    cust_navi_xpath = "(//span[@class='mat-line dynamic-menu-text'][normalize-space()='Custodial Orders'])[1]"
    custodial_header_xpath = "//div[@class='mat-tooltip-trigger s4-tooltip-host']"



    def enter_email_address(self, username_text):
        # self.type_into_element(username_text, "username_xpath", self.username_xpath)

        # self.driver.find_element(By.XPATH, self.username_xpath).send_keys(username_text)
        username = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.username_xpath)))
        username.clear()
        username.send_keys(username_text)

    def enter_password(self, password_text):
        # self.type_into_element(password_text, "password_xpath", self.password_xpath)

       # self.driver.find_element(By.XPATH, self.password_xpath).send_keys(password_text)
        password = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.password_xpath)))
        password.clear()
        password.send_keys(password_text)

    def click_login_button(self):
        self.element_click("login_xpath", self.login_xpath)
        # element = self.driver.find_element(By.XPATH, self.login_xpath).click()
        login = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_xpath)))
        login.click()

    def main_menu_link(self):
        # return self.driver.find_element(By.XPATH, self.main_menu_xpath).is_displayed()
        menu_link = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.main_menu_xpath)))
        return menu_link


    def retreive_toast_message(self):
        act_msg = self.driver.find_element(By.XPATH, self.retreive_invalid_login_cred_xpath).text
        return act_msg.text

    def custom_sleep(self, seconds):
        time.sleep(seconds)

    def navigate_to_custodial_screen(self):
        self.element_click("main_menu_xpath", self.main_menu_xpath)
        self.custom_sleep(5)
        self.element_click("inmatecsmg_xpath", self.inmatecsmg_xpath)
        self.element_click("inmatecsmg_modules_xpath", self.inmatecsmg_modules_xpath)
        self.element_click("legals_modules_xpath", self.legals_modules_xpath)
        self.element_click("cust_navi_xpath", self.cust_navi_xpath)

        # self.driver.find_element(By.XPATH, self.main_menu_xpath).click()
        # self.custom_sleep(5)
        # self.driver.find_element(By.XPATH, self.inmatecsmg_xpath).click()
        # self.driver.find_element(By.XPATH, "(//a)[13]").click()
        # self.driver.find_element(By.XPATH, self.legals_modules_xpath).click()
        # self.driver.find_element(By.XPATH, self.cust_navi_xpath).click()

    def validate_cust_screen(self):
        current_url = self.driver.current_url
        return current_url






