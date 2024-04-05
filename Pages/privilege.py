import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class privilegePage:

    def __init__(self,driver):
        self.driver = driver

    email_text_xpath = "//input[@name='email']"
    emai_password_xpath = "//input[@name='password']"
    click_login_xpath = "//button[contains(@type,'submit')]"
    privilege_xpath = "//div[text()='Privilege']"
    privilege_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[1]"
    user_xpath = "//div[text()='Users']"
    location_cpath = "//div[@id='location-select']"
    dropdown_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[2]"
    location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[2]"
    verify_hover_users_page_xpath = "//button[text()='Add User']"
    adduser_xpath = "//button[text()='Add User']"
    name_xapth = "//input[contains(@name,'firstName')]"
    last_name_xpath ="//input[contains(@name,'lastName')]"
    name_mail_xpath = "//input[contains(@name,'email')]"
    phone_name_xpath = "//input[contains(@name,'phone')]"
    invite_button_xpath = "//button[text()='Invite']"
    table_rows_xpath = "//table[@class='MuiTable-root css-s064k4']//tr"
    table_columns_xpath = "//table[@class='MuiTable-root css-s064k4']//th"

    actions_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr/td[@dataindex='action'])[1]"
    action_instance_button_xpath = "(//div[text()='Instance'])[2]"
    instance_check_box_xpath = "(//input[contains(@type,'checkbox')])[2]"
    assign_instance_button_xpath = "(//button[text()='Assign Instance'])"

    role_xpath = "(//div[text()='Role'])"
    assign_role_check_box_xpath = "(//input[contains(@type,'checkbox')])[4]"
    assign_role_button_xpath = "(//button[text()='Assign Roles'])"

    actions_edit_xpath = "(//div[text()='Edit'])"
    verify_actions_edit_xpath = "(//div[text()='Fill required fields to edit user'])"

    actions_password_xpath = "(//div[text()='Password'])"
    verify_reset_password_xpath = "(//div[text()='You can reset password for'])"

    actions_log_xpath = "(//div[text()='Logs'])"
    action_table_rows_xpath = "(//table[@class='MuiTable-root css-s064k4'])[2]//tr"
    action_table_columns_xpath = "(//table[@class='MuiTable-root css-s064k4'])[2]//th"
    table_data_xpath = "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)[2]"

    # location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    # dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"

    alert_otp_msg_xpath = "//div[contains(@role,'alert')]"

    def alert_otp_msg(self):
        return self.driver.find_element(By.XPATH, self.alert_otp_msg_xpath).text

    def location(self):
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def location_dropdown(self):

        element = self.driver.find_element(By.XPATH, self.dropdown_elements_xpath)
        element.click()

    def actions_log(self):
        self.driver.find_element(By.XPATH,self.actions_log_xpath).click()

    def users_action_table_total_rows(self):
        rows = self.driver.find_elements(By.XPATH,self.action_table_rows_xpath)
        return print(len(rows))
    def users_action_table_total_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.action_table_columns_xpath)
        return print(len(columns))
    def actions_table_data(self):
        tbody = self.driver.find_element(By.XPATH, self.table_data_xpath)
        data = []
        for tr in tbody.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)[2]/tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/tbody)[2]//td")]
            data.append(row)
        print(data)


    def actions_password(self):
        self.driver.find_element(By.XPATH,self.actions_password_xpath).click()
    def verify_password(self):
        return self.driver.find_element(By.XPATH,self.verify_reset_password_xpath).text

    def actions_edit(self):
        self.driver.find_element(By.XPATH, self.actions_edit_xpath).click()
    def verify_actions_edit_page(self):
        return self.driver.find_element(By.XPATH,self.verify_actions_edit_xpath).text


    def action_button(self):
        self.driver.find_element(By.XPATH, self.actions_button_xpath).click()

    def action_role(self):
        self.driver.find_element(By.XPATH, self.role_xpath).click()

    def assign_role_check_box(self):
        self.driver.find_element(By.XPATH, self.assign_role_check_box_xpath).click()
    def assign_role_button(self):
        self.driver.find_element(By.XPATH, self.assign_role_button_xpath).click()

    def action_instance_button(self):
        self.driver.find_element(By.XPATH, self.action_instance_button_xpath).click()

    def instance_check_box(self):
        self.driver.find_element(By.XPATH, self.instance_check_box_xpath).click()
    def assign_instance_button(self):
        self.driver.find_element(By.XPATH, self.assign_instance_button_xpath).click()


    def users_total_rows(self):
        rows = self.driver.find_elements(By.XPATH,self.table_rows_xpath)
        return print(len(rows))
    def users_total_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.table_columns_xpath)
        return print(len(columns))
    def table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table/tbody")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, ".//td")]
            data.append(row)
        print(data)

    def email_address(self,email_addrees_text):
        self.driver.find_element(By.XPATH, self.email_text_xpath).click()
        self.driver.find_element(By.XPATH, self.email_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_text_xpath).send_keys(email_addrees_text)

    def email_address_password(self,email_password_address):
        self.driver.find_element(By.XPATH, self.emai_password_xpath).click()
        self.driver.find_element(By.XPATH, self.emai_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.emai_password_xpath).send_keys(email_password_address)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.click_login_xpath).click()

    def privilege_page_button(self):
        self.driver.find_element(By.XPATH, self.privilege_button_xpath).click()

    def privilege_page(self):
        self.driver.find_element(By.XPATH, self.privilege_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.user_xpath)))
        element.click()

    def add_user_button(self):
        self.driver.find_element(By.XPATH, self.adduser_xpath).click()
    def add_user_data_name(self,firstname):
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[contains(@name,'firstName')]")))
        element.click()
        element.clear()
        element.send_keys(firstname)
        # self.driver.find_element(By.XPATH, self.name_xapth).click()
        # self.driver.find_element(By.XPATH, self.name_xapth).clear()
        # self.driver.find_element(By.XPATH, self.name_xapth).send_keys(firstname)

    def add_user_data_lastname(self,lastname):
        self.driver.find_element(By.XPATH, self.last_name_xpath).click()
        self.driver.find_element(By.XPATH, self.last_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.last_name_xpath).send_keys(lastname)

    def add_user_data_email(self,email):
        self.driver.find_element(By.XPATH, self.name_mail_xpath).click()
        self.driver.find_element(By.XPATH, self.name_mail_xpath).clear()
        self.driver.find_element(By.XPATH, self.name_mail_xpath).send_keys(email)

    def add_user_data_phone(self,phone):
        self.driver.find_element(By.XPATH, self.phone_name_xpath).click()
        self.driver.find_element(By.XPATH, self.phone_name_xpath).clear()
        self.driver.find_element(By.XPATH, self.phone_name_xpath).send_keys(phone)

    def add_user_invite_button(self):
        self.driver.find_element(By.XPATH, self.invite_button_xpath).click()


    def veriry_users_page(self):
        return self.driver.find_element(By.XPATH,self.verify_hover_users_page_xpath).text

    def hover_user_page(self):
        # privilegepage = self.driver.find_element(By.XPATH, self.privilege_xpath)
        # users = self.driver.find_element(By.XPATH, self.user_xpath)
        # actions =ActionChains(self.driver)
        # actions.move_to_element(privilegepage).click()
        # actions.move_to_element(users).click()
        return self.driver.find_element(By.XPATH, self.user_xpath).text

    def location(self):
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def location_dropdown(self):
        element = self.driver.find_element(By.XPATH, self.dropdown_elements_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()

