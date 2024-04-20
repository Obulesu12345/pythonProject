import os
import time
import pytest

from pages.dashboard import Test_Login
from pages.login_page import LoginPage
from pages.ip_tracking import Iptracking


@pytest.mark.usefixtures("setup_and_teardown")
class TestIpTracking:
    # def test_verify_report_login_page(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     self.driver.implicitly_wait(10)
    #     ip = Iptracking(self.driver)
    #     message = "Reports"
    #     assert ip.verify_report_button().__eq__(message)
    #     ip.current_url()
    #     self.driver.save_screenshot("ip_tracking_page.png")
    #     self.driver.quit()


    def test_report_iptracking_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        ip = Iptracking(self.driver)
        ip.iptracking_page()
        time.sleep(1)
        # message = "External IP Communication"
        # assert ip.verify_ip_tracking_page().__eq__(message)
        ip.current_url()
        self.driver.save_screenshot("ip_tracking_login_page.png")
        self.driver.quit()

    def test_select_date_and_time(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        ip = Iptracking(self.driver)
        ip.iptracking_page()
        time.sleep(1)
        ip.from_date()
        time.sleep(1)
        ip.to_date()
        time.sleep(1)
        ip.public_ip_dropdown_button()
        time.sleep(2)
        ip.public_ip_list()
        time.sleep(1)
        ip.submit_button()
        time.sleep(2)
        message = "External IP Communication | 154.83.3.29"
        assert ip.verify_ip_tracking_page().__eq__(message)
        # self.driver.implicitly_wait(10)
        # ip.table_title()
        self.driver.save_screenshot("ip_tracking_table_title.png")
        self.driver.quit()

    def test_ip_tracking_display_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        ip = Iptracking(self.driver)
        ip.iptracking_page()
        time.sleep(1)
        ip.from_date()
        time.sleep(1)
        ip.to_date()
        time.sleep(1)
        ip.public_ip_dropdown_button()
        time.sleep(1)
        ip.public_ip_list()
        time.sleep(1)
        ip.submit_button()
        ip.table_title_data()
        ip.ip_tracking_table_data()
        self.driver.save_screenshot("ip_tracking_table_data.png")
        self.driver.quit()


    def test_ip_tracking_csv(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        ip = Iptracking(self.driver)
        ip.iptracking_page()
        time.sleep(1)
        ip.from_date()
        time.sleep(1)
        ip.to_date()
        time.sleep(1)
        ip.public_ip_dropdown_button()
        time.sleep(1)
        ip.public_ip_list()
        time.sleep(1)
        ip.submit_button()
        time.sleep(1)
        ip.csv()
        time.sleep(3)
        message = "Downloading CSV..."
        assert ip.verify_otp_for_csv().__eq__(message)
        self.driver.save_screenshot("ip_tracking_csv.png")


    def test_ip_tracking_verify_each_row_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        ip = Iptracking(self.driver)
        ip.iptracking_page()
        login = Test_Login(self.driver)
        login.location()
        time.sleep(1)
        login.location_dropdown()
        time.sleep(1)
        ip.from_date()
        time.sleep(2)
        ip.to_date()
        time.sleep(2)
        ip.public_ip_dropdown_button()
        time.sleep(1)
        ip.public_ip_list()
        time.sleep(1)
        ip.submit_button()
        self.driver.implicitly_wait(60)
        ip.total_table_data_for_single_row()
        self.driver.save_screenshot("ip_tracking_table.png")
        self.driver.quit()


































# import os
# import time
# import pytest
#
# from Pages.Dashboardpage import Test_Login
# from Pages.loginpage import LoginPage
# from Pages.ip_tracking import Iptracking
#
#
# @pytest.mark.usefixtures("setup_and_teardown")
# class TestIpTracking:
#     def test_verify_report_login_page(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         ip = Iptracking(self.driver)
#         message = "Reports"
#         assert ip.verify_report_button().__eq__(message)
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "ip_tracking_page.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#
#     def test_report_iptracking_login_page(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
#         time.sleep(4)
#         message = "External IP Communication"
#         assert ip.verify_ip_tracking_page().__eq__(message)
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "ip_tracking_login_page.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#     def test_select_date_and_time(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(2)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
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
#         time.sleep(3)
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "ip_tracking_table_data.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#     def test_ip_tracking_display_data(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
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
#         ip.ip_tracking_table_data()
#         self.driver.quit()
#
#
#     def test_ip_tracking_table_received_data(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
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
#         ip.ip_tracking_table_data()
#         time.sleep(3)
#         ip.ip_tracking_table_received_data()
#         self.driver.quit()
#
#
#     def test_ip_tracking_table_transmitted_data(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
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
#         ip.ip_tracking_table_data()
#         time.sleep(3)
#         ip.ip_tracking_table_transmitted_data()
#         self.driver.quit()
#
#     def test_ip_tracking_table_total_data(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
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
#         ip.ip_tracking_table_data()
#         time.sleep(3)
#         ip.ip_tracking_table_total_data()
#         self.driver.quit()
#
#     def test_ip_tracking_table_verify(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
#         login = Test_Login(self.driver)
#         login.location()
#         time.sleep(2)
#         login.location_dropdown()
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
#         # ip.ip_tracking_table_data()
#         # time.sleep(3)
#         ip.verify_data()
#         self.driver.quit()
#
#
#     def test_ip_tracking_verify_single_row_table_data(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         ip = Iptracking(self.driver)
#         ip.iptracking_page()
#         login = Test_Login(self.driver)
#         login.location()
#         time.sleep(2)
#         login.location_dropdown()
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
#         ip.total_table_data_for_single_row()
#         self.driver.quit()
#
