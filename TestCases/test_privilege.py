import os
import time
import pytest
from pages.login_page import LoginPage
from pages.privilege import privilegePage

@pytest.mark.usefixtures("setup_and_teardown")
class TestPrivilege:
    def test_privilege_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page_button()
        time.sleep(2)
        message = "Users"
        assert privilage.hover_user_page().__eq__(message)
        privilage.check_verify_privilege_page_users_message()
        privilage.current_url()
        self.driver.save_screenshot("privilege_verify_users_page.png")
        self.driver.quit()

    def test_privilege_page_dropdown(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        message = "ADD USER"
        assert privilage.veriry_users_page().__eq__(message)
        privilage.current_url()
        self.driver.save_screenshot("privilege_users_page.png")
        self.driver.quit()

    def test_add_user(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(1)
        privilage.add_user_button()
        time.sleep(2)
        privilage.add_user_data_name("obulesu")
        time.sleep(1)
        privilage.add_user_data_lastname("garladinne")
        time.sleep(1)
        privilage.add_user_data_email("obulesu9390@gmail.com")
        time.sleep(1)
        privilage.add_user_data_phone("8790345527")
        time.sleep(1)
        privilage.add_user_invite_button()
        time.sleep(1)
        message = "Phone already taken"
        assert privilage.alert_otp_msg().__eq__(message)
        privilage.check_verify_privilege_page_alert_otp_message()
        privilage.current_url()
        self.driver.save_screenshot("privilege_add_user.png")
        self.driver.quit()

    def test_users_table_data(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        privilage.users_total_rows()
        privilage.users_total_columns()
        privilage.privilege_table_data()
        time.sleep(1)
        self.driver.save_screenshot("privilege_table.png")
        self.driver.quit()

    def test_user_table_actions_for_instance(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        privilage.action_button_list_for_instance()
        time.sleep(2)
        # privilage.action_instance_button()
        # time.sleep(2)
        privilage.instance_check_box()
        time.sleep(2)
        privilage.assign_instance_button()
        time.sleep(2)
        message = "Assigned instances!"
        assert privilage.alert_otp_msg().__eq__(message)
        privilage.check_verify_instance_page_for_alert_otp_message()
        self.driver.save_screenshot("privilege_action_instance.png")
        self.driver.quit()


    def test_user_role_actions(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        privilage.action_button_list_for_role()
        time.sleep(2)
        privilage.assign_role_check_box()
        time.sleep(2)
        privilage.assign_role_button()
        time.sleep(2)
        message = "Assigned roles!"
        assert privilage.alert_otp_msg().__eq__(message)
        privilage.check_verify_role_page_for_alert_otp_message()
        time.sleep(3)
        self.driver.save_screenshot("privilege_action_role.png")
        self.driver.quit()

    def test_user_edit_actions(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        privilage.action_button_list_for_edit()
        time.sleep(1)
        message = "Fill required fields to edit user"
        assert privilage.verify_actions_edit_page().__eq__(message)
        privilage.edit_button()
        time.sleep(2)
        message1 = "Updated data of TulasiRam!"
        assert privilage.alert_otp_msg().__eq__(message1)
        privilage.check_verify_privilege_page_for_edit_page_otp_message()
        time.sleep(3)
        self.driver.save_screenshot("privilege_action_edit.png")
        self.driver.quit()

    def test_user_password_actions(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        privilage.action_button_list_for_password()
        time.sleep(2)
        message = "You can reset password for TulasiRam r"
        assert privilage.verify_password().__eq__(message)
        self.driver.save_screenshot("privilege_action_password.png")
        self.driver.quit()

    def test_user_log_actions(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(1)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        privilage.action_button_list_for_logs()
        time.sleep(2)
        privilage.privilege_logs_table_data()
        self.driver.save_screenshot("privilege_action_logs.png")
        self.driver.quit()


    def test_user_verify_email(self):
        login_page = privilegePage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        privilage = privilegePage(self.driver)
        privilage.location()
        time.sleep(2)
        privilage.location_dropdown()
        time.sleep(2)
        privilage.privilege_page()
        time.sleep(2)
        privilage.action_button_list_for_verify_email()
        time.sleep(2)
        message = "Sent email for verification!"
        assert privilage.alert_otp_msg().__eq__(message)
        privilage.check_verify_privilege_page_for_verify_page_otp_message()
        self.driver.save_screenshot("privilege_action_verify_email.png")
        time.sleep(2)
        self.driver.quit()




























# import os
# import time
# import pytest
# from Pages.loginpage import LoginPage
# from Pages.privilege import privilegePage
#
# @pytest.mark.usefixtures("setup_and_teardown")
# class TestPrivilege:
#     def test_login_page_with_credentials(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         self.driver.quit()
#
#     def test_privilege_page(self):
#         login_page = LoginPage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(5)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(3)
#         privilage.privilege_page_button()
#         time.sleep(2)
#         message = "Users"
#         assert privilage.hover_user_page().__eq__(message)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "privilege_verify_users_page.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#     def test_privilege_page_dropdown(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(3)
#         privilage.privilege_page()
#         time.sleep(3)
#         message = "ADD USER"
#         assert privilage.veriry_users_page().__eq__(message)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "privilege_users_page.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#     def test_add_user(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(3)
#         privilage.privilege_page()
#         time.sleep(1)
#         privilage.add_user_button()
#         time.sleep(2)
#         privilage.add_user_data_name("obulesu")
#         time.sleep(1)
#         privilage.add_user_data_lastname("garladinne")
#         time.sleep(1)
#         privilage.add_user_data_email("obulesu9390@gmail.com")
#         time.sleep(1)
#         privilage.add_user_data_phone("8790345527")
#         time.sleep(1)
#         privilage.add_user_invite_button()
#         time.sleep(1)
#         message = "Phone already taken"
#         assert privilage.alert_otp_msg().__eq__(message)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "privilege_add_user.png")
#         self.driver.save_screenshot(screenshot_path)
#         self.driver.quit()
#
#     def test_users_table_data(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(5)
#         privilage.privilege_page()
#         time.sleep(3)
#         privilage.users_total_rows()
#         time.sleep(3)
#         privilage.users_total_columns()
#         time.sleep(3)
#         privilage.table_data()
#         time.sleep(3)
#         self.driver.quit()
#
#     def test_user_actions(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(5)
#         privilage.privilege_page()
#         time.sleep(3)
#         privilage.action_button()
#         time.sleep(3)
#         privilage.action_instance_button()
#         time.sleep(3)
#         privilage.instance_check_box()
#         time.sleep(3)
#         privilage.assign_instance_button()
#         time.sleep(4)
#         self.driver.quit()
#
#
#     def test_user_role_actions(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(5)
#         privilage.privilege_page()
#         time.sleep(3)
#         privilage.action_button()
#         time.sleep(3)
#         privilage.action_role()
#         time.sleep(3)
#         privilage.assign_role_check_box()
#         time.sleep(3)
#         privilage.assign_role_button()
#         time.sleep(3)
#         self.driver.quit()
#
#     def test_user_edit_actions(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(5)
#         privilage.privilege_page()
#         time.sleep(3)
#         privilage.action_button()
#         time.sleep(3)
#         privilage.actions_edit()
#         time.sleep(3)
#         message = "Fill required fields to edit user"
#         assert privilage.verify_actions_edit_page().__eq__(message)
#         time.sleep(3)
#         self.driver.quit()
#
#     def test_user_password_actions(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(5)
#         privilage.privilege_page()
#         time.sleep(3)
#         privilage.action_button()
#         time.sleep(3)
#         privilage.actions_password()
#         time.sleep(3)
#         message = "You can reset password for"
#         privilage.verify_password().__eq__(message)
#         time.sleep(3)
#         self.driver.quit()
#
#     def test_user_log_actions(self):
#         login_page = privilegePage(self.driver)
#         login_page.email_address("abdul@gmail.com")
#         login_page.email_address_password("Tulasi@1234")
#         login_page.click_login()
#         time.sleep(3)
#         privilage = privilegePage(self.driver)
#         privilage.location()
#         time.sleep(3)
#         privilage.location_dropdown()
#         time.sleep(5)
#         privilage.privilege_page()
#         time.sleep(3)
#         privilage.action_button()
#         time.sleep(3)
#         privilage.actions_log()
#         time.sleep(3)
#         privilage.users_action_table_total_rows()
#         time.sleep(3)
#         privilage.users_action_table_total_columns()
#         time.sleep(3)
#         privilage.actions_table_data()
#         self.driver.quit()
#
#
#
