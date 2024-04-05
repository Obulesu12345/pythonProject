import time
import pytest
from Pages.loginpage import LoginPage
from Pages.instance import InstancePage
from Pages.ZoomViewPage import ZoomViewPage

@pytest.mark.usefixtures("setup_and_teardown")
class TestZoomView:
    def test_login_page_with_credentials(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        self.driver.quit()
    def test_manage_zoomview_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
    def test_verify_manage_zoomview_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        message = "Services"
        assert zoomview.verify_zoomview_page().__eq__(message)
        self.driver.quit()

    def test_zoomview_service_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.zoomview_service_button()
        time.sleep(4)
        zoomview.service_instance()
        time.sleep(4)
        zoomview.instance_data()
        time.sleep(5)
        zoomview.hostname_button()
        time.sleep(5)
        zoomview.hostname_data()
        # time.sleep(4)
        self.driver.quit()

    def test_service_table(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.service_button()
        time.sleep(5)
        # zoomview.row_per_page_button()
        # time.sleep(5)
        zoomview.rows_drop_down_button()
        time.sleep(5)
        zoomview.rows_drop_down()
        time.sleep(4)
        zoomview.service_table_data()
        time.sleep(2)
        self.driver.quit()

    def test_service_total_instance_count(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.service_button()
        time.sleep(5)
        zoomview.zoomview_service_button()
        time.sleep(4)
        zoomview.total_intsances()

    def test_pause_alerts_table(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.pause_alerts()
        time.sleep(3)
        zoomview.pause_alerts_table_data()
        time.sleep(3)

    def test_zoomview_service_check_instance_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.zoomview_service_button()
        time.sleep(4)
        message = "Select Instance"
        assert zoomview.verify_instance_panel().__eq__(message)
        time.sleep(4)

    def test_graph_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.select_graph()
        time.sleep(3)
        message = "15 mins data"
        assert zoomview.verify_graph_page().__eq__(message)

    def test_graph_one_instance(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.select_graph()
        time.sleep(3)
        zoomview.graph_instance_button()
        time.sleep(3)
        zoomview.graph_select_instance_check_box()
        time.sleep(3)
        zoomview.graph_service_button()
        time.sleep(3)
        zoomview.graph_service_dropdown_list()
        time.sleep(3)
        zoomview.intervel_dropdown()
        time.sleep(3)
        zoomview.graph_dropdown_listitems()
        time.sleep(3)
        zoomview.graph_submit_button()
        time.sleep(5)
        zoomview.verify_graph_instance()
        self.driver.quit()


    def test_graph_all_instance(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("zebu@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.select_graph()
        time.sleep(3)
        zoomview.graph_instance_button()
        time.sleep(3)
        zoomview.graph_select_all_instance_check_box()
        time.sleep(3)
        zoomview.graph_service_button()
        time.sleep(3)
        zoomview.graph_service_dropdown_list()
        time.sleep(3)
        zoomview.intervel_dropdown()
        time.sleep(3)
        zoomview.graph_dropdown_listitems()
        time.sleep(3)
        zoomview.graph_submit_button()
        time.sleep(10)
        zoomview.zoomview_graph_instances()
        time.sleep(10)
        zoomview.zoomview_instances_graph()
        self.driver.quit()

    def test_internet_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        message = "Internet Activities"
        assert zoomview.verify_internet_activities_page().__eq__(message)
        self.driver.quit()

    def test_internet_total_instances(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.internet_instance_button()
        time.sleep(3)
        zoomview.total_instances()
        time.sleep(4)


    def test_internet_instance_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.internet_instance_button()
        time.sleep(3)
        zoomview.select_instances()
        time.sleep(3)
        zoomview.internet_interval_dropdown()
        time.sleep(5)
        zoomview.internet_dropdown_list()
        time.sleep(4)
        zoomview.internet_instance_submit()
        time.sleep(3)
        zoomview.internet_hostname_data()
        time.sleep(3)
        zoomview.internet_hostname_arrow()
        time.sleep(3)
        zoomview.internet_instance_hostname()
        time.sleep(3)

    def test_internet_activities_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.internet_activities_page()
        time.sleep(4)
        zoomview.internet_activities_table()
        time.sleep(4)
        self.driver.quit()

    def test_internet_external_communication_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.internet_activities_page()
        time.sleep(4)
        zoomview.external_communication()
        time.sleep(3)
        zoomview.external_communication_table()
        time.sleep(3)
        zoomview.external_communication_table_data()
        time.sleep(3)

    def test_apps_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.internet_activities_page()
        time.sleep(4)
        zoomview.apps()
        time.sleep(3)
        zoomview.apps_table()
        time.sleep(3)
        zoomview.apps_table_data()
        time.sleep(3)
        self.driver.quit()

    def test_city_wise_traffic_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.internet_activities_page()
        time.sleep(4)
        zoomview.city_wise_traffic()
        time.sleep(3)
        zoomview.city_wise_traffic_table()
        time.sleep(4)
        zoomview.city_wise_traffic_table_data()
        time.sleep(3)

    def test_ISP_contributor_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.internet_activities_page()
        time.sleep(4)
        zoomview.ISP_contributor()
        time.sleep(3)
        zoomview.ISP_contributor_table()
        time.sleep(3)
        zoomview.ISP_contributor_table_data()
        time.sleep(3)

    def test_session_flow_page(self):
        login_page = LoginPage(self.driver)
        login_page.email_address("abdul@gmail.com")
        login_page.email_address_password("Tulasi@1234")
        login_page.click_login()
        time.sleep(5)
        zoomview = ZoomViewPage(self.driver)
        time.sleep(3)
        zoomview.manage_zoomview_page()
        time.sleep(4)
        zoomview.internet_button()
        time.sleep(4)
        zoomview.session_flow()
        time.sleep(3)
        zoomview.session_flow__table()
        time.sleep(3)
        zoomview.session_flow_table_data()
        self.driver.quit()

