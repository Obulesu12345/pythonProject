import time
import pytest
from pages.login_page import LoginPage
from pages.instance import InstancePage
from pages.billing_payment_history import PaymentHistory


@pytest.mark.usefixtures("setup_and_teardown")
class TestPayment_history:
    def test_verify_billing_payment_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        payment = PaymentHistory(self.driver)
        payment.billing_button()
        time.sleep(1)
        message = "Payment History"
        assert payment.verify_billing_payment_history_page().__eq__(message)
        payment.current_url()
        self.driver.save_screenshot("billing_payment.png")
        self.driver.quit()

    def test_payment_history_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        payment = PaymentHistory(self.driver)
        payment.billing_payment_page()
        time.sleep(1)
        message = "Payment History"
        assert payment.verify_payment_history_page().__eq__(message)
        payment.current_url()
        self.driver.save_screenshot("billing_payment_history_page.png")
        self.driver.quit()

    def test_payment_history_page_table(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        payment = PaymentHistory(self.driver)
        payment.billing_payment_page()
        time.sleep(1)
        payment.table_dropdown_arrow_button()
        time.sleep(1)
        payment.dropdown_listitems()
        time.sleep(1)
        payment.table_data()
        time.sleep(1)
        payment.right_arrow_button()
        time.sleep(1)
        payment.table_data()
        self.driver.save_screenshot("billing_payment_history_table.png")
        self.driver.quit()

    def test_verify_billing_invoices_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        self.driver.implicitly_wait(10)
        payment = PaymentHistory(self.driver)
        payment.billing_button()
        time.sleep(1)
        payment.invoices_button()
        time.sleep(1)
        message = "Total Balance | ₹0"
        assert payment.verify_billing_invoices_text().__eq__(message)
        time.sleep(10)
        # payment.invoice_table_data()
        payment.table_invoice_data()
        self.driver.implicitly_wait(10)
        payment.total_balance_check_box()
        time.sleep(1)
        payment.total_balance()
        time.sleep(1)
        self.driver.save_screenshot("billing_billing_invoices_page.png")
        self.driver.quit()
