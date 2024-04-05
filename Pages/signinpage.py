import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
class SignupPage:

    def __init__(self,driver):
        self.driver = driver

    signup_xpath = "//a[text()='Sign Up']"
    company_email_id = "login-email"
    set_password_id = "login-password"
    confirm_password_id = "login-confirmPassword"
    mobile_id = "outlined-basic"
    signup_button_xpath = "//button[text()='Sign Up']"
    verify_signinpage_xpath = "//h3[text()='Cloud Operating Console']"

    login_as_partner_xpath = "//button[text()='Login as Partner']"
    input_email_xpath ="//input[@id='login-email']"
    input_mail_password = "//input[@id='login-password']"
    login_button_xpath = "//button[text()='Login']"

    enter_otp1_id = "otp-0"
    enter_otp2_id = "otp-1"
    enter_otp3_id = "otp-2"
    enter_otp4_id = "otp-3"
    enter_otp5_id = "otp-4"
    enter_otp6_id = "otp-5"
    verify_enter_otp_xpath = "//p[text()='Please enter the OTP that we just sent to your email address.']"
    enter_otp_submit_xpath = "//button[text()='Submit']"

    temrs_and_conditions_link_text = "Terms & Conditions"
    blog_link_text = "Blog"
    verify_bolg_xpath = "//h1[text()='Z-Talk by Zybisys']"

    verify_sign_up_page_xpath = "//h4[contains(@class,'MuiTypography-root MuiTypography-h4 css-kh6z3e')]"

    verify_create_account_xpath = "//*[contains(@class,'MuiTypography-root MuiTypography-caption css-1mbwc4g')]"
    partner_not_found_xpath = "//*[@class='w-11/12 mt-8']/p"

    verify_incorrect_url_page_xpath = "//*[text()='404']"

    alert_otp_msg_xpath = "//div[contains(@role,'alert')]"

    signup_otp1_xpath = "//input[contains(@aria-label,'Please enter verification code. Digit 1')]"
    signup_otp2_xpath ="//input[contains(@aria-label,'Digit 2')]"
    signup_otp3_xpath = "//input[contains(@aria-label,'Digit 3')]"
    signup_otp4_xpath = "//input[contains(@aria-label,'Digit 4')]"
    signup_otp5_xpath = "//input[contains(@aria-label,'Digit 5')]"
    signup_otp6_xpath = "//input[contains(@aria-label,'Digit 6')]"

    verify_email_button_xpath = "//button[contains(@type,'submit')]"


    verify_login_as_partner_logo_xpath = "//*[text()='ZyBiSys Partner Login for Partners']"

    def verify_login_as_partner_logo(self):
        return self.driver.find_element(By.XPATH, self.verify_login_as_partner_logo_xpath).text
    def verify_email_button(self):
        self.driver.find_element(By.XPATH, self.verify_email_button_xpath).click()

    def signup_otp1(self,text):
        self.driver.find_element(By.XPATH, self.signup_otp1_xpath).click()
        self.driver.find_element(By.XPATH, self.signup_otp1_xpath).clear()
        self.driver.find_element(By.XPATH, self.signup_otp1_xpath).send_keys(text)

    def signup_otp2(self,text):
        self.driver.find_element(By.XPATH, self.signup_otp2_xpath).click()
        self.driver.find_element(By.XPATH, self.signup_otp2_xpath).clear()
        self.driver.find_element(By.XPATH, self.signup_otp2_xpath).send_keys(text)

    def signup_otp3(self,text):
        self.driver.find_element(By.XPATH, self.signup_otp3_xpath).click()
        self.driver.find_element(By.XPATH, self.signup_otp3_xpath).clear()
        self.driver.find_element(By.XPATH, self.signup_otp3_xpath).send_keys(text)

    def signup_otp4(self,text):
        self.driver.find_element(By.XPATH, self.signup_otp4_xpath).click()
        self.driver.find_element(By.XPATH, self.signup_otp4_xpath).clear()
        self.driver.find_element(By.XPATH, self.signup_otp4_xpath).send_keys(text)

    def signup_otp5(self,text):
        self.driver.find_element(By.XPATH, self.signup_otp5_xpath).click()
        self.driver.find_element(By.XPATH, self.signup_otp5_xpath).clear()
        self.driver.find_element(By.XPATH, self.signup_otp5_xpath).send_keys(text)

    def signup_otp6(self, text):
        self.driver.find_element(By.XPATH, self.signup_otp6_xpath).click()
        self.driver.find_element(By.XPATH, self.signup_otp6_xpath).clear()
        self.driver.find_element(By.XPATH, self.signup_otp6_xpath).send_keys(text)


    def alert_otp_msg(self):
        return self.driver.find_element(By.XPATH, self.alert_otp_msg_xpath).text

    def verify_incorrect_url_page(self):
        return self.driver.find_element(By.XPATH, self.verify_incorrect_url_page_xpath).text

    def partner_not_found(self):
        return self.driver.find_element(By.XPATH, self.partner_not_found_xpath).text

    def verify_create_account(self):
        return self.driver.find_element(By.XPATH, self.verify_create_account_xpath).text

    # def capture_url(self):
    #     current_url = driver.current_url
    #     print(current_url)

    def verify_sign_up_page(self):
        return self.driver.find_element(By.XPATH, self.verify_sign_up_page_xpath).text
    def verify_current_url(self):
        driver = webdriver.Chrome()
        driver.get("https://dev.zybisys.com/signup12")
        driver.maximize_window()
        current_url = driver.current_url
        print(current_url)
    def bolg(self):
        self.driver.find_element(By.LINK_TEXT,self.blog_link_text).click()
    def verify_blog(self):
        return self.driver.find_element(By.XPATH,self.verify_bolg_xpath).text



    def verify_enter_otp(self):
        return self.driver.find_element(By.XPATH, self.verify_enter_otp_xpath).text
    def submit(self):
        self.driver.find_element(By.XPATH, self.enter_otp_submit_xpath).click()
    def otp1(self,text):
        self.driver.find_element(By.ID, self.enter_otp1_id).click()
        self.driver.find_element(By.ID, self.enter_otp1_id).clear()
        self.driver.find_element(By.ID, self.enter_otp1_id).send_keys(text)

    def otp2(self,text):
        self.driver.find_element(By.ID, self.enter_otp2_id).click()
        self.driver.find_element(By.ID, self.enter_otp2_id).clear()
        self.driver.find_element(By.ID, self.enter_otp2_id).send_keys(text)

    def otp3(self,text):
        self.driver.find_element(By.ID, self.enter_otp3_id).click()
        self.driver.find_element(By.ID, self.enter_otp3_id).clear()
        self.driver.find_element(By.ID, self.enter_otp3_id).send_keys(text)

    def otp4(self,text):
        self.driver.find_element(By.ID, self.enter_otp4_id).click()
        self.driver.find_element(By.ID, self.enter_otp4_id).clear()
        self.driver.find_element(By.ID, self.enter_otp4_id).send_keys(text)

    def otp5(self,text):
        self.driver.find_element(By.ID, self.enter_otp5_id).click()
        self.driver.find_element(By.ID, self.enter_otp5_id).clear()
        self.driver.find_element(By.ID, self.enter_otp5_id).send_keys(text)

    def otp6(self,text):
        self.driver.find_element(By.ID, self.enter_otp6_id).click()
        self.driver.find_element(By.ID, self.enter_otp6_id).clear()
        self.driver.find_element(By.ID, self.enter_otp6_id).send_keys(text)


    def login_as_partner(self):
        self.driver.find_element(By.XPATH, self.login_as_partner_xpath).click()

    def input_email(self,email_text):
        self.driver.find_element(By.XPATH, self.input_email_xpath).click()
        self.driver.find_element(By.XPATH, self.input_email_xpath).clear()
        self.driver.find_element(By.XPATH, self.input_email_xpath).send_keys(email_text)

    def input_email_password(self,email_password):
        self.driver.find_element(By.XPATH, self.input_mail_password).click()
        self.driver.find_element(By.XPATH, self.input_mail_password).clear()
        self.driver.find_element(By.XPATH, self.input_mail_password).send_keys(email_password)

    def login_button(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()


    def signup(self):
        self.driver.find_element(By.XPATH, self.signup_xpath).click()

    def email_address(self,email_addrees_text):
        self.driver.find_element(By.ID, self.company_email_id).click()
        self.driver.find_element(By.ID, self.company_email_id).clear()
        self.driver.find_element(By.ID, self.company_email_id).send_keys(email_addrees_text)

    def email_address_password(self,email_password_address):
        self.driver.find_element(By.ID, self.set_password_id).click()
        self.driver.find_element(By.ID, self.set_password_id).clear()
        self.driver.find_element(By.ID, self.set_password_id).send_keys(email_password_address)

    def email_confirm_password(self,email_confirm_address):
        self.driver.find_element(By.ID, self.confirm_password_id).click()
        self.driver.find_element(By.ID, self.confirm_password_id).clear()
        self.driver.find_element(By.ID, self.confirm_password_id).send_keys(email_confirm_address)

    def mobile_number(self,mobile_number):
        self.driver.find_element(By.ID, self.mobile_id).click()
        self.driver.find_element(By.ID, self.mobile_id).clear()
        self.driver.find_element(By.ID, self.mobile_id).send_keys(mobile_number)

    def signup_submit(self):
        self.driver.find_element(By.XPATH, self.signup_button_xpath).click()

    def verify_signin_page(self):
        return self.driver.find_element(By.XPATH, self.verify_signinpage_xpath).text
