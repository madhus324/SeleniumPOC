import pytest
from pageObject.Loginpage import Loginpage
from pageObject.SearchOff import SearchOff
from pageObject.Add_Cust_record import AddcustodialRecord
import time

from tests.BaseTest import BaseTest
from utilities.customLogger import LogGen


class Test_toasts(BaseTest):

    logger = LogGen.loggen()
    user_name = "MADHUM"
    password = "Admin@123"
    last_name = "Python"
    first_name = "seven"

    def insert_offender(self):
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

    @pytest.mark.regression
    def test_orderdate_toast(self):
        self.insert_offender()
        self.logger.info("**********Test_07_Login*********")
        self.logger.info("****Verifying Order Date toast warning messages in Custodial order screen***")
        add_cust_ord = AddcustodialRecord(self.driver)
        add_cust_ord.click_add_btn()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.enter_order_date(" ")
        add_cust_ord.custom_sleep(3)
        add_cust_ord.save_calculate()
        add_cust_ord.custom_sleep(3)
        exp_msg = "Please select Ordered Date"
        # assert add_cust_ord.success_message().__eq__(exp_msg)
        if add_cust_ord.success_message().__eq__(exp_msg):
            assert True
            self.logger.info("****Verifying Order Date messages -- Test Passed***")
        else:
            assert False
            self.logger.info("****Verifying Order Date messages -- Test Failed***")


    @pytest.mark.regression
    def test_court_toast(self):
        self.insert_offender()
        self.logger.info("**********Test_08_Login*********")
        self.logger.info("****Verifying Court field toast warning messages in Custodial order screen***")
        add_cust_ord = AddcustodialRecord(self.driver)
        add_cust_ord.click_add_btn()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.enter_order_date("10/01/2024")
        add_cust_ord.custom_sleep(3)
        add_cust_ord.save_calculate()
        add_cust_ord.custom_sleep(3)
        exp_msg = "Please select Court"
        # assert add_cust_ord.success_message().__eq__(exp_msg)
        if add_cust_ord.success_message().__eq__(exp_msg):
            assert True
            self.logger.info("****Verifying Court Field messages -- Test Passed***")
        else:
            assert False
            self.logger.info("****Verifying Court Field messages -- Test Failed***")

    @pytest.mark.regression
    def test_Type_toast(self):
        self.insert_offender()
        self.logger.info("**********Test_09_Login*********")
        self.logger.info("****Verifying Type field toast warning messages in Custodial order screen***")
        add_cust_ord = AddcustodialRecord(self.driver)
        add_cust_ord.click_add_btn()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.enter_order_date("10/01/2024")
        add_cust_ord.custom_sleep(3)
        add_cust_ord.enter_court()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.save_calculate()
        add_cust_ord.custom_sleep(3)
        exp_msg = "Please select Type"
        # assert add_cust_ord.success_message().__eq__(exp_msg)
        if add_cust_ord.success_message().__eq__(exp_msg):
            assert True
            self.logger.info("****Verifying Type Field messages -- Test Passed***")
        else:
            assert False
            self.logger.info("****Verifying Type Field messages -- Test Failed***")


    @pytest.mark.regression
    def test_commenceDate_toast(self):
        self.insert_offender()
        self.logger.info("**********Test_10_Login*********")
        self.logger.info("****Verifying Commence Date toast warning messages in Custodial order screen***")
        add_cust_ord = AddcustodialRecord(self.driver)
        add_cust_ord.click_add_btn()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.enter_order_date("10/01/2024")
        add_cust_ord.custom_sleep(3)
        add_cust_ord.enter_court()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.enter_type()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.save_calculate()
        add_cust_ord.custom_sleep(3)
        exp_msg = "Please select Commence Type"
        # assert add_cust_ord.success_message().__eq__(exp_msg)
        if add_cust_ord.success_message().__eq__(exp_msg):
            assert True
            self.logger.info("****Verifying Commence Date messages -- Test Passed***")
        else:
            assert False
            self.logger.info("****Verifying Commence Date messages -- Test Failed***")

