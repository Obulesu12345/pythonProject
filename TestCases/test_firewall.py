import time
import pytest
from Pages.loginpage import LoginPage
from Pages.instance import InstancePage
from Pages.Firewallpage import FirewallPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestFirewall:
    def test_verify_firewall_policy_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_page()
        message = "Firewall"
        assert firewall.verify_firewall_page().__eq__(message)
        time.sleep(3)

    def test_firewall_policy_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        self.driver.quit()

    def test_firewall_policy_overview_tabel_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.overview_button()
        time.sleep(3)
        firewall.firewall_policy_button()
        time.sleep(3)
        firewall.firewall_policy_table_data()
        time.sleep(3)

    def test_firewall_policy_overview_activity_tabel_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.overview_button()
        time.sleep(3)
        firewall.overview_activity_table_data()
        time.sleep(3)
        firewall.firewall_policy_overview_activity_table_data()
        time.sleep(3)
        self.driver.quit()


    def test_firewall_incoming_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.incoming_button()
        time.sleep(3)

    def test_firewall_incoming_wan_tabel_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.incoming_button()
        time.sleep(3)
        firewall.incoming_wan_button()
        time.sleep(3)
        firewall.firewall_incoming_wan_table_data()
        time.sleep(3)
        self.driver.quit()

    def test_firewall_incoming_captive_tabel_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.incoming_button()
        time.sleep(3)
        firewall.incoming_captive_button()
        time.sleep(3)
        firewall.firewall_incoming_captive_table_row_data()
        time.sleep(3)
        firewall.firewall_incoming_captive_table_data()
        self.driver.quit()

    def test_firewall_outgoing_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.outgoing_button()

    def test_firewall_outgoing_wan_table_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.outgoing_button()
        time.sleep(3)
        firewall.outgoing_wan_button()
        time.sleep(3)
        firewall.firewall_outgoing_wan_table_data()
        self.driver.quit()

    def test_firewall_outgoing_captive_table_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.outgoing_button()
        time.sleep(3)
        firewall.outgoing_captive_button()
        time.sleep(3)
        firewall.firewall_outgoing_captive_table_data()
        self.driver.quit()

    def test_firewall_outgoing_lan_others_table_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.outgoing_button()
        time.sleep(3)
        firewall.outgoing_lan_others_button()
        time.sleep(3)
        firewall.firewall_outgoing_lan_others_table_data()
        self.driver.quit()

    def test_incoming_page_total_instance(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        firewall = FirewallPage(self.driver)
        time.sleep(3)
        firewall.manage_firewall_page()
        time.sleep(3)
        firewall.incoming_button()
        time.sleep(3)
        firewall.dropdown_arrow_button()
        time.sleep(3)
        firewall.all_button()







