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
    start_lama_button_xpath = "//button[text()='start lama']"
    verify_lama_licence_text_xpath = "//p[text()='LAMA License']"
    check_box_button_xpath = "//input[contains(@type,'checkbox')]"
    licence_read_text_xpath = "(//div[contains(@class,'MuiBox-root css-pwynxm')]/p)[13]"
    agree_button_xpath  = "(//button[contains(@type,'button')])[5]"
    verify_lama_uat_page_text_xpath = "//p[text()='LAMA Configuration']"


    def verify_lama_uat_page_text(self):
        return self.driver.find_element(By.XPATH, self.verify_lama_uat_page_text_xpath).text

    def agree_button(self):
        self.driver.find_element(By.XPATH, self.agree_button_xpath).click()

    def licence_read_text(self):

        element = self.driver.find_element(By.XPATH, self.licence_read_text_xpath)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        # print(element)
    def check_box_button(self):
        self.driver.find_element(By.XPATH, self.check_box_button_xpath).click()

    def verify_lama_licence_text(self):
        return self.driver.find_element(By.XPATH, self.verify_lama_licence_text_xpath).text

    def start_lama_button(self):
        self.driver.find_element(By.XPATH, self.start_lama_button_xpath).click()

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