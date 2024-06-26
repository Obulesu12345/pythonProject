import os
import time
import pytest

from pages.dashboard import Test_Login
from pages.login_page import LoginPage
from pages.geo_traffic import GeoTraffic


@pytest.mark.usefixtures("setup_and_teardown")
class TestGeotraffic:
    # def test_verify_report_login_page(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     self.driver.implicitly_wait(10)
    #     geo = GeoTraffic(self.driver)
    #     time.sleep(2)
    #     message = "Reports"
    #     assert geo.verify_report_button().__eq__(message)


    def test_report_geotraffice_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        geo = GeoTraffic(self.driver)
        geo.topapps_page()
        time.sleep(2)
        message = "Public IP"
        assert geo.verify_geo_traffic_page().__eq__(message)
        geo.current_url()
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "geottaffic_login.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_select_date_and_time(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        geo = GeoTraffic(self.driver)
        geo.topapps_page()
        time.sleep(1)
        geo.from_date()
        time.sleep(1)
        geo.to_date()
        time.sleep(1)
        geo.public_ip_dropdown_button()
        time.sleep(1)
        geo.public_ip_list()
        time.sleep(1)
        geo.submit_button()
        time.sleep(1)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "geottaffic_table.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_geo_traffic_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        geo = GeoTraffic(self.driver)
        geo.location()
        time.sleep(1)
        geo.location_dropdown()
        time.sleep(1)
        geo.topapps_page()
        time.sleep(1)
        geo.from_date()
        time.sleep(1)
        geo.to_date()
        time.sleep(1)
        geo.public_ip_dropdown_button()
        time.sleep(1)
        geo.public_ip_list()
        time.sleep(1)
        geo.submit_button()
        time.sleep(20)
        geo.table_title()
        geo.geo_traffic_table_data()
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "geo_tracking_table1.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


    # def test_geo_traffic_table_data_verify(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     self.driver.implicitly_wait(10)
    #     geo = GeoTraffic(self.driver)
    #     geo.location()
    #     time.sleep(1)
    #     geo.location_dropdown()
    #     time.sleep(1)
    #     geo.topapps_page()
    #     time.sleep(1)
    #     geo.from_date()
    #     time.sleep(1)
    #     geo.to_date()
    #     time.sleep(1)
    #     geo.public_ip_dropdown_button()
    #     time.sleep(1)
    #     geo.public_ip_list()
    #     time.sleep(1)
    #     geo.submit_button()
    #     time.sleep(1)
    #     geo.verify_data()
    #     folder_path = "screenshots"
    #     screenshot_path = os.path.join(folder_path, "geo_tracking_table1.png")
    #     self.driver.save_screenshot(screenshot_path)
    #     self.driver.quit()

    def test_ip_tracking_verify_each_row_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        geo = GeoTraffic(self.driver)
        geo.location()
        time.sleep(1)
        geo.location_dropdown()
        time.sleep(1)
        geo.topapps_page()
        time.sleep(1)
        geo.from_date()
        time.sleep(1)
        geo.to_date()
        time.sleep(1)
        geo.public_ip_dropdown_button()
        time.sleep(1)
        geo.public_ip_list()
        time.sleep(1)
        geo.submit_button()
        self.driver.implicitly_wait(60)
        geo.rows_per_page()
        time.sleep(2)
        geo.rows_per_page_dropdown()
        time.sleep(2)
        geo.total_table_data_for_each_single_row()
        self.driver.quit()

    def test_geo_traffic_csv(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        geo = GeoTraffic(self.driver)
        geo.topapps_page()
        time.sleep(1)
        geo.from_date()
        time.sleep(1)
        geo.to_date()
        time.sleep(1)
        geo.public_ip_dropdown_button()
        time.sleep(1)
        geo.public_ip_list()
        time.sleep(1)
        geo.submit_button()
        time.sleep(1)
        geo.csv()
        time.sleep(3)
        message = "report send to your mail sonu.verma@zybisys.com, tulasiram.r@zybisys.com, parameswari.t@zybisys.com"
        assert geo.alert_otp_msg().__eq__(message)
        self.driver.quit()
























# import os
# import time
# import pytest
#
# from Pages.Dashboardpage import Test_Login
# from Pages.loginpage import LoginPage
# from Pages.geo_traffice import GeoTraffic
#
#
# @pytest.mark.usefixtures("setup_and_teardown")
# class TestGeotraffic:
#     def test_verify_report_login_page(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(2)
#         geo = GeoTraffic(self.driver)
#         time.sleep(2)
#         message = "Reports"
#         assert geo.verify_report_button().__eq__(message)
#
#
#     def test_report_geotraffice_login_page(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(2)
#         geo = GeoTraffic(self.driver)
#         geo.topapps_page()
#         time.sleep(2)
#         message = "City Wise Traffic | Ip not found"
#         assert geo.verify_geo_traffic_page().__eq__(message)
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "geottaffic_login.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#     def test_select_date_and_time(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(2)
#         geo = GeoTraffic(self.driver)
#         geo.topapps_page()
#         time.sleep(2)
#         geo.from_date()
#         time.sleep(1)
#         geo.to_date()
#         time.sleep(1)
#         geo.public_ip_dropdown_button()
#         time.sleep(1)
#         geo.public_ip_list()
#         time.sleep(1)
#         geo.submit_button()
#         time.sleep(1)
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "geottaffic_table.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#     def test_geo_traffic_table_verify(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         geo = GeoTraffic(self.driver)
#         geo.location()
#         time.sleep(2)
#         geo.location_dropdown()
#         time.sleep(2)
#         geo.topapps_page()
#         time.sleep(2)
#         geo.from_date()
#         time.sleep(1)
#         geo.to_date()
#         time.sleep(1)
#         geo.public_ip_dropdown_button()
#         time.sleep(1)
#         geo.public_ip_list()
#         time.sleep(1)
#         geo.submit_button()
#         time.sleep(3)
#         geo.table_title()
#         self.driver.implicitly_wait(20)
#         geo.summary_table_data()
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "geo_tracking_table1.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#
#     def test_geo_traffic_table_data_verify(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         self.driver.implicitly_wait(10)
#         geo = GeoTraffic(self.driver)
#         geo.location()
#         time.sleep(5)
#         geo.location_dropdown()
#         time.sleep(3)
#         geo.topapps_page()
#         time.sleep(4)
#         geo.from_date()
#         time.sleep(4)
#         geo.to_date()
#         time.sleep(4)
#         geo.public_ip_dropdown_button()
#         time.sleep(3)
#         geo.public_ip_list()
#         time.sleep(3)
#         geo.submit_button()
#         time.sleep(2)
#         geo.verify_data()
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "geo_tracking_table1.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
