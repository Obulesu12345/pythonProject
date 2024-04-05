import time
import pytest
from Pages.loginpage import LoginPage
from Pages.instance import InstancePage
from Pages.setting_page import SettingPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestFirewall:
    def test_setting_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        setting = SettingPage(self.driver)
        time.sleep(3)
        setting.manage_setting_page()
        time.sleep(3)

    def test_verify_setting_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        setting = SettingPage(self.driver)
        time.sleep(3)
        setting.manage_setting_page()
        time.sleep(3)
        message = "Add respective emails to send the daily reports"
        setting.verify_setting_page().__eq__(message)
        self.driver.quit()

    def test_daily_reports(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        setting = SettingPage(self.driver)
        time.sleep(3)
        setting.manage_setting_page()
        time.sleep(3)
        setting.daily_reports_button()
        time.sleep(3)
        setting.cxo_report_add_mail_button()
        time.sleep(3)
        setting.add_email_input("anshul.reejonia@gmail.com")
        time.sleep(3)

    def test_daily_reports_for_technician_report(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        setting = SettingPage(self.driver)
        time.sleep(3)
        setting.manage_setting_page()
        time.sleep(3)
        setting.daily_reports_button()
        time.sleep(3)
        setting.technician_report_add_mail_button()
        time.sleep(3)
        setting.technician_add_email_input("anshul.reejonia@gmail.com")
        time.sleep(3)

    def test_notification(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        setting = SettingPage(self.driver)
        time.sleep(3)
        setting.manage_setting_page()
        time.sleep(3)
        setting.notification_button()
        time.sleep(3)
        setting.notification_add_email_button()
        time.sleep(3)
        setting.notification_add_email_input("anshul.reejonia@gmail.com")
        time.sleep(3)
        setting.notification_save_button()
        time.sleep(2)

    def test_cloud_connect(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        setting = SettingPage(self.driver)
        time.sleep(3)
        setting.manage_setting_page()
        time.sleep(3)
        setting.cloud_connect_button()
        time.sleep(3)
        setting.cloud_connect_add_email_button()
        time.sleep(3)
        setting.cloud_connect_add_email_input("anshul.reejonia@gmail.com")
        time.sleep(3)
        setting.cloud_connect_save_button()
        time.sleep(2)


