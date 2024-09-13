import pytest

from pageObject.BasePage import BasePage
from pageObject.Loginpage import Loginpage
from tests.BaseTest import BaseTest
from utilities.customLogger import LogGen



class Test_navigate_custodial_screen(BaseTest):
    logger = LogGen.loggen()
    user_name = "OMS_OWNER"
    password = "oms_owner"
    last_name = "Python"
    first_name = "six"

    @pytest.mark.smoke
    def test_validate_Custodial_screen(self):
        self.logger.info("**********Test_03_Custodial order*********")
        self.logger.info("****Verifying Navigating to Custodial order screen***")
        homepage = Loginpage(self.driver)
        homepage.custom_sleep(5)
        homepage.enter_email_address(self.user_name)
        homepage.enter_password(self.password)
        homepage.custom_sleep(10)
        homepage.click_login_button()
        homepage.custom_sleep(5)
        homepage.navigate_to_custodial_screen()
        homepage.custom_sleep(5)
        expected_url = "https://qa.elitev5.com/#/OCDCORDS"
        # assert homepage.validate_cust_screen().__eq__(expected_url)
        if homepage.validate_cust_screen().__eq__(expected_url):
            assert True
            self.logger.info("********Verifying Navigating to Custodial order screen Test Passed***********")
        else:
            assert False
            self.logger.info("********Verifying Navigating to Custodial order screen Test Failed***********")



