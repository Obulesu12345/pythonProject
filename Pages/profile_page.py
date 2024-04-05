import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProfilePage:

    def __init__(self,driver):
        self.driver = driver

    verify_profile_page_xpath = "(//*[text()='Profile'])[1]"

    profile_page_xpath = "(//*[text()='Profile'])[1]"

    verify_page_xpath = "(//*[text()='Personal Details'])"

    def verify_page(self):
        return self.driver.find_element(By.XPATH, self.verify_page_xpath).text

    def verify_profile_page(self):
        return self.driver.find_element(By.XPATH, self.verify_profile_page_xpath).text

    def profile_page(self):
        self.driver.find_element(By.XPATH, self.profile_page_xpath).click()