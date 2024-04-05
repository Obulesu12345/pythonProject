import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://dev.zybisys.com/login'

class Test_Login:
    @pytest.fixture()
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        yield self.driver
        self.driver.quit()


    def test_login_page(self):

        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        message = 'Cloud Operating Console'
        assert self.driver.find_element(By.XPATH,"//h3[@class='MuiTypography-root MuiTypography-h3 css-tzvxie']").text.__contains__(message)
        self.driver.quit()

    def test_login_page_with_credentials(self):

        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("zebu@gmail.com")
        self.driver.find_element(By.ID, "login-password").send_keys("Tulasi@123")
        self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        time.sleep(5)
        message = "Home"
        assert self.driver.find_element(By.LINK_TEXT,"Home").text.__contains__(message)
        self.driver.quit()

    def test_login_page_with_wrong_credentials(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("zabc@gmail.com")
        self.driver.find_element(By.ID, "login-password").send_keys("Tulasi@123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        time.sleep(3)
        message = "Could not identify user, credentials seem to be wrong."
        assert self.driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-hkw11m']/span[1]").text.__contains__(message)
    #     # assert self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-hkw11m']/span[1]").is_displayed()
        self.driver.quit()
    def test_login_page_with_wrong_email(self):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("abc@gmail.")
        # self.driver.find_element(By.ID, "login-password").send_keys("Tulasi@123")
        # self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        message = "Please enter a valid email"
        assert self.driver.find_element(By.XPATH,"//ul[@class='MuiBox-root css-dbde']/li[1]").text.__contains__(message)
        time.sleep(4)
        self.driver.quit()

    def test_login_page_with_wrong_password(self):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("zebu@gmail.com")
        self.driver.find_element(By.ID, "login-password").send_keys("1234567")
        # self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        message = "Please enter valid password:"
        assert self.driver.find_element(By.XPATH,"//ul[@class='MuiBox-root css-70qvj9']/li[1]").text.__contains__(message)
        self.driver.quit()

    def test_login_page_with_empty_credentials(self):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("")
        self.driver.find_element(By.ID, "login-password").send_keys("")
        self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        message= 'Enter your Login credentials'
        assert self.driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-12re8tr']").text.__contains__(message)
        self.driver.quit()

    def test_forgot_password(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.find_element(By.PARTIAL_LINK_TEXT,"Forgot ").click()
        time.sleep(4)
        message = 'Forgot Password?'
        assert self.driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-8atqhb']/h3[1]").text.__contains__(message)
        self.driver.quit()

    def test_forgot_password_entered_wrong_mail(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT,"Forgot Password?").click()
        time.sleep(3)
        self.driver.find_element(By.ID,"forgot-password-email").send_keys("abc@gmail.c")
        time.sleep(4)
        message = 'Please enter a valid email'
        assert self.driver.find_element(By.XPATH,"//ul[@class='MuiBox-root css-dbde']/li[1]").text.__contains__(message)
        self.driver.quit()

    def test_forgot_password_entered_with_mail(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT,"Forgot Password?").click()
        time.sleep(3)
        self.driver.find_element(By.ID,"forgot-password-email").send_keys("zebu@gmail.com")
        self.driver.implicitly_wait(10)
        reset_paasword = self.driver.find_element(By.XPATH,"//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//preceding::button")
        assert reset_paasword.is_displayed()
        time.sleep(4)
        self.driver.quit()

    def test_forgot_password_reset(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Forgot Password?").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "forgot-password-email").send_keys("zebu@gmail.com")
        reset_paasword = self.driver.find_element(By.XPATH,"//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//preceding::button")
        reset_paasword.click()
        time.sleep(5)
        message = 'We have sent an OTP to zebu@gmail.com. Please check your inbox/spam folder and enter the OTP to proceed'
        assert self.driver.find_element(By.XPATH,"//p[@class='MuiTypography-root MuiTypography-body1 css-1gjww4s']").text.__contains__(message)
        time.sleep(4)
        self.driver.quit()


    def test_forgot_password_back_to_login(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Forgot Password?").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,"//button[contains(@type,'button')]//child::span[1]").click()
        message = 'Welcome Back!'
        assert self.driver.find_element(By.XPATH,"//h3[@class='MuiTypography-root MuiTypography-h3 css-b309xq']").text.__contains__(message)
        time.sleep(4)
        self.driver.quit()
    def test_forgot_password_reset(self):
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Forgot Password?").click()
        time.sleep(3)
        self.driver.find_element(By.ID, "forgot-password-email").send_keys("zebu@gmail.com")
        reset_paasword = self.driver.find_element(By.XPATH,"//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//preceding::button")
        reset_paasword.click()
        self.driver.find_element(By.XPATH)
        time.sleep(4)
        self.driver.quit()














