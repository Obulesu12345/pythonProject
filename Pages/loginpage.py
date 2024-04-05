from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    verify_page_xpath = "//h3[text()='Cloud Operating Console']"
    email_text_xpath = "//input[@id='login-email']"
    emai_password_xpath = "//input[@id='login-password']"
    click_login_xpath = "//button[contains(@type,'submit')]"
    home_link_text = "Home"
    verify_message_xpath = "//div[text()='Enter your Login credentials']"

    wrong_mail_xpath = "//ul[@class='MuiBox-root css-dbde']/li[1]"
    valid_password_xpath = "//ul[@class='MuiBox-root css-70qvj9']/li[1]"
    verify_login_credentials_xpath = "//div[@class='MuiBox-root css-12re8tr']"
    forgot_button_link_text = "Forgot Password?"
    verify_forgot_password_xpath = "//div[@class='MuiBox-root css-8atqhb']/h3[1]"
    enter_forgot_password_emai_id = "forgot-password-email"
    forgot_entered_email_id = "//ul[@class='MuiBox-root css-dbde']/li[1]"
    verify_reset_password_button_xpath = "//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//preceding::button"
    verify_otp_message_xpath = "//p[@class='MuiTypography-root MuiTypography-body1 css-1gjww4s']"
    login_back_xpath = "//button[contains(@type,'button')]//child::span[1]"
    verify_login_back_xpath = "//h3[@class='MuiTypography-root MuiTypography-h3 css-b309xq']"
    verify_incorrect_url_page_xpath = "//*[text()='404']"

    logout_button_xpath = "//*[@class='MuiSvgIcon-root MuiSvgIcon-fontSizeMedium css-9u5na5']"
    verify_logout_username_xpath = "//div[text()='Abdul']"
    logout_xpath = "//span[text()='Logout']"
    verify_logout_xpath = "//h3[text()='Welcome Back!']"

    reset_password_button_xpath = "//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//preceding::button"

    enter_otp1_xpath = "//input[contains(@aria-label,'Please enter verification code. Digit 1')]"
    enter_otp2_xpath = "//input[contains(@aria-label,'Digit 2')]"
    enter_otp3_xpath = "//input[contains(@aria-label,'Digit 3')]"
    enter_otp4_xpath = "//input[contains(@aria-label,'Digit 4')]"
    enter_otp5_xpath = "//input[contains(@aria-label,'Digit 5')]"
    enter_otp6_xpath = "//input[contains(@aria-label,'Digit 6')]"
    verify_enter_otp_xpath = "//p[text()='Please enter the OTP that we just sent to your email address.']"
    enter_otp_submit_xpath = "//button[text()='Continue']"

    forgot_new_password_xpath = "//input[@name='newPassword']"
    forgot_confirm_password_xpath = "//input[@name='confirmPassword']"
    forgot_set_password_button_xpath = "//button[text()='Set Password']"

    verify_log_in_page_xpath = "(//*[text()='Instances'])[2]"

    def verify_log_in_page_instance_xpath(self):
        return self.driver.find_element(By.XPATH, self.verify_log_in_page_xpath).text

    # def verify_current_url(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://dev.zybisys.com/loginewkjef")
    #     driver.maximize_window()
    #     current_url = driver.current_url
    #     print(current_url)

    def forgot_new_password(self,new_password):
        self.driver.find_element(By.XPATH, self.forgot_new_password_xpath).click()
        self.driver.find_element(By.XPATH, self.forgot_new_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.forgot_new_password_xpath).send_keys(new_password)

    def forgot_confirm_password(self,confirm_password):
        self.driver.find_element(By.XPATH, self.forgot_confirm_password_xpath).click()
        self.driver.find_element(By.XPATH, self.forgot_confirm_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.forgot_confirm_password_xpath).send_keys(confirm_password)

    def forgot_set_password_button(self):
        self.driver.find_element(By.XPATH, self.forgot_set_password_button_xpath).click()

    def verify_enter_otp(self):
        return self.driver.find_element(By.XPATH, self.verify_enter_otp_xpath).text

    def submit(self):
        self.driver.find_element(By.XPATH, self.enter_otp_submit_xpath).click()

    def reset_password_button(self):
        self.driver.find_element(By.XPATH, self.reset_password_button_xpath).click()


    def login_otp1(self,text_otp1):
        self.driver.find_element(By.XPATH, self.enter_otp1_xpath).click()
        self.driver.find_element(By.XPATH, self.enter_otp1_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_otp1_xpath).send_keys(text_otp1)

    def login_otp2(self,text_otp2):
        self.driver.find_element(By.XPATH, self.enter_otp2_xpath).click()
        self.driver.find_element(By.XPATH, self.enter_otp2_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_otp2_xpath).send_keys(text_otp2)

    def login_otp3(self,text_otp3):
        self.driver.find_element(By.XPATH, self.enter_otp3_xpath).click()
        self.driver.find_element(By.XPATH, self.enter_otp3_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_otp3_xpath).send_keys(text_otp3)

    def login_otp4(self,text_otp4):
        self.driver.find_element(By.XPATH, self.enter_otp4_xpath).click()
        self.driver.find_element(By.XPATH, self.enter_otp4_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_otp4_xpath).send_keys(text_otp4)

    def login_otp5(self,text_otp5):
        self.driver.find_element(By.XPATH, self.enter_otp5_xpath).click()
        self.driver.find_element(By.XPATH, self.enter_otp5_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_otp5_xpath).send_keys(text_otp5)

    def login_otp6(self,text_otp6):
        self.driver.find_element(By.XPATH, self.enter_otp6_xpath).click()
        self.driver.find_element(By.XPATH, self.enter_otp6_xpath).clear()
        self.driver.find_element(By.XPATH, self.enter_otp6_xpath).send_keys(text_otp6)


    def logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

    def verify_logout_username(self):
        return self.driver.find_element(By.XPATH, self.verify_logout_username_xpath).text

    def logout(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()

    def verify_logout(self):
        return self.driver.find_element(By.XPATH, self.verify_logout_xpath).text


    def verify_incorrect_url_page(self):
        return self.driver.find_element(By.XPATH, self.verify_incorrect_url_page_xpath).text
    def verify_login_page(self):
        return self.driver.find_element(By.XPATH, self.verify_page_xpath).text

    def email_address(self,email_addrees_text):
        self.driver.find_element(By.XPATH, self.email_text_xpath).click()
        self.driver.find_element(By.XPATH, self.email_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_text_xpath).send_keys(email_addrees_text)

    def email_address_password(self,email_password_address):
        self.driver.find_element(By.XPATH, self.emai_password_xpath).click()
        self.driver.find_element(By.XPATH, self.emai_password_xpath).clear()
        self.driver.find_element(By.XPATH, self.emai_password_xpath).send_keys(email_password_address)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.click_login_xpath).click()

    def Home_page(self):
        return self.driver.find_element(By.LINK_TEXT, self.home_link_text).text

    def verify_message_wrong_credentials(self):
        return self.driver.find_element(By.XPATH, self.verify_message_xpath).text

    def verify_message_wrong_mail(self):
        return self.driver.find_element(By.XPATH, self.wrong_mail_xpath).text

    def verify_message_wrong_password(self):
        return self.driver.find_element(By.XPATH, self.valid_password_xpath).text

    def verify_credentials(self):
        return self.driver.find_element(By.XPATH, self.verify_login_credentials_xpath).text

    def click_forgot(self):
        self.driver.find_element(By.LINK_TEXT, self.forgot_button_link_text).click()

    def verify_forgot_password(self):
        return self.driver.find_element(By.XPATH, self.verify_forgot_password_xpath).text

    def forgot_email_address(self,forgot_email_password_addrees):
        self.driver.find_element(By.ID, self.enter_forgot_password_emai_id).click()
        self.driver.find_element(By.ID, self.enter_forgot_password_emai_id).clear()
        self.driver.find_element(By.ID, self.enter_forgot_password_emai_id).send_keys(forgot_email_password_addrees)

    def verify_forgot_enter_email(self):
        return self.driver.find_element(By.ID, self.forgot_entered_email_id).text

    def verify_reset_button(self):
        return self.driver.find_element(By.XPATH, self.verify_reset_password_button_xpath)

    def verify_otp_message(self):
        return self.driver.find_element(By.XPATH, self.verify_otp_message_xpath).text

    def login_back_button(self):
        self.driver.find_element(By.XPATH, self.login_back_xpath).click()
    def verify_login_back(self):
        return self.driver.find_element(By.XPATH, self.verify_login_back_xpath).text


