import os
import time
import pytest
from pages.login_page import LoginPage
from pages.instance import InstancePage
from pages.report_bandwidth import Bandwidth


@pytest.mark.usefixtures("setup_and_teardown")
class TestBandwidth:
    # def test_verify_report_login_page(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     self.driver.implicitly_wait(10)
    #     message = "Reports"
    #     band = Bandwidth(self.driver)
    #     assert band.verify_reports().__eq__(message)
    #     band.current_url()
    #     self.driver.quit()

    def test_report_bandwidth_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        message = "Bandwidth | All IP"
        assert band.verify_bandwidth_page().__eq__(message)
        band.current_url()
        self.driver.quit()

    def test_Select_date_and_time(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(1)
        band.from_date()
        time.sleep(1)
        band.to_date()
        time.sleep(2)
        band.submit_button()
        message = "Bandwidth | All IP"
        assert band.verify_bandwidth_page().__eq__(message)
        self.driver.save_screenshot("time.png")
        self.driver.quit()

    def test_Select_date_and_time_and_display_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(1)
        band.from_date()
        time.sleep(3)
        band.to_date()
        time.sleep(5)
        # band.submit_button()
        # self.driver.implicitly_wait(10)
        # message = "Bandwidth | All IP"
        # assert band.verify_bandwidth_page().__eq__(message)
        # band.band_table_data()
        # self.driver.quit()


    def test_table_verify_each_row_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(1)
        band.location()
        time.sleep(1)
        band.location_dropdown()
        band.from_date()
        time.sleep(1)
        band.to_date()
        time.sleep(1)
        band.submit_button()
        time.sleep(1)
        band.single_row_total()
        time.sleep(1)
        self.driver.save_screenshot("band_width_table_data.png")
        self.driver.quit()

    def test_csv(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(1)
        band.from_date()
        time.sleep(1)
        band.to_date()
        time.sleep(1)
        band.submit_button()
        time.sleep(1)
        band.csv()
        self.driver.save_screenshot("band_width_csv.png")
        band.table_data()
        self.driver.quit()




    # def test_table_recived_data(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     time.sleep(5)
    #     band = Bandwidth(self.driver)
    #     band.bandwidth_page()
    #     time.sleep(3)
    #     band.from_date()
    #     time.sleep(3)
    #     band.to_date()
    #     time.sleep(3)
    #     band.submit_button()
    #     time.sleep(5)
    #     band.bandwidth_table_data()
    #     time.sleep(5)
    #     band.bandwidth_table_received_data()
    #     time.sleep(5)
    #     self.driver.quit()
    #
    # def test_table_transmitted_data(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     time.sleep(5)
    #     band = Bandwidth(self.driver)
    #     band.bandwidth_page()
    #     time.sleep(3)
    #     band.from_date()
    #     time.sleep(3)
    #     band.to_date()
    #     time.sleep(3)
    #     band.submit_button()
    #     time.sleep(5)
    #     band.bandwidth_table_data()
    #     time.sleep(5)
    #     band.bandwidth_table_transmitted_data()
    #     time.sleep(5)
    #
    # def test_table_total_data(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     time.sleep(3)
    #     band = Bandwidth(self.driver)
    #     band.bandwidth_page()
    #     time.sleep(2)
    #     band.from_date()
    #     time.sleep(2)
    #     band.to_date()
    #     time.sleep(2)
    #     band.submit_button()
    #     time.sleep(3)
    #     # band.bandwidth_table_data()
    #     # time.sleep(5)
    #     band.total_table_data()
    #     time.sleep(5)


    # def test_table_verify_total_table_data(self):
    #     login_page = LoginPage(self.driver)
    #     login_page.email_address("abdul@gmail.com")
    #     login_page.email_address_password("Tulasi@1234")
    #     login_page.click_login()
    #     time.sleep(5)
    #     band = Bandwidth(self.driver)
    #     band.bandwidth_page()
    #     time.sleep(3)
    #     band.from_date()
    #     time.sleep(4)
    #     band.to_date()
    #     time.sleep(4)
    #     band.submit_button()
    #     time.sleep(2)
    #     band.verify_the_total_table_data()
    #     self.driver.quit()





























