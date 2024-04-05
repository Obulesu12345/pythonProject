import time
import pytest

from Pages.Dashboardpage import Test_Login
from Pages.loginpage import LoginPage
from Pages.topapps import Topapps


@pytest.mark.usefixtures("setup_and_teardown")
class TestTopapps:
    def test_verify_report_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        apps = Topapps(self.driver)
        time.sleep(3)
        message = "Reports"
        assert apps.verify_report_button().__eq__(message)

    def test_report_topapps_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        apps = Topapps(self.driver)
        apps.topapps_page()
        time.sleep(4)
        message = "From"
        assert apps.verify_apps_page().__eq__(message)
        self.driver.quit()

    def test_select_date_and_time(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
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
        time.sleep(5)


    def test_top_apps_table_received_data(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        ip = Topapps(self.driver)
        login = Test_Login(self.driver)
        login.Hover_over_dashboard()
        login.location()
        time.sleep(5)
        login.location_dropdown()
        ip.topapps_page()
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
        time.sleep(4)
        # ip.topapps_table_data()
        # time.sleep(3)
        ip.topapps_table_received_data()
        self.driver.quit()


    def test_top_apps_table_verify(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(3)
        apps = Topapps(self.driver)
        apps.location()
        time.sleep(5)
        apps.location_dropdown()
        time.sleep(3)
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
        time.sleep(4)
        # apps.topapps_table_data()
        time.sleep(3)
        apps.verify_data()
        self.driver.quit()