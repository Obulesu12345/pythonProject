import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SettingPage:

    def __init__(self,driver):
        self.driver = driver

    manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
    setting_button_xpath = "//div[text()='Setting']"
    verify_setting_page_xpath = "//*[text()='Add respective emails to send the daily reports']"

    daily_reports_button_xpath = "//*[text()='Daily Reports']"
    cxo_report_add_mail_button_xpath = "(//button[text()='Add Emails'])[1]"
    add_email_input_xpath = "(//input[contains(@type,'email')])[3]"

    technician_report_add_mail_button_xpath = "(//button[text()='Add Emails'])[2]"
    technician_add_email_input_xpath = "(//input[contains(@type,'email')])[4]"

    notification_button_xpath = "//button[text()='Notifications']"
    notification_add_email_button_xpath = "//button[text()='Add Emails']"
    notification_add_email_input_xpath = "(//input[contains(@type,'email')])[3]"
    notification_save_button_xpath = "//button[text()='Save']"

    cloud_connect_button_xpath = "//button[text()='Cloud connect']"
    cloud_connect_add_email_button_xpath = "//button[text()='Add Emails']"
    cloud_connect_add_email_input_xpath = "(//input[contains(@type,'email')])[2]"
    cloud_connect_save_button_xpath = "//button[text()='Save']"

    verify_manage_page_text_xpath = "//div[text()='Setting']"

    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def verify_manage_page_text(self):
        return self.driver.find_element(By.XPATH, self.verify_manage_page_text_xpath).text



    def cloud_connect_save_button(self):
        self.driver.find_element(By.XPATH, self.cloud_connect_save_button_xpath).click()

    def cloud_connect_add_email_button(self):
        self.driver.find_element(By.XPATH, self.cloud_connect_add_email_button_xpath).click()

    def cloud_connect_add_email_input(self, add_email):
        self.driver.find_element(By.XPATH, self.cloud_connect_add_email_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.cloud_connect_add_email_input_xpath).click()
        self.driver.find_element(By.XPATH, self.cloud_connect_add_email_input_xpath).send_keys(add_email)

    def cloud_connect_button(self):
        self.driver.find_element(By.XPATH, self.cloud_connect_button_xpath).click()


    def notification_save_button(self):
        self.driver.find_element(By.XPATH, self.notification_save_button_xpath).click()

    def notification_add_email_button(self):
        self.driver.find_element(By.XPATH, self.notification_add_email_button_xpath).click()

    def notification_add_email_input(self, add_email):
        self.driver.find_element(By.XPATH, self.notification_add_email_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.notification_add_email_input_xpath).click()
        self.driver.find_element(By.XPATH, self.notification_add_email_input_xpath).send_keys(add_email)


    def notification_button(self):
        self.driver.find_element(By.XPATH, self.notification_button_xpath).click()


    def technician_add_email_input(self, add_email):
        self.driver.find_element(By.XPATH, self.technician_add_email_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.technician_add_email_input_xpath).click()
        self.driver.find_element(By.XPATH, self.technician_add_email_input_xpath).send_keys(add_email)


    def technician_report_add_mail_button(self):
        self.driver.find_element(By.XPATH, self.technician_report_add_mail_button_xpath).click()


    def add_email_input(self, add_email):
        self.driver.find_element(By.XPATH, self.add_email_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.add_email_input_xpath).click()
        self.driver.find_element(By.XPATH, self.add_email_input_xpath).send_keys(add_email)


    def cxo_report_add_mail_button(self):
        self.driver.find_element(By.XPATH, self.cxo_report_add_mail_button_xpath).click()

    def daily_reports_button(self):
        self.driver.find_element(By.XPATH, self.daily_reports_button_xpath).click()

    def verify_setting_page(self):
        return self.driver.find_element(By.XPATH, self.verify_setting_page_xpath).text

    def manage_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()

    def manage_setting_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()

        element = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, self.setting_button_xpath)))
        element.click()