import os
import time
import pytest
from Pages.loginpage import LoginPage
from Pages.instance import InstancePage
from Pages.Report_bandwidth import Bandwidth


@pytest.mark.usefixtures("setup_and_teardown")
class TestBandwidth:
    def test_verify_report_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        message = "Reports"
        band = Bandwidth(self.driver)
        assert band.verify_reports().__eq__(message)
        self.driver.quit()

    def test_report_bandwidth_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        message = "Bandwidth | All IP"
        assert band.verify_bandwidth_page().__eq__(message)
        self.driver.quit()

    def test_Select_date_and_time(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(4)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        band.from_date()
        time.sleep(3)
        # band.to_date()
        # time.sleep(3)
        # band.submit_button()
        # time.sleep(5)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "time.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_Select_date_and_time_and_display_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        band.from_date()
        time.sleep(3)
        band.to_date()
        time.sleep(3)
        band.submit_button()
        time.sleep(5)
        band.bandwidth_table_data()
        self.driver.quit()

    def test_table_recived_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        band.from_date()
        time.sleep(3)
        band.to_date()
        time.sleep(3)
        band.submit_button()
        time.sleep(5)
        band.bandwidth_table_data()
        time.sleep(5)
        band.bandwidth_table_received_data()
        time.sleep(5)
        self.driver.quit()

    def test_table_transmitted_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        band.from_date()
        time.sleep(3)
        band.to_date()
        time.sleep(3)
        band.submit_button()
        time.sleep(5)
        band.bandwidth_table_data()
        time.sleep(5)
        band.bandwidth_table_transmitted_data()
        time.sleep(5)

    def test_table_total_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(3)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(2)
        band.from_date()
        time.sleep(2)
        band.to_date()
        time.sleep(2)
        band.submit_button()
        time.sleep(3)
        # band.bandwidth_table_data()
        # time.sleep(5)
        band.total_table_data()
        time.sleep(5)


    def test_table_verify_total_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        band.from_date()
        time.sleep(3)
        band.to_date()
        time.sleep(3)
        band.submit_button()
        time.sleep(2)
        band.verify_the_total_table_data()
        self.driver.quit()


    def test_table_verify_single_row_table_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        band = Bandwidth(self.driver)
        band.bandwidth_page()
        time.sleep(3)
        band.from_date()
        time.sleep(3)
        band.to_date()
        time.sleep(3)
        band.submit_button()
        time.sleep(2)
        band.total_table_data_for_single_row()
        self.driver.quit()



