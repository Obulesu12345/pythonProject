import os
import time
import pytest

from Pages.Dashboardpage import Test_Login
from Pages.loginpage import LoginPage
from Pages.ip_tracking import Iptracking
from Pages.summary_report import SummaryReport


@pytest.mark.usefixtures("setup_and_teardown")
class TestIpTracking:
    def test_verify_report_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        ip = SummaryReport(self.driver)
        message = "Reports"
        assert ip.verify_report_button().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "reports.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


    def test_report_summary_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        ip = SummaryReport(self.driver)
        ip.summary_page()
        time.sleep(2)
        message = "External IP Communication | 10.187.1.49"
        assert ip.verify_summary_page().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "verify_summary_page.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_select_date_and_time(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        ip = SummaryReport(self.driver)
        ip.summary_page()
        time.sleep(4)
        ip.from_date()
        time.sleep(4)
        ip.to_date()
        time.sleep(4)
        ip.public_ip_dropdown_button()
        time.sleep(3)
        ip.public_ip_list()
        time.sleep(3)
        ip.submit_button()

    def test_summary_display_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        ip = SummaryReport(self.driver)
        ip.summary_page()
        time.sleep(4)
        ip.from_date()
        time.sleep(4)
        ip.to_date()
        time.sleep(4)
        ip.public_ip_dropdown_button()
        time.sleep(3)
        ip.public_ip_list()
        time.sleep(3)
        ip.submit_button()
        self.driver.implicitly_wait(20)
        ip.table_title()
        ip.summary_table_data()
        self.driver.quit()

    def test_summary_external_communication_table_verify(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(3)
        ip = SummaryReport(self.driver)
        ip.summary_page()
        login = Test_Login(self.driver)
        login.location()
        time.sleep(2)
        login.location_dropdown()
        time.sleep(4)
        ip.from_date()
        time.sleep(4)
        ip.to_date()
        time.sleep(4)
        ip.public_ip_dropdown_button()
        time.sleep(3)
        ip.public_ip_list()
        time.sleep(3)
        ip.submit_button()
        self.driver.implicitly_wait(20)
        ip.verify_external_communication_table_data()

    def test_summary_report_apps_table_verify(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(3)
        ip = SummaryReport(self.driver)
        ip.summary_page()
        login = Test_Login(self.driver)
        login.location()
        time.sleep(2)
        login.location_dropdown()
        time.sleep(4)
        ip.from_date()
        time.sleep(4)
        ip.to_date()
        time.sleep(4)
        ip.public_ip_dropdown_button()
        time.sleep(3)
        ip.public_ip_list()
        time.sleep(3)
        ip.submit_button()
        self.driver.implicitly_wait(20)
        ip.verify_apps_table_data()



    def test_summary_report_city_wise_traffic_table_verify(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(3)
        ip = SummaryReport(self.driver)
        ip.summary_page()
        login = Test_Login(self.driver)
        login.location()
        time.sleep(2)
        login.location_dropdown()
        time.sleep(4)
        ip.from_date()
        time.sleep(4)
        ip.to_date()
        time.sleep(4)
        ip.public_ip_dropdown_button()
        time.sleep(3)
        ip.public_ip_list()
        time.sleep(3)
        ip.submit_button()
        self.driver.implicitly_wait(20)
        ip.city_wise_traffic_table_data()
        time.sleep(5)