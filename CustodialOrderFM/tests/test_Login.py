import pytest
from pageObject.Loginpage import Loginpage
from tests.BaseTest import BaseTest
from utilities import ExcelUtils
from utilities.customLogger import LogGen

class TestLogin(BaseTest):

    logger = LogGen.loggen()
    user_name = "OMS_OWNER"
    password = "oms_owner"
    last_name = "Python"
    first_name = "six"

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_with_valid_credentials(self):
        self.logger.info("**********Test_01_Login*********")
        self.logger.info("****Verifying Login Page***")
        homepage = Loginpage(self.driver)
        homepage.custom_sleep(10)
        homepage.enter_email_address(self.user_name)
        homepage.enter_password(self.password)
        homepage.custom_sleep(10)
        homepage.click_login_button()
        homepage.custom_sleep(5)
        assert homepage.main_menu_link()
        if homepage.main_menu_link():
            assert True
            self.logger.info("****Login test passed ****")
        else:
            self.logger.info("****Login test failed ****")
            assert False
        homepage.logout()


    @pytest.mark.regression
    def test_login_with_invalid_credentials(self):
        self.logger.info("**********Test_02_Login*********")
        self.logger.info("****Verifying Invalid Login details test****")

        homepage = Loginpage(self.driver)
        homepage.custom_sleep(10)
        homepage.enter_email_address(self.user_name)
        homepage.enter_password("password")
        homepage.custom_sleep(10)
        homepage.click_login_button()
        homepage.custom_sleep(3)
        expected_url = "https://qa.elitev5.com/#/login"
        if homepage.validate_cust_screen() == (expected_url):
            assert True
            self.logger.info("****Invalid Login cred test Passed ****")
        else:
            assert False
            self.logger.info("****Invalid Login cred test Failed ****")
        # homepage.logout()

        # expected_msg = "Invalid username or password, please try again."
        # actual_msg = homepage.retreive_toast_message().text
        # if actual_msg == expected_msg:
        #     assert True
        #     self.logger.info("****Login test Passed ****")
        # else:
        #     assert False
        #     self.logger.info("****Login test Failed ****")
        #     self.logger.error("****Login test Failed ****")
        #     logging.exception("Detailed error information:")







