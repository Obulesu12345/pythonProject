import time
import pytest
from Pages.loginpage import LoginPage
from Pages.instance import InstancePage
from Pages.billing_payment_history import PaymentHistory


@pytest.mark.usefixtures("setup_and_teardown")
class TestPayment_history:
    def test_verify_billing_payment_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        payment = PaymentHistory(self.driver)
        time.sleep(3)
        payment.billing_button()
        time.sleep(3)
        message = "Payment History"
        assert payment.verify_billing_payment_history_page().__eq__(message)
        self.driver.quit()

    def test_payment_history_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        payment = PaymentHistory(self.driver)
        time.sleep(3)
        payment.billing_payment_page()
        time.sleep(3)
        message = "Payment History"
        assert payment.verify_payment_history_page().__eq__(message)

    def test_payment_history_page_table(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        payment = PaymentHistory(self.driver)
        time.sleep(3)
        payment.billing_payment_page()
        time.sleep(5)
        payment.table_dropdown_arrow_button()
        time.sleep(5)
        payment.dropdown_listitems()
        time.sleep(5)
        payment.payment_history_table_data()
        time.sleep(5)
        payment.right_arrow_button()
        time.sleep(2)
        payment.payment_history_table_data()

    def test_verify_billing_invoices_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        payment = PaymentHistory(self.driver)
        time.sleep(3)
        payment.billing_button()
        time.sleep(3)
        payment.invoices_button()
        time.sleep(3)
        payment.invoice_table_data()
        time.sleep(3)
        payment.total_balance_check_box()
        time.sleep(3)
        payment.total_balance()
        time.sleep(3)
