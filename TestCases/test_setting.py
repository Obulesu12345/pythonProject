import time
import pytest
from pages.login_page import LoginPage
from pages.instance import InstancePage
from pages.setting_page import SettingPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestFirewall:
    def test_setting_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        setting = SettingPage(self.driver)
        setting.manage_page()
        time.sleep(1)
        message = "Setting"
        assert setting.verify_manage_page_text().__eq__(message)
        setting.current_url()
        self.driver.save_screenshot("setting.png")
        self.driver.quit()


    def test_verify_setting_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        setting = SettingPage(self.driver)
        setting.manage_setting_page()
        time.sleep(1)
        message = "Add respective emails to send the daily reports"
        setting.verify_setting_page().__eq__(message)
        setting.current_url()
        self.driver.save_screenshot("setting.png")
        self.driver.quit()

    def test_daily_reports(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        setting = SettingPage(self.driver)
        setting.manage_setting_page()
        time.sleep(1)
        setting.daily_reports_button()
        time.sleep(1)
        setting.cxo_report_add_mail_button()
        time.sleep(1)
        setting.add_email_input("anshul.reejonia@gmail.com")
        setting.notification_save_button()
        self.driver.save_screenshot("setting_daily_reports_page.png")
        self.driver.quit()

    def test_daily_reports_for_technician_report(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        setting = SettingPage(self.driver)
        setting.manage_setting_page()
        time.sleep(1)
        setting.daily_reports_button()
        time.sleep(1)
        setting.technician_report_add_mail_button()
        time.sleep(1)
        setting.technician_add_email_input("anshul.reejonia@gmail.com")
        time.sleep(1)
        setting.notification_save_button()
        self.driver.save_screenshot("setting_daily_reports_for_technician_report.png")
        self.driver.quit()

    def test_notification(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        setting = SettingPage(self.driver)
        setting.manage_setting_page()
        time.sleep(1)
        setting.notification_button()
        time.sleep(1)
        setting.notification_add_email_button()
        time.sleep(1)
        setting.notification_add_email_input("anshul.reejonia@gmail.com")
        time.sleep(1)
        setting.notification_save_button()
        self.driver.save_screenshot("setting_notification.png")
        self.driver.quit()

    def test_cloud_connect(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        setting = SettingPage(self.driver)
        setting.manage_setting_page()
        time.sleep(1)
        setting.cloud_connect_button()
        time.sleep(1)
        setting.cloud_connect_add_email_button()
        time.sleep(1)
        setting.cloud_connect_add_email_input("anshul.reejonia@gmail.com")
        time.sleep(1)
        setting.cloud_connect_save_button()
        time.sleep(1)
        self.driver.save_screenshot("setting_cloud_connect.png")
        self.driver.quit()


