import os
import time
import pytest
from Pages.loginpage import LoginPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_verify(self):
        login = LoginPage(self.driver)
        message = "Cloud Operating Console"
        assert login.verify_login_page().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_page_verify.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_incorrect_url(self):
        login = LoginPage(self.driver)
        message = "404"
        assert login.verify_incorrect_url_page().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)

        self.driver.quit()

    def test_login_page_with_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        message = "Home"
        assert login_page.Home_page().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_with_credentials.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_login_page_with_wrong_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdulabc@gmail.com")
        login_page.email_address_password("Tulasi@123")
        login_page.click_login()
        message = "Enter your Login credentials"
        assert login_page.verify_message_wrong_credentials().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_wrong_credentials.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_login_page_with_wrong_email(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abc@gmail.")
        message = "Please enter a valid email"
        assert login_page.verify_message_wrong_mail.__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_wrong_email.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_login_page_with_wrong_password(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("1234567")
        message = "Please enter valid password:"
        assert login_page.verify_message_wrong_password.__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_wrong_password.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_login_page_with_empty_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("")
        login_page.email_address_password("")
        # login_page.click_login()
        message= 'Enter your Login credentials'
        assert login_page.verify_credentials().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        self.driver.quit()

    def test_forgot_password(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot()
        message = 'Forgot Password?'
        assert login_page.verify_forgot_password.__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_forgot_password.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()
    #
    def test_forgot_password_entered_wrong_mail(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot()
        time.sleep(3)
        login_page.forgot_email_address("abc@gmail.c")
        message = 'Please enter a valid email'
        assert login_page.verify_forgot_enter_email.__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "log_in_forgot_password_wrong_email.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_forgot_password_entered_with_mail(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot()
        time.sleep(3)
        login_page.forgot_email_address("zebu@gmail.com")
        time.sleep(3)
        reset_paasword = login_page.verify_reset_button()
        assert reset_paasword.is_displayed()
        current_url = self.driver.current_url
        print(current_url)
        self.driver.quit()

    def test_forgot_password_reset(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot()
        time.sleep(3)
        login_page.forgot_email_address("zebu@gmail.com")
        time.sleep(3)
        reset_paasword = login_page.verify_reset_button()
        reset_paasword.click()
        message = 'We have sent an OTP to zebu@gmail.com. Please check your inbox/spam folder and enter the OTP to proceed'
        login_page.verify_otp_message.__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_password_reset.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_forgot_password_otp(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot()
        time.sleep(3)
        login_page.forgot_email_address("abdul@gmail.com")
        time.sleep(1)
        # reset_paasword = login_page.verify_reset_button()
        login_page.reset_password_button()
        time.sleep(2)
        login_page.login_otp1("1")
        time.sleep(1)
        login_page.login_otp2("1")
        time.sleep(1)
        login_page.login_otp3("1")
        time.sleep(1)
        login_page.login_otp4("1")
        time.sleep(1)
        login_page.login_otp5("1")
        time.sleep(1)
        login_page.login_otp6("1")
        time.sleep(1)
        # message = "Please enter the OTP that we just sent to your email address."
        # assert reset_paasword.verify_enter_otp().__eq__(message)
        login_page.submit()
        time.sleep(2)
        login_page.forgot_new_password("Tulasi@1234")
        login_page.forgot_confirm_password("Tulasi@1234")
        login_page.forgot_set_password_button()
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_forgot_password_otp.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_login_page_with_after_the_password(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        message = "Instances"
        assert login_page.verify_log_in_page_instance_xpath().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_dashboard_page.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_forgot_password_back_to_login(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot()
        time.sleep(3)
        login_page.login_back_button()
        message = 'Welcome Back!'
        assert login_page.verify_login_back().__eq__(message)
        current_url = self.driver.current_url
        print(current_url)
        self.driver.quit()

    def test_logout_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        message = "Home"
        assert login_page.Home_page().__eq__(message)
        login_page.logout_button()
        time.sleep(3)
        message = "Abdul"
        login_page.verify_logout_username().__eq__(message)
        login_page.logout()
        message1 = 'Welcome Back!'
        login_page.verify_logout().__eq__(message1)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_verify_page.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()



