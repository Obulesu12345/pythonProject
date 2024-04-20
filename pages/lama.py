import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Lama:

    def __init__(self,driver):
        self.driver = driver

    manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
    verify_lama_page_xpath = "//div[text()='Lama']"
    verify_uat_page_xpath = "//div[text()='UAT']"
    verify_uat_xpath = "//button[text()='start lama']"


    def verify_uat(self):
        return self.driver.find_element(By.XPATH, self.verify_uat_xpath).text

    def uat_page(self):
        self.driver.find_element(By.XPATH, self.verify_uat_page_xpath).click()

    def verify_uat_page(self):
        return self.driver.find_element(By.XPATH, self.verify_uat_page_xpath).text

    def manage_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()

    def lama_page(self):
        self.driver.find_element(By.XPATH, self.verify_lama_page_xpath).click()

    def verify_lama_page(self):
        return self.driver.find_element(By.XPATH, self.verify_lama_page_xpath).text


    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)