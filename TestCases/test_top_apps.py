import os
import time
import pytest

from pages.dashboard import Test_Login
from pages.login_page import LoginPage
from pages.top_apps import Topapps


@pytest.mark.usefixtures("setup_and_teardown")
class TestTopapps:
    def test_verify_report_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        apps = Topapps(self.driver)
        time.sleep(3)
        message = "Reports"
        assert apps.verify_report_button().__eq__(message)
        apps.current_url()
        self.driver.save_screenshot("verify_report.png")


    def test_report_topapps_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        apps = Topapps(self.driver)
        apps.topapps_page()
        time.sleep(4)
        message = "From"
        assert apps.verify_apps_page().__eq__(message)
        apps.current_url()
        self.driver.save_screenshot("verify_top_apps_.png")
        self.driver.quit()

    def test_select_date_and_time(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        apps = Topapps(self.driver)
        apps.topapps_page()
        time.sleep(4)
        apps.from_date()
        time.sleep(4)
        apps.to_date()
        time.sleep(4)
        apps.public_ip_dropdown_button()
        time.sleep(3)
        apps.public_ip_list()
        time.sleep(3)
        apps.submit_button()
        self.driver.implicitly_wait(10)
        self.driver.save_screenshot("verify_top_apps_table_.png")
        self.driver.quit()

    def test_csv(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        apps = Topapps(self.driver)
        apps.topapps_page()
        time.sleep(2)
        apps.from_date()
        time.sleep(1)
        apps.to_date()
        time.sleep(1)
        apps.public_ip_dropdown_button()
        time.sleep(1)
        apps.public_ip_list()
        time.sleep(1)
        apps.submit_button()
        time.sleep(1)
        apps.csv()
        time.sleep(3)
        message = "report send to your mail sonu.verma@zybisys.com, tulasiram.r@zybisys.com, parameswari.t@zybisys.com"
        assert apps.alert_otp_msg().__eq__(message)



    def test_top_apps_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        apps = Topapps(self.driver)
        login = Test_Login(self.driver)
        login.dashboard()
        login.location()
        time.sleep(1)
        login.location_dropdown()
        apps.topapps_page()
        time.sleep(1)
        apps.from_date()
        time.sleep(1)
        apps.to_date()
        time.sleep(1)
        apps.public_ip_dropdown_button()
        time.sleep(1)
        apps.public_ip_list()
        time.sleep(1)
        apps.submit_button()
        time.sleep(1)
        apps.rows_per_page()
        time.sleep(1)
        apps.rows_per_page_dropdown()
        apps.table_title()
        time.sleep(2)
        apps.topapps_table_data()
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "top_apps_table.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


    # def test_top_apps_table_verify(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     self.driver.implicitly_wait(10)
    #     apps = Topapps(self.driver)
    #     apps.location()
    #     time.sleep(5)
    #     apps.location_dropdown()
    #     time.sleep(3)
    #     apps.topapps_page()
    #     time.sleep(4)
    #     apps.from_date()
    #     time.sleep(4)
    #     apps.to_date()
    #     time.sleep(4)
    #     apps.public_ip_dropdown_button()
    #     time.sleep(3)
    #     apps.public_ip_list()
    #     time.sleep(3)
    #     apps.submit_button()
    #     time.sleep(4)
    #     apps.rows_per_page()
    #     time.sleep(2)
    #     apps.rows_per_page_dropdown()
    #     time.sleep(3)
    #     apps.verify_data()
    #     self.driver.quit()


    def test_ip_tracking_verify_each_row_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        apps = Topapps(self.driver)
        apps.location()
        time.sleep(1)
        apps.location_dropdown()
        time.sleep(1)
        apps.topapps_page()
        time.sleep(1)
        apps.from_date()
        time.sleep(1)
        apps.to_date()
        time.sleep(1)
        apps.public_ip_dropdown_button()
        time.sleep(1)
        apps.public_ip_list()
        time.sleep(1)
        apps.submit_button()
        self.driver.implicitly_wait(60)
        apps.rows_per_page()
        time.sleep(2)
        apps.rows_per_page_dropdown()
        apps.total_table_data_for_each_single_row()
        self.driver.quit()






















# import time
# import pytest
#
# from Pages.Dashboardpage import Test_Login
# from Pages.loginpage import LoginPage
# from Pages.topapps import Topapps
#
#
# @pytest.mark.usefixtures("setup_and_teardown")
# class TestTopapps:
#     def test_verify_report_login_page(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         apps = Topapps(self.driver)
#         time.sleep(3)
#         message = "Reports"
#         assert apps.verify_report_button().__eq__(message)
#
#     def test_report_topapps_login_page(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         apps = Topapps(self.driver)
#         apps.topapps_page()
#         time.sleep(4)
#         message = "From"
#         assert apps.verify_apps_page().__eq__(message)
#         self.driver.quit()
#
#     def test_select_date_and_time(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         apps = Topapps(self.driver)
#         apps.topapps_page()
#         time.sleep(4)
#         apps.from_date()
#         time.sleep(4)
#         apps.to_date()
#         time.sleep(4)
#         apps.public_ip_dropdown_button()
#         time.sleep(3)
#         apps.public_ip_list()
#         time.sleep(3)
#         apps.submit_button()
#         time.sleep(5)
#
#
#     def test_top_apps_table_received_data(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         ip = Topapps(self.driver)
#         login = Test_Login(self.driver)
#         login.Hover_over_dashboard()
#         login.location()
#         time.sleep(5)
#         login.location_dropdown()
#         ip.topapps_page()
#         time.sleep(4)
#         ip.from_date()
#         time.sleep(4)
#         ip.to_date()
#         time.sleep(4)
#         ip.public_ip_dropdown_button()
#         time.sleep(3)
#         ip.public_ip_list()
#         time.sleep(3)
#         ip.submit_button()
#         time.sleep(4)
#         # ip.topapps_table_data()
#         # time.sleep(3)
#         ip.topapps_table_received_data()
#         self.driver.quit()
#
#
#     def test_top_apps_table_verify(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         apps = Topapps(self.driver)
#         apps.location()
#         time.sleep(5)
#         apps.location_dropdown()
#         time.sleep(3)
#         apps.topapps_page()
#         time.sleep(4)
#         apps.from_date()
#         time.sleep(4)
#         apps.to_date()
#         time.sleep(4)
#         apps.public_ip_dropdown_button()
#         time.sleep(3)
#         apps.public_ip_list()
#         time.sleep(3)
#         apps.submit_button()
#         time.sleep(4)
#         # apps.topapps_table_data()
#         time.sleep(3)
#         apps.verify_data()
#         self.driver.quit()