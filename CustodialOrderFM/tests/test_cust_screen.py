from datetime import datetime, timedelta
import pytest
from pageObject.Loginpage import Loginpage
from pageObject.SearchOff import SearchOff
from pageObject.Add_Cust_record import AddcustodialRecord
from tests.BaseTest import BaseTest
from utilities.customLogger import LogGen


class Test_add_custodial(BaseTest):
    logger = LogGen.loggen()
    user_name = "MADHUM"
    password = "Admin@123"
    last_name = "Luther"
    first_name = "two"
    today_date = datetime.now().strftime("%d-%m-%Y")
    print(today_date)
    future_date = datetime.now() + timedelta(days=7)
    formatted_future_date = future_date.strftime("%d/%m/%Y")

    # @pytest.mark.regression
    def test_add_record_offender(self):
        self.logger.info("**********Test_05_Login*********")
        self.logger.info("****Verifying Custodial order screen***")
        homepage = Loginpage(self.driver)
        homepage.custom_sleep(5)
        homepage.enter_email_address(self.user_name)
        homepage.enter_password(self.password)
        homepage.custom_sleep(10)
        homepage.click_login_button()
        homepage.custom_sleep(10)
        homepage.navigate_to_custodial_screen()
        homepage.custom_sleep(5)
        # expected_url = "https://qa.elitev5.com/#/OCDCORDS"
        # assert homepage.validate_cust_screen().__eq__(expected_url)
        search_off = SearchOff(self.driver)
        homepage.custom_sleep(5)
        search_off.click_on_search()
        search_off.enter_lastname(self.last_name)
        search_off.enter_firstname(self.first_name)
        search_off.search_offender()
        homepage.custom_sleep(5)
        add_cust_ord = AddcustodialRecord(self.driver)
        add_cust_ord.click_add_btn()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.enter_order_date(self.today_date)
        add_cust_ord.custom_sleep(5)
        add_cust_ord.enter_court()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.enter_type()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.drag_drop()
        add_cust_ord.enter_commence_type()
        add_cust_ord.custom_sleep(2)
        add_cust_ord.enter_commence_date(self.today_date)
        add_cust_ord.custom_sleep(2)
        add_cust_ord.drag_drop()
        add_cust_ord.click_term_type_lngth()
        # add_cust_ord.custom_sleep(3)
        add_cust_ord.enter_holdexpdate_date(self.formatted_future_date)
        add_cust_ord.custom_sleep(5)
        add_cust_ord.scroll_down_to_charges()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.click_add_under_chrg()
        add_cust_ord.custom_sleep(5)
        add_cust_ord.click_add_charges()
        add_cust_ord.enter_matter()
        add_cust_ord.launch_description()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.select_one_charge()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.select_save_charge()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.click_save_charge()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.select_charge_in_matter()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.click_save_charge()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.click_select_in_charge()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.select_outcome()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.save_calculate()
        add_cust_ord.custom_sleep(4)
        add_cust_ord.calculation_reason()
        add_cust_ord.custom_sleep(3)
        add_cust_ord.save_calculation()
        add_cust_ord.custom_sleep(3)
        exp_msg = "Record(s) saved"
        # assert add_cust_ord.success_message().__eq__(exp_msg)
        if add_cust_ord.success_message().__eq__(exp_msg):
            assert True
            self.logger.info("************* Custodial Order Test Passed **********")
        else:
            assert False
            self.logger.info("************* Custodial Order Test Failed **********")













