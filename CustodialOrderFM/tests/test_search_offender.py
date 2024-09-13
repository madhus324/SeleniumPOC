import pytest

from pageObject.BasePage import BasePage
from pageObject.Loginpage import Loginpage
from pageObject.SearchOff import SearchOff
import time

from tests.BaseTest import BaseTest
from utilities.customLogger import LogGen



class Test_Search_offender(BaseTest):
    logger = LogGen.loggen()
    user_name = "MADHUM"
    password = "Admin@123"
    last_name = "Python"
    first_name = "six"

    @pytest.mark.smoke
    def test_search_offender(self):
        self.logger.info("**********Test_04_Login*********")
        self.logger.info("****Verifying offender in the header in Custodial order screen***")
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
        assert homepage.validate_cust_screen().__eq__(expected_url)
        search_off = SearchOff(self.driver)
        homepage.custom_sleep(5)
        search_off.click_on_search()
        search_off.enter_lastname(self.last_name)
        search_off.enter_firstname(self.first_name)
        search_off.search_offender()
        # assert search_off.assert_add_button
        if search_off.assert_add_button:
            assert True
            self.logger.info("****Verifying offender in the header -- Test Passed***")
        else:
            assert False
            self.logger.info("****Verifying offender in the header -- Test Failed***")



