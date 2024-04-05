from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class Login_setup:
    # @pytest.fixture()
    # def driver(self):
    #     driver=webdriver.Chrome()
    #     driver.maximize_window()
    #     yield driver
    #     driver.quit()
    driver=webdriver.Chrome()
    def test_login_page_with_credentials(self):
        # self.driver.implicitly_wait(10)
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("zebu@gmail.com")
        self.driver.find_element(By.ID, "login-password").send_keys("Tulasi@123")
        self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        time.sleep(5)
        expected_message = "Home"
        assert self.driver.find_element(By.LINK_TEXT,"Home").text.__contains__(expected_message)
#         # element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Home")))
#         # element.is_displayed()
#         # assert self.driver.find_element(By.XPATH, "MuiBox-root css-35ezg3").is_displayed()
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
        excepected_message = "Could not identify user, credentials seem to be wrong."
        assert self.driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-hkw11m']/span[1]").text.__contains__(excepected_message)
    #     # assert self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-hkw11m']/span[1]").is_displayed()
        self.driver.quit()
    def test_login_page_with_wrong_email(self):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("abc@gmail.")
        # self.driver.find_element(By.ID, "login-password").send_keys("Tulasi@123")
        # self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        expected_message = "Please enter a valid email"
        assert self.driver.find_element(By.XPATH,"//ul[@class='MuiBox-root css-dbde']/li[1]").text.__contains__(expected_message)
        time.sleep(4)
        self.driver.quit()

    def test_login_page_with_wrong_password(self):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("zebu@gmail.com")
        self.driver.find_element(By.ID, "login-password").send_keys("1234567")
        # self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]").click()
        expected_message = "Please enter valid password:"
        assert self.driver.find_element(By.XPATH,"//ul[@class='MuiBox-root css-70qvj9']/li[1]").text.__contains__(expected_message)
        self.driver.quit()

    #
    def test_login_page_with_empty_credentials(self):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.find_element(By.ID, "login-email").send_keys("")
        self.driver.find_element(By.ID, "login-password").send_keys("")
        self.driver.find_element(By.XPATH, "//button[contains(@type,'submit')]")
        expected_message= 'Enter your Login credentials'
        self.driver.find_element(By.XPATH,"//div[@class='MuiBox-root css-12re8tr']").text.__contains__(expected_message)



    def back_login_page(self):
        self.driver.find_element(By.XPATH,"//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//following::button")