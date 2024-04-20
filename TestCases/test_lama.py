import time
import pytest

from Pages.lama import Lama
from Pages.loginpage import LoginPage
from Pages.instance import InstancePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestLama:
    def test_lama_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        lama = Lama(self.driver)
        lama.manage_page()
        time.sleep(1)
        message = "Lama"
        assert lama.verify_lama_page().__eq__(message)
        lama.current_url()
        self.driver.save_screenshot("lama.png")
        self.driver.quit()

    def test_lama_uat_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        lama = Lama(self.driver)
        lama.manage_page()
        time.sleep(1)
        lama.lama_page()
        time.sleep(1)
        message = "UAT"
        assert lama.verify_uat_page().__eq__(message)
        lama.current_url()
        self.driver.save_screenshot("uat.png")
        self.driver.quit()

    def test_lama_verify_uat_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        lama = Lama(self.driver)
        lama.manage_page()
        time.sleep(1)
        lama.lama_page()
        time.sleep(1)
        lama.uat_page()
        time.sleep(1)
        message = "START LAMA"
        assert lama.verify_uat().__eq__(message)
        lama.current_url()
        self.driver.save_screenshot("uat.png")
        self.driver.quit()