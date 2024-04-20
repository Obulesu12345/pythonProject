import os
import time
import pytest
from Pages.signinpage import SignupPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSignup:
    def test_signup_verify(self):
        signup = SignupPage(self.driver)
        message = "Cloud Operating Console"
        assert signup.verify_signin_page().__eq__(message)
        with open('signup.txt', 'wt') as f:
            print("print this for successfully verify signup page", file = f)

    def test_signip_up_with_wrong_url(self):
        sign = SignupPage(self.driver)
        message = "404"
        assert sign.verify_incorrect_url_page().__eq__(message)
        with open('signup.txt', 'wt') as f:
            print("print this for successfully display 404 page", file = f)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "signup_page_with_wrong_url.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_signup_page(self):
        signup = SignupPage(self.driver)
        signup.signup()
        time.sleep(2)
        signup.email_address("abdul10@gmail.com")
        signup.email_address_password("Obu@12345")
        signup.email_confirm_password("Obu@12345")
        signup.mobile_number("8790345527")
        signup.signup_submit()
        time.sleep(2)
        message = "OTP Sent!"
        assert signup.alert_otp_msg().__eq__(message)
        time.sleep(3)
        signup.signup_otp1("1")
        signup.signup_otp2("1")
        signup.signup_otp3("1")
        signup.signup_otp4("1")
        signup.signup_otp5("1")
        signup.signup_otp6("1")
        signup.verify_email_button()
        # message = "OTP does not match"
        # assert signup.alert_otp_msg().__eq__(message)
        with open('signup.txt', 'wt') as f:
            print("print this for successfully verify signup OTP message", file = f)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "signup_page.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    def test_login_as_partner_verify_page(self):
        signup = SignupPage(self.driver)
        signup.login_as_partner()
        message = "ZyBiSys Partner Login for Partners"
        assert signup.verify_login_as_partner_logo().__eq__(message)
        with open('signup.txt', 'wt') as f:
            print(" successfully verify message is ZyBiSys Partner Login for Partners", file = f)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "verify_login_as_partner_page.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()


    def test_login_as_partner_as_verify_wrong_credentials(self):
        signup = SignupPage(self.driver)
        signup.login_as_partner()
        signup.input_email("abdul@gmail.com")
        signup.input_email_password("Tulasi@1234")
        signup.login_button()
        time.sleep(3)
        message = "Partner not found"
        assert signup.alert_otp_msg().__eq__(message)
        with open('signup.txt', 'wt') as f:
            print(" successfully verify message is Partner not found", file = f)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "verify_login_as_partner.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()



    def test_login_as_partner(self):
        signup = SignupPage(self.driver)
        signup.login_as_partner()
        signup.input_email("tulasiram.r@zybisys.com")
        signup.input_email_password("Tulasi@123")
        signup.login_button()
        time.sleep(3)
        message = "OTP sent to tulasiram.r@zybisys.com"
        assert signup.alert_otp_msg().__eq__(message)
        time.sleep(3)
        message = "Please enter the OTP that we just sent to your email address."
        assert signup.verify_enter_otp().__eq__(message)
        time.sleep(2)
        signup.otp1("1")
        signup.otp2("1")
        signup.otp3("1")
        signup.otp4("1")
        signup.otp5("1")
        signup.otp6("1")
        signup.submit()
        with open('signup.txt', 'wt') as f:
            print(" successfully verify message is Please enter the OTP that we just sent to your email address.", file = f)
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "login_as_partner.png")
        self.driver.save_screenshot(screenshot_path)
        self.driver.quit()

    # def test_blog(self):
    #     signup = SignupPage(self.driver)
    #     signup.bolg()
    #     message = "Z-Talk by Zybisys"
    #     assert signup.verify_blog().__eq__(message)
    #     with open('signup.txt', 'wt') as f:
    #         print(" successfully verify message is Z-Talk by Zybisys", file = f)







