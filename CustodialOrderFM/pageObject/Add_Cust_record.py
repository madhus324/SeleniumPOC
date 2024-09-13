from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from pynput.keyboard import Key, Controller
from pageObject.BasePage import BasePage
keyboard = Controller()
import time

class AddcustodialRecord(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def double_click(self, xpath):
        date_input = self.driver.find_element(By.XPATH, xpath)
        actions = ActionChains(self.driver)
        actions.double_click(date_input).perform()

    Add_btn_cust_xpath = "//button[@class='court-btn controls-btn add-btn']"
    order_date_1_xpath = "(//div[@col-id='orderedDate'])[2]"
    order_date_2_xpath = "/html/body/app-root/app-home/mat-sidenav-container/mat-sidenav-content/perfect-scrollbar/div/div[1]/main/app-ocdleglo/s4-pane/div/div/div[3]/div/s4-panel/div/div/div/mat-expansion-panel/div/div/s4-dynamic-grid/div/ag-grid-angular/div/div[2]/div[2]/div[3]/div[2]/div/div/div/div[2]/grid-cell-editor-date/mat-form-field/div/div[1]/div[1]/input"
    court_1_xpath = "(//div[@col-id='court'])[2]"
    court_2_xpath = "(//span[@class='mat-option-text']//span)[3]"
    # court_2_xpath = "//span[text()='Supreme Court - Launce']"
    type_1_xpath = "(//div[@col-id='sentenceCalcType'])[2]"
    # type_2_xpath = "//span[text()='JFL Custodial Holding ']"
    # Index xpath for type
    type_2_xpath = "(//span[@class='mat-option-text']//span)[9]"
    commence_dte_1_xpath = "(//div[@col-id='commenceDate'])[2]"
    commence_dte_2_xpath = "/html[1]/body[1]/app-root[1]/app-home[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/perfect-scrollbar[1]/div[1]/div[1]/main[1]/app-ocdleglo[1]/s4-pane[1]/div[1]/div[1]/div[3]/div[1]/s4-panel[1]/div[1]/div[1]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/s4-dynamic-grid[1]/div[1]/ag-grid-angular[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[9]/grid-cell-editor-date[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]"
    holdexpdt_1_xpath = "(//div[@col-id='holdExpiryDate'])[2]"
    holdexpdt_2_xpath = "/html[1]/body[1]/app-root[1]/app-home[1]/mat-sidenav-container[1]/mat-sidenav-content[1]/perfect-scrollbar[1]/div[1]/div[1]/main[1]/app-ocdleglo[1]/s4-pane[1]/div[1]/div[1]/div[3]/div[1]/s4-panel[1]/div[1]/div[1]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/s4-dynamic-grid[1]/div[1]/ag-grid-angular[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[14]/grid-cell-editor-date[1]/mat-form-field[1]/div[1]/div[1]/div[1]/input[1]"
    addbtn_charges_grd_xpath = "(//button[contains(@class,'court-btn controls-btn')])[4]"
    # addbtn_charges_grd_xpath = "(//button[@type='submit'])[3]"
    # addbtn_in_charges_xpath = "(//button[@type='submit'])[5]"
    addbtn_in_charges_xpath = "(//button[@type='submit'])[6]"
    matter_field_xpath = "(//div[@col-id='matter'])[5]"
    description_xpath = "/html[1]/body[1]/div[6]/div[2]/div[1]/mat-dialog-container[1]/app-ocdchgsu-dlg[1]/s4-dialog-card[1]/s4-dialog-card-content[1]/mat-dialog-content[1]/s4-panel[1]/div[1]/div[1]/div[1]/mat-expansion-panel[1]/div[1]/div[1]/s4-dynamic-grid[1]/div[1]/ag-grid-angular[1]/div[1]/div[2]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[4]/grid-cell-render-hyperlink[1]/s4-hyperlink[1]/s4-image[1]/img[1]"
    select_charge_xpath = "(//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin'])[4]"
    select_save_chrg_xpath = "(//button[@class='mat-focus-indicator mat-raised-button mat-button-base primary-blue-btn mat-primary ng-star-inserted'])[4]"
    save_charge_in_matter_xpath = "//button[@class='court-btn controls-btn save-btn']"
    select_chrge_in_matter_xpath = "//span[@class='mat-checkbox-inner-container mat-checkbox-inner-container-no-side-margin']"
    click_select_in_charge_xpath = "//span[@class='mat-button-wrapper'][normalize-space()='Select']"
    outcome_1_xpath = "(//div[@col-id='outcome'])[2]"
    select_outcome_2_xpath = "//span[text()='Held Over']"
    save_calculate_xpath = "//span[normalize-space()='Save & Calculate']"
    click_cal_rsn_xpath = "//input[@id='sentence_calc']"
    select_rsn_lov_xpath = "(//div[normalize-space()='Adjust Sentence'])[1]"
    cal_rsn_save_xpath = "//button[@id='cal_sent_exp']"
    drag_Xpath = "(//div[@class='ag-body-horizontal-scroll-viewport'])[2]"
    click_navi_condi_tab_xpath = "//div[contains(text(),'Conditions')]"
    retreive_toast_msg = "//div[@class='toastContainer ng-star-inserted']//p[1]"
    ttl_header_xpath = "(//div[@col-id='termTypeAndLength'])[2]"
    term_type_lngt_xpath = "(//div[@col-id='lengthBtn'])[2]"
    addbtn_in_ttl_xpath = "//div[@class='cdk-overlay-container']//div[@class='ng-star-inserted']//div[1]//button[1]"
    term_type_1_xpath = "(//div[@col-id='termType'])[2]"
    term_type_2_xpath = "(//span[@class='mat-option-text']//span)[3]"
    enter_years_1_xpath = "(//div[@col-id='years'])[2]"
    enter_years_2_xpath = "(//div[@class='ag-cell-value ag-cell ag-cell-normal-height ag-cell-range-selected ag-cell-range-selected-1 ag-cell-range-single-cell ag-cell-focus ag-cell-not-inline-editing ag-align-left'])[1]"
    commence_type_1_xpath = "(//div[@col-id='commenceType'])[2]"
    commence_type_2_xpath = "(//span[@class='mat-option-text']//span)[3]"
    click_select_in_ttl_xpath = "(//span[@class='mat-button-wrapper'][normalize-space()='Select'])[1]"


    def click_add_btn(self):
        self.element_click("Add_btn_cust_xpath", self.Add_btn_cust_xpath)

        # self.driver.find_element(By.XPATH, self.Add_btn_cust_xpath).click()

    def enter_order_date(self, order_date):
        self.double_click(self.order_date_1_xpath)
        self.type_into_element(order_date, "order_date_2_xpath", self.order_date_2_xpath)

        # self.double_click(self.order_date_1_xpath)
        # self.driver.find_element(By.XPATH, self.order_date_2_xpath).send_keys(order_date)

    def enter_court(self):
        self.double_click(self.court_1_xpath)
        self.element_click("court_2_xpath", self.court_2_xpath)

        # self.double_click(self.court_1_xpath)
        # self.driver.find_element(By.XPATH, self.court_2_xpath).click()

    def enter_type(self):
        self.double_click(self.type_1_xpath)
        self.element_click("type_2_xpath", self.type_2_xpath)

        # self.double_click(self.type_1_xpath)
        # self.driver.find_element(By.XPATH, self.type_2_xpath).click()

    def click_term_type_lngth(self):
        # self.drag_drop()
        # self.custom_sleep(2)
        exp_warn_msg = "Please select Term Type(s) & Length(s)"
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Save & Calculate']").click()
        time.sleep(3)
        act_msg = self.driver.find_element(By.XPATH, "//div[@class='toastContainer ng-star-inserted']//p[1]").text
        if act_msg == exp_warn_msg:
            print("Term Type(s) & Length(s) is a Mandatory field")
            self.element_click("term_type_lngt_xpath", self.term_type_lngt_xpath)
            self.custom_sleep(3)
            self.add_ttl()
        else:
            pass

        # mand_ele = self.driver.find_element(By.XPATH, self.term_type_lngt_xpath)
        # is_mandatory = mand_ele.is_displayed()
        #
        # if is_mandatory:
        #     print("The element is mandatory, performing the action.")
        #     self.element_click("term_type_lngt_xpath", self.term_type_lngt_xpath)
        #     self.custom_sleep(3)
        #     self.add_ttl()
        # else:
        #     print("The element is not mandatory, skipping the action.")

        # self.custom_sleep(3)
        # self.element_click("term_type_lngt_xpath", self.term_type_lngt_xpath)


    def add_ttl(self):
        self.element_click("addbtn_in_ttl_xpath", self.addbtn_in_ttl_xpath)
        self.custom_sleep(3)
        self.double_click(self.term_type_1_xpath)
        self.element_click("term_type_2_xpath", self.term_type_2_xpath)
        self.custom_sleep(3)
        self.double_click(self.enter_years_1_xpath)
        self.custom_sleep(3)
        while True:
            time.sleep(2)
            keyboard.press('2')
            keyboard.release('2')
            break
        self.element_click("click_select_in_ttl_xpath", self.click_select_in_ttl_xpath)

    def enter_commence_date(self, commence_date):
        # self.double_click(self.commence_dte_1_xpath)
        # self.type_into_element(commence_date, "commence_dte_2_xpath", self.commence_dte_2_xpath)

        exp_warn_msg = "Please select Commence Date"
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Save & Calculate']").click()
        time.sleep(3)
        act_msg = self.driver.find_element(By.XPATH, "//div[@class='toastContainer ng-star-inserted']//p[1]").text
        if act_msg == exp_warn_msg:
            print("Commence Date is a Mandatory field")
            self.double_click(self.commence_dte_1_xpath)
            time.sleep(3)
            self.type_into_element(commence_date, "commence_dte_2_xpath", self.commence_dte_2_xpath)
            time.sleep(3)
        else:
            pass
            print("Commence Date is a Mandatory field")

    def enter_commence_type(self):
        exp_warn_msg = "Please select Commence Type"
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Save & Calculate']").click()
        time.sleep(3)
        act_msg = self.driver.find_element(By.XPATH, "//div[@class='toastContainer ng-star-inserted']//p[1]").text
        if act_msg == exp_warn_msg:
            print("Commence Type is a Mandatory field")
            self.double_click("(//div[@col-id='commenceType'])[2]")
            time.sleep(3)
            self.driver.find_element(By.XPATH, "(//span[@class='mat-option-text']//span)[3]").click()
            time.sleep(3)
        else:
            pass
            print("Commence Type is Not a mandatory field")

    def enter_holdexpdate_date(self, holdexpiry_date):
        exp_warn_msg = "Please select Hold Expiry Date"
        self.driver.find_element(By.XPATH, "//span[normalize-space()='Save & Calculate']").click()
        time.sleep(3)
        act_msg = self.driver.find_element(By.XPATH, "//div[@class='toastContainer ng-star-inserted']//p[1]").text
        if act_msg == exp_warn_msg:
            assert True
            print("Hold Expiry Date is a Mandatory field")
            self.double_click(self.holdexpdt_1_xpath)
            self.type_into_element(holdexpiry_date, "holdexpdt_2_xpath", self.holdexpdt_2_xpath)
        else:
            pass
            print("Hold Expiry Date is not a Mandatory field")
            # assert False

        # self.double_click(self.holdexpdt_1_xpath)
        # self.type_into_element(holdexpiry_date, "holdexpdt_2_xpath", self.holdexpdt_2_xpath)

    def custom_sleep(self, seconds):
        time.sleep(seconds)

    def scroll_down_to_charges(self):
        # self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        refresh_data = self.driver.find_element(By.XPATH, "//span[normalize-space()='Refresh Data']")
        self.driver.execute_script("arguments[0].scrollIntoView()", refresh_data)

    def click_add_under_chrg(self):
        self.element_click("addbtn_charges_grd_xpath", self.addbtn_charges_grd_xpath)

        # self.driver.find_element(By.XPATH, self.addbtn_charges_grd_xpath).click()

    def click_add_charges(self):
        self.element_click("addbtn_in_charges_xpath", self.addbtn_in_charges_xpath)

        # self.driver.find_element(By.XPATH, self.addbtn_in_charges_xpath).click()

    def enter_matter(self):
        self.double_click(self.matter_field_xpath)
        self.custom_sleep(5)
        while True:
            time.sleep(2)
            keyboard.press('m')
            keyboard.release('m')
            keyboard.press('a')
            keyboard.release('a')
            keyboard.press('t')
            keyboard.release('t')
            break

    def launch_description(self):
        self.element_click("description_xpath", self.description_xpath)

        # self.driver.find_element(By.XPATH, self.description_xpath).click()

    def select_one_charge(self):
        self.element_click("select_charge_xpath", self.select_charge_xpath)

        # self.driver.find_element(By.XPATH, self.select_charge_xpath).click()

    def select_save_charge(self):
        self.element_click("select_save_chrg_xpath", self.select_save_chrg_xpath)

        # self.driver.find_element(By.XPATH, self.select_save_chrg_xpath).click()

    def click_save_charge(self):
        self.element_click("save_charge_in_matter_xpath", self.save_charge_in_matter_xpath)

        # self.driver.find_element(By.XPATH, self.save_charge_in_matter_xpath).click()

    def select_charge_in_matter(self):
        self.element_click("select_chrge_in_matter_xpath", self.select_chrge_in_matter_xpath)

        # self.driver.find_element(By.XPATH, self.select_chrge_in_matter_xpath).click()

    def click_select_in_charge(self):
        self.element_click("click_select_in_charge_xpath", self.click_select_in_charge_xpath)

        # self.driver.find_element(By.XPATH, self.click_select_in_charge_xpath).click()

    def select_outcome(self):
        self.double_click(self.outcome_1_xpath)
        self.element_click("select_outcome_2_xpath", self.select_outcome_2_xpath)

        # self.double_click(self.outcome_1_xpath)
        # self.driver.find_element(By.XPATH, self.select_outcome_2_xpath).click()

    def save_calculate(self):
        self.element_click("save_calculate_xpath", self.save_calculate_xpath)

        # self.driver.find_element(By.XPATH, self.save_calculate_xpath).click()

    def calculation_reason(self):
        # self.element_click("self.click_cal_rsn_xpath", self.self.click_cal_rsn_xpath)
        # self.custom_sleep(2)
        # self.element_click("select_rsn_lov_xpath", self.select_rsn_lov_xpath)

        cal_rsn = self.driver.find_element(By.XPATH, self.click_cal_rsn_xpath)
        cal_rsn.click()
        self.driver.find_element(By.XPATH, self.select_rsn_lov_xpath).click()

    def save_calculation(self):
        self.element_click("cal_rsn_save_xpath", self.cal_rsn_save_xpath)

        # self.driver.find_element(By.XPATH, self.cal_rsn_save_xpath).click()
        time.sleep(5)

    def drag_drop(self):
        drag_element = self.driver.find_element(By.XPATH, self.drag_Xpath)
        action = ActionChains(self.driver)
        action.click_and_hold(drag_element)
        action.move_by_offset(200, 0)
        action.release().perform()

    def check_condi_tab(self):
        self.element_click("click_navi_condi_tab_xpath", self.click_navi_condi_tab_xpath)

    def success_message(self):
        toast_msg = self.driver.find_element(By.XPATH, self.retreive_toast_msg).text
        return toast_msg

