import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class LoginPage:

    def __init__(self,driver):
        self.driver = driver

    verify_login_page_xpath = "//h3[text()='Cloud Operating Console']"
    email_text_xpath = "//input[@id='login-email']"
    email_password_text_xpath = "//input[@id='login-password']"
    click_login_button_xpath = "//button[text()='Login']"
    verify_message_home_link_text = "Home"
    verify_login_page_message_xpath = "//div[text()='Enter your Login credentials']"
    verify_wrong_credentials_message_xpath = "//*[text()='Email ID or Password is wrong']"

    verify_message_for_wrong_mail_xpath = "//ul[@class='MuiBox-root css-dbde']/li[1]"
    verify_message_for_valid_password_xpath = "//ul[@class='MuiBox-root css-70qvj9']/li[1]"
    verify_enter_your_login_credentials_message_xpath = "//div[@class='MuiBox-root css-12re8tr']"
    forgot_button_xpath  = "//a[@href='/forgot_password']"
    verify_forgot_password_message_xpath = "//div[@class='MuiBox-root css-8atqhb']/h3[1]"
    forgot_password_email_text_xpath = "//input[contains(@id,'forgot-password-email')]"
    verify_forgot_password_for_wrong_email_xpath = "//ul[@class='MuiBox-root css-dbde']/li[1]"
    verify_reset_password_button_xpath = "//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//preceding::button"
    verify_password_reset_message_xpath = "//div[@class='MuiBox-root css-8atqhb']/h3"
    login_back_button_xpath = "//button[contains(@type,'button')]//child::span[1]"
    verify_login_back__page_message_xpath = "//h3[@class='MuiTypography-root MuiTypography-h3 css-b309xq']"
    verify_incorrect_url_page_xpath = "//*[text()='404']"

    logout_button_xpath = "//*[contains(@data-testid,'KeyboardArrowDownIcon')]"
    verify_logout_username_xpath = "//div[text()='Profile']"
    logout_xpath = "//span[text()='Logout']"
    verify_logout_xpath = "//h3[text()='Welcome Back!']"

    reset_password_button_xpath = "//button[contains(@type,'button')]/span[@class='MuiTouchRipple-root css-w0pj6f']//preceding::button"

    enter_otp1_xpath = "//input[contains(@aria-label,'Please enter verification code. Digit 1')]"
    enter_otp2_xpath = "//input[contains(@aria-label,'Digit 2')]"
    enter_otp3_xpath = "//input[contains(@aria-label,'Digit 3')]"
    enter_otp4_xpath = "//input[contains(@aria-label,'Digit 4')]"
    enter_otp5_xpath = "//input[contains(@aria-label,'Digit 5')]"
    enter_otp6_xpath = "//input[contains(@aria-label,'Digit 6')]"
    verify_enter_otp_xpath = "//div[@class='MuiBox-root css-8atqhb']/p"
    enter_otp_submit_xpath = "//button[text()='Continue']"

    forgot_new_password_xpath = "//input[@name='newPassword']"
    forgot_confirm_password_xpath = "//input[@name='confirmPassword']"
    forgot_set_password_button_xpath = "//button[text()='Set Password']"

    verify_after_log_in_page_message_xpath = "(//*[text()='Instances'])[2]"

    def current_url(self):
        current_url = self.driver.current_url
        print("url:-", current_url)

    # def screen_shots(self,):
    #     folder_path = "screenshots"
    #     screenshot_path = os.path.join(folder_path, "login_forgot_password_otp.png")
    #     self.driver.save_screenshot.os.path.join("screenshots", "login_forgot_password_otp.png")
    #     self.driver.quit()

    def verify_log_in_page_instance_message_xpath(self):
        # try:
        return self.driver.find_element(By.XPATH, self.verify_after_log_in_page_message_xpath).text
        # return element
            # interact with the element
        # except NoSuchElementException:
        #     print("Element not found")
        # return self.driver.find_element(By.XPATH, self.verify_after_log_in_page_message_xpath).text

    def check_verify_log_in_page_instance_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_after_log_in_page_message_xpath).text
        if data == "Instances":
            print("successfully displayed message is Instances")
        else:
            print("not displayed")


    # def verify_current_url(self):
    #     driver = webdriver.Chrome()
    #     driver.get("https://dev.zybisys.com/loginewkjef")
    #     driver.maximize_window()
    #     current_url = driver.current_url
    #     print(current_url)

    def forgot_new_password(self,new_password):
        try:
            element = self.driver.find_element(By.XPATH, self.forgot_new_password_xpath)
            element.clear()
            element.click()
            element.send_keys(new_password)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.forgot_new_password_xpath).click()
        # self.driver.find_element(By.XPATH, self.forgot_new_password_xpath).clear()
        # self.driver.find_element(By.XPATH, self.forgot_new_password_xpath).send_keys(new_password)

    def forgot_confirm_password(self,confirm_password):
        try:
            element = self.driver.find_element(By.XPATH, self.forgot_confirm_password_xpath)
            element.clear()
            element.click()
            element.send_keys(confirm_password)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.forgot_confirm_password_xpath).click()
        # self.driver.find_element(By.XPATH, self.forgot_confirm_password_xpath).clear()
        # self.driver.find_element(By.XPATH, self.forgot_confirm_password_xpath).send_keys(confirm_password)

    def forgot_set_password_button(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.forgot_set_password_button_xpath)))

        # Interact with the element
        #     element.click()
        except TimeoutException as e:
            print("TimeoutException occurred:", e)

        # self.driver.find_element(By.XPATH, self.forgot_set_password_button_xpath).click()

    def verify_enter_otp(self):
        try:
            element = self.driver.find_element(By.XPATH, self.verify_enter_otp_xpath).text
            return element
        except NoSuchElementException:
            print("Element not found")


    def check_verify_enter_otp(self):
        data = self.driver.find_element(By.XPATH, self.verify_enter_otp_xpath).text
        if data == "We have sent an OTP to ab******om. Please check your inbox/spam folder and enter the OTP to proceed":
            print("Successfully displayed message is We have sent an OTP to ab******om. Please check your inbox/spam folder and enter the OTP to proceed")
        else:
            print("Not displayed")


    def submit(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.enter_otp_submit_xpath)))

        # Interact with the element
            element.click()
        except TimeoutException as e:
            print("TimeoutException occurred:", e)

        # self.driver.find_element(By.XPATH, self.enter_otp_submit_xpath).click()

    def reset_password_button(self):
        self.driver.find_element(By.XPATH, self.reset_password_button_xpath).click()


    def login_otp1(self,text_otp1):
        try:
            element = self.driver.find_element(By.XPATH, self.enter_otp1_xpath)
            element.clear()
            element.click()
            element.send_keys(text_otp1)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.enter_otp1_xpath).click()
        # self.driver.find_element(By.XPATH, self.enter_otp1_xpath).clear()
        # self.driver.find_element(By.XPATH, self.enter_otp1_xpath).send_keys(text_otp1)

    def login_otp2(self,text_otp2):
        try:
            element = self.driver.find_element(By.XPATH, self.enter_otp2_xpath)
            element.clear()
            element.click()
            element.send_keys(text_otp2)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.enter_otp2_xpath).click()
        # self.driver.find_element(By.XPATH, self.enter_otp2_xpath).clear()
        # self.driver.find_element(By.XPATH, self.enter_otp2_xpath).send_keys(text_otp2)

    def login_otp3(self,text_otp3):
        try:
            element = self.driver.find_element(By.XPATH, self.enter_otp3_xpath)
            element.clear()
            element.click()
            element.send_keys(text_otp3)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.enter_otp3_xpath).click()
        # self.driver.find_element(By.XPATH, self.enter_otp3_xpath).clear()
        # self.driver.find_element(By.XPATH, self.enter_otp3_xpath).send_keys(text_otp3)

    def login_otp4(self,text_otp4):
        try:
            element = self.driver.find_element(By.XPATH, self.enter_otp4_xpath)
            element.clear()
            element.click()
            element.send_keys(text_otp4)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.enter_otp4_xpath).click()
        # self.driver.find_element(By.XPATH, self.enter_otp4_xpath).clear()
        # self.driver.find_element(By.XPATH, self.enter_otp4_xpath).send_keys(text_otp4)

    def login_otp5(self,text_otp5):
        try:
            element = self.driver.find_element(By.XPATH, self.enter_otp5_xpath)
            element.clear()
            element.click()
            element.send_keys(text_otp5)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.enter_otp5_xpath).click()
        # self.driver.find_element(By.XPATH, self.enter_otp5_xpath).clear()
        # self.driver.find_element(By.XPATH, self.enter_otp5_xpath).send_keys(text_otp5)

    def login_otp6(self,text_otp6):
        try:
            element = self.driver.find_element(By.XPATH, self.enter_otp6_xpath)
            element.clear()
            element.click()
            element.send_keys(text_otp6)
        except NoSuchElementException as e:
            print("Element not found:", e)

        # self.driver.find_element(By.XPATH, self.enter_otp6_xpath).click()
        # self.driver.find_element(By.XPATH, self.enter_otp6_xpath).clear()
        # self.driver.find_element(By.XPATH, self.enter_otp6_xpath).send_keys(text_otp6)


    def logout_button(self):
        try:
            element = self.driver.find_element(By.XPATH, self.logout_button_xpath)
            element.click()
        except NoSuchElementException:
            print("Element not found")

    def verify_logout_username(self):
        try:
            element = self.driver.find_element(By.XPATH, self.verify_logout_username_xpath).text
            return element
        except NoSuchElementException:
            print("Element not found")

    def logout(self):
        try:
            element = self.driver.find_element(By.XPATH, self.logout_xpath)
            element.click()
        except NoSuchElementException:
            print("Element not found")

    def verify_logout(self):
        return self.driver.find_element(By.XPATH, self.verify_logout_xpath).text


    def verify_incorrect_url_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_incorrect_url_page_xpath).text
        return data
        # if data == "404":
        #     print("successfully login with wrong url")
        # else:
        #     print("not succesfully login")

    def check_incorrect_url_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_incorrect_url_page_xpath).text
        if data == "404":
            print("successfully displayed message is 404")
        else:
            print("not displayed")

    def verify_login_page(self):
        # return self.driver.find_element(By.XPATH, self.verify_login_page_xpath).text
        data = self.driver.find_element(By.XPATH, self.verify_login_page_xpath).text
        return data
        # if data == "Cloud Operating Console":
        #     print("successfully login")
        # else:
        #     print("not succesfully login")
    def check_verify_login_page(self):
        # return self.driver.find_element(By.XPATH, self.verify_login_page_xpath).text
        data = self.driver.find_element(By.XPATH, self.verify_login_page_xpath).text
        # return data
        if data == "Cloud Operating Console":
            print("login page is opened successfully ")
            # print("successfully displayed message is Cloud Operating Console")
        else:
            print("login page is not opened, its opening another page")


    def email_address(self,email_addrees_text):
        self.driver.find_element(By.XPATH, self.email_text_xpath).clear()
        self.driver.find_element(By.XPATH, self.email_text_xpath).click()
        self.driver.find_element(By.XPATH, self.email_text_xpath).send_keys(email_addrees_text)

    def email_address_password(self,email_password_address):
        try:
            element = self.driver.find_element(By.XPATH, self.email_password_text_xpath)
            element.clear()
            element.click()
            element.send_keys(email_password_address)
            # self.driver.find_element(By.XPATH, self.email_password_text_xpath).click()
            # self.driver.find_element(By.XPATH, self.email_password_text_xpath).send_keys(email_password_address)
        except ElementNotInteractableException as e:
            # Handle the exception
            print("Element is not interactable:", e)
        # try:
        #     # Perform some action that may raise ElementNotInteractableException
        #     element = driver.find_element_by_id('some_element_id')
        #     element.click()  # For example, trying to click on the element
        # except ElementNotInteractableException as e:
        #     # Handle the exception
        #     print("Element is not interactable:", e)
        #     # Additional code to handle the exception, such as scrolling, waiting, or trying a different approach
        # finally:
        #     Close the WebDriver
            # driver.quit()

    def click_login(self):
        try:
            # Wait for the element to be clickable
            element = self.driver.find_element(By.XPATH, self.click_login_button_xpath)

            # Interact with the element
            element.click()
        except ElementNotInteractableException as e:
            print("Element is not interactable:", e)


        # try:
        #     element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.click_login_button_xpath)))
        #
        #     # Interact with the element
        #     element.click()
        # except TimeoutException as e:
        #     print("TimeoutException occurred:", e)


        # try:
        # #     # Use WebDriverWait to wait for element presence
        #     element = WebDriverWait(self.driver, 10).until(EC.ele((By.XPATH, self.click_login_button_xpath)))
        #     # element.click()
        # except ElementNotInteractableException as e:
        #     print("Element is not interactable:", e)

        # retry_count = 3
        # while retry_count > 0:
        #     try:
        #         # Wait for the element to be clickable
        #         element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, self.click_login_button_xpath)))
        #
        #         # Interact with the element
        #         element.click()
        #     except StaleElementReferenceException:
        #         print("Stale element reference. Retrying...")
        #         retry_count -= 1

        # self.driver.find_element(By.XPATH, self.click_login_button_xpath).click()

    def Home_page(self):
        try:
            data = self.driver.find_element(By.LINK_TEXT, self.verify_message_home_link_text).text
            return data
        except NoSuchElementException:
            print("Element not found")

    def check_home_page_page(self):
        data = self.driver.find_element(By.XPATH, self.verify_after_log_in_page_message_xpath).text
        if data == "Instances":
            print("Dashboard page is opened successfully")
            # print("successfully login with Instances page")
        else:
            print("Dashboard page is not opened ")

    def verify_message_wrong_credentials(self):
        try:
            data = self.driver.find_element(By.XPATH, self.verify_wrong_credentials_message_xpath).text
            return data
        except NoSuchElementException:
            print("Element not found")
    def check_wrong_credentials_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_wrong_credentials_message_xpath).text
        if data == "Email ID or Password is wrong":
            print("Successfully displayed message is Email ID or Password is wrong")
        else:
            print("Not displayed, please enter a valid email and password")

    def verify_message_wrong_mail(self):
        return self.driver.find_element(By.XPATH, self.verify_message_for_wrong_mail_xpath).text

    def check_wrong_mail_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_message_for_wrong_mail_xpath).text
        if data == "Please enter a valid email":
            print("Successfully Displayed message is Please enter a valid email")
        else:
            print("Not displayed, please enter a valid email")

    def verify_message_wrong_password(self):
        return self.driver.find_element(By.XPATH, self.verify_message_for_valid_password_xpath).text

    def check_wrong_password_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_message_for_valid_password_xpath).text
        if data == "Please enter valid password:":
            print("Successfully displayed message is Please enter valid password")
        else:
            print("Not displayed, please enter a valid password")


    def verify_empty_credentials_message(self):
        return self.driver.find_element(By.XPATH, self.verify_enter_your_login_credentials_message_xpath).text

    def check_empty_credentials_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_enter_your_login_credentials_message_xpath).text
        if data == "Enter your Login credentials":
            print("We are entering username and password is empty credentials")
            # print("Successfully displayed message is Enter your Login credentials")
        else:
            print("Please Enter your Login credentials")

    def click_forgot(self):
        try:
            element = self.driver.find_element(By.XPATH, self.forgot_button_xpath)

        # Interact with the element
            element.click()
        except ElementNotInteractableException as e:
            print("Element is not interactable:", e)
        # self.driver.find_element(By.XPATH, self.forgot_button_xpath).click()

    def verify_forgot_password(self):
        return self.driver.find_element(By.XPATH, self.verify_forgot_password_message_xpath).text

    def check_forgot_password_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_forgot_password_message_xpath).text
        if data == "Forgot Password?":
            print("successfully displayed message is Forgot Password?")
        else:
            print("not displayed")

    def forgot_email_address(self,forgot_email_password_addrees):
        try:
            element = self.driver.find_element(By.XPATH, self.forgot_password_email_text_xpath)
            element.clear()
            element.click()
            element.send_keys(forgot_email_password_addrees)
        except NoSuchElementException as e:
            print("Element not found:", e)
            # self.driver.find_element(By.XPATH, self.email_password_text_xpath).click()
            # self.driver.find_element(By.XPATH, self.email_password_text_xpath).send_keys(email_password_address)
        # except ElementNotInteractableException as e:
        #     # Handle the exception
        #     print("Element is not interactable:", e)

        # self.driver.find_element(By.ID, self.forgot_password_email_text_id).click()
        # self.driver.find_element(By.ID, self.forgot_password_email_text_id).clear()
        # self.driver.find_element(By.ID, self.forgot_password_email_text_id).send_keys(forgot_email_password_addrees)

    def verify_forgot_enter_email(self):
        return self.driver.find_element(By.ID, self.verify_forgot_password_for_wrong_email_xpath).text

    def check_forgot_password_wrong_email_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_forgot_password_for_wrong_email_xpath).text
        if data == "Please enter a valid email":
            print("successfully displayed message is Please enter a valid email")
        else:
            print("not displayed")
    def reset_button(self):

        try:
            element = self.driver.find_element(By.XPATH, self.verify_reset_password_button_xpath)
            element.click()
        except ElementNotInteractableException as e:
            print("Element is not interactable:", e)



    def verify_reset_button(self):
        return self.driver.find_element(By.XPATH, self.verify_reset_password_button_xpath)

    def verify_password_reset_message(self):
        return self.driver.find_element(By.XPATH, self.verify_password_reset_message_xpath).text

    def check_verify_password_reset_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_password_reset_message_xpath).text
        if data == "Password Reset":
            print("Successfully displayed message is Password Reset")
        else:
            print("not displayed")

    def login_back_button(self):
        try:
            element = self.driver.find_element(By.XPATH, self.login_back_button_xpath)
            element.click()
        except ElementNotInteractableException as e:
            print("Element is not interactable:", e)
    def verify_login_back_page_message(self):
        return self.driver.find_element(By.XPATH, self.verify_login_back__page_message_xpath).text

    def check_verify_login_back_message(self):
        data = self.driver.find_element(By.XPATH, self.verify_login_back__page_message_xpath).text
        if data == "Welcome Back!":
            print("successfully displayed message is Welcome Back!")
        else:
            print("not displayed")





















