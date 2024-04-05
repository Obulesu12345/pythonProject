import time
import pytest
from Pages.loginpage import LoginPage
from Pages.instance import InstancePage
from Pages.profile_page import ProfilePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestProfile:
    def test_verify_profile_login_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        message = "Profile"
        profile = ProfilePage(self.driver)
        assert profile.verify_profile_page().__eq__(message)
        self.driver.quit()

    def test_profile_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        profile = ProfilePage(self.driver)
        profile.profile_page()
        time.sleep(3)
        message = "Personal Details"
        assert profile.verify_page().__eq__(message)
        self.driver.quit()
