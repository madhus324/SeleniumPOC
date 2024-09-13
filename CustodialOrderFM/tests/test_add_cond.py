import pytest

from pageObject.BasePage import BasePage
from pageObject.Loginpage import Loginpage
from pageObject.SearchOff import SearchOff
import time
from pageObject.Add_conditions import AddConditions

from tests.BaseTest import BaseTest
from utilities.customLogger import LogGen



class Test_Add_Conditions(BaseTest):
    logger = LogGen.loggen()
    user_name = "MADHUM"
    password = "Admin@123"
    last_name = "Python"
    first_name = "six"

    @pytest.mark.regression
    def test_add_condition(self):
        self.logger.info("**********Test_06_Login*********")
        self.logger.info("****Verifying Search Offender Page***")

        homepage = Loginpage(self.driver)
        homepage.custom_sleep(5)
        homepage.enter_email_address(self.user_name)
        homepage.enter_password(self.password)
        homepage.custom_sleep(10)
        homepage.click_login_button()
        homepage.custom_sleep(5)
        homepage.navigate_to_custodial_screen()
        homepage.custom_sleep(5)
        search_off = SearchOff(self.driver)
        homepage.custom_sleep(5)
        search_off.click_on_search()
        search_off.enter_lastname(self.last_name)
        search_off.enter_firstname(self.first_name)
        search_off.search_offender()
        homepage.custom_sleep(5)
        add_cond = AddConditions(self.driver)
        add_cond.add_conditions()
        exp_msg = "Record(s) saved"
        # assert add_cond.success_message().__eq__(exp_msg)
        if add_cond.success_message().__eq__(exp_msg):
            assert True
            self.logger.info("****Search Offender Page test passed***")
        else:
            assert False
            self.logger.info("****Search Offender Page test failed***")












