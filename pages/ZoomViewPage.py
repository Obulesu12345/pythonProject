import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ZoomViewPage:

    def __init__(self,driver):
        self.driver = driver

    manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
    manage_zoomview_button_xpath = "(//div[text()='Zoom View'])"
    verify_zoomview_page_xpath = "(//button[text()='Services'])[1]"

    zoomview_service_instance_xpath = "//button[text()='Instances']"
    # service_instance_xpath = "//div[@class='MuiBox-root css-1vmar9t']/div"
    service_instance_xpath = "(//div[@class='MuiBox-root css-1vmar9t']/div)[6]"
    select_instance_button_xpath = "//button[text()='Submit']"
    hostname_button_xpath = "//*[contains(@data-testid,'ExpandMoreIcon')]"
    hostname_data_xpath = "(//div[@class='MuiBox-root css-1555w3t']/div)[2]"
    instance_data_xpath = "(//div[@class='MuiBox-root css-1555w3t']/div)[1]"

    service_button_xpath = "(//button[text()='Services'])[2]"
    rows_button_xpath = "(//div[contains(@role,'button')])[2]"
    rows_dropdown_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li"

    pause_alerts_xpath= "//button[text()='Pause Alerts']"

    graphs_xpath = "//button[text()='Graphs']"
    verify_graph_page_xpath = "//p[text()='15 mins data']"
    graphs_instance_button_xpath = "//button[text()='Instances']"

    select_instance_check_box_xpath = "(//input[contains(@type,'checkbox')])[4]"
    graph_interval_dropdown_xpath = "(//div[contains(@role,'button')])[3]"
    graph_check_interval_xpath = "(//div[contains(@role,'button')])[2]"
    dropdown_listitems_xpath = "(//ul[contains(@role,'listbox')])//li"
    submit_button_xpath = "//button[text()='Submit']"
    graph_service_button_xpath = "//div[@id='demo-select-small']"
    service_dropdown_list_xpath = "//ul[contains(@role,'listbox')]//li"

    zoomview_instance_graph_xpath = "//div[contains(@id,'zoomview-graphs')]/div"
    instance_total_xpath = "//p[text()='Instances']/parent::div/descendant::div[6]"

    verify_graph_instance_page_xpath = "(//div[@class='MuiBox-root css-f0kha9'])[1]"

    select_all_graph_instance_xpath = "(//input[contains(@type,'checkbox')])[1]"


    internet_button_xpath = "//button[text()='Internet']"
    internet_instance_button_xpath = "//button[text()='Instances']"
    select_instances_xpath = "(//div[@class='MuiBox-root css-1vmar9t']/div)"
    internet_interval_dropdown_xpath = "(//*[contains(@role,'button')])[7]"
    check_internet_interval_dropdown_xpath = "(//*[contains(@data-testid,'ArrowDropDownIcon')])[7]"
    internet_interval_dropdown_list_xpath = "(//*[contains(@role,'listbox')])/li"
    internet_instance_submit_xpath = "//button[text()='Submit']"

    verify_internet_activities_page_xpath  ="//button[text()='Internet Activities']"



    internet_instance_hostname_xpath = "//div[@class='MuiBox-root css-9lsp3l']"
    internet_hostname_arrow_xpath = "//*[contains(@data-testid,'ExpandMoreIcon')]"
    internet_hostname_data_xpath = "(//div[@class='MuiBox-root css-0'])[2]"

    internet_activities_page_xpath = "//button[text()='Internet Activities']"
    internet_activities_table_xpath = "//div[@class='MuiBox-root css-1j2is0p']"

    external_communication_xpath = "(//div[@class='MuiBox-root css-69i1ev']/p)[1]"
    external_communication_table_xpath = "(//div[@class='MuiBox-root css-1fpff4c']/table)[1]"
    external_communication_table_data_xpath = "(//div[@class='MuiBox-root css-14w0bz'])[1]"

    apps_xpath = "(//div[@class='MuiBox-root css-69i1ev']/p)[2]"
    apps_table_xpath = "(//div[@class='MuiBox-root css-1fpff4c']/table)[2]"
    apps_table_data_xpath = "(//div[@class='MuiBox-root css-14w0bz'])[2]"

    city_wise_traffic_xpath = "(//div[@class='MuiBox-root css-69i1ev']/p)[3]"
    city_wise_traffic_table_xpath = "(//div[@class='MuiBox-root css-1fpff4c']/table)[3]"
    city_wise_traffic_table_data_xpath = "(//div[@class='MuiBox-root css-14w0bz'])[3]"

    ISP_contributor_xpath = "(//div[@class='MuiBox-root css-69i1ev']/p)[4]"
    ISP_contributor_table_xpath = "(//div[@class='MuiBox-root css-1fpff4c']/table)[4]"
    ISP_contributor_table_data_xpath = "(//div[@class='MuiBox-root css-14w0bz'])[3]"

    session_flow_xpath = "//button[text()='Session Flow']"
    session_flow_table_xpath = "//div[@class='MuiBox-root css-1h1hd2a']/table"
    session_flow_table_data_xpath = "//div[@class='MuiBox-root css-14w0bz']"

    total_intsances_xpath = "//div[@class='MuiBox-root css-1vmar9t']/div"

    verify_instance_panel_xpath = "//*[text()='Select Instance']"

    zoomview_instances_graphs_xpath = "(//div[contains(@id,'zoomview-graphs')]/div)"

    graph_instances_page_xpath = "(//div[@class='MuiBox-root css-f0kha9'])"

    internet_one_instance_xpath = "(//div[@class='MuiBox-root css-1vmar9t']/div)[4]"

    verify_manage_page_xpath = "(//div[text()='Zoom View'])"

    verify_interval_button_text_xpath = "//div[contains(@id,'zoom-view-internet-activity-interval')]"

    verify_internet_instance_text_xpath = "// p[text() = 'Select Instance']"

    def graph_check_interval(self):
        self.driver.find_element(By.XPATH, self.graph_check_interval_xpath).click()


    def verify_internet_instance_text(self):
        return self.driver.find_element(By.XPATH, self.verify_internet_instance_text_xpath).text
    def verify_interval_button_text(self):
        data = self.driver.find_element(By.XPATH, self.verify_interval_button_text_xpath).text
        print("select interval:", data)


    def dashboard_total_intances(self):
        total = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
        print("total instance:", total)

        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(1)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.manage_zoomview_button_xpath)))
        element.click()
        self.driver.find_element(By.XPATH, self.service_button_xpath).click()
        self.driver.find_element(By.XPATH, self.zoomview_service_instance_xpath).click()

        total_instance = self.driver.find_elements(By.XPATH, self.total_intsances_xpath)
        instance = len(total_instance)
        print("total service panals:", instance)


        if instance == total:
            print("matched")
        else:
            print("not matched")



    def manage_zoomview_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(1)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.manage_zoomview_button_xpath)))
        element.click()


    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def verify_manage_page(self):
        return self.driver.find_element(By.XPATH, self.verify_manage_page_xpath).text

    def verify_instance_panel(self):
        return self.driver.find_element(By.XPATH, self.verify_instance_panel_xpath).text

    def total_intsances(self):
        data = self.driver.find_elements(By.XPATH, self.total_intsances_xpath)
        print(len(data))
        # print(data)

    def verify_graph_page(self):
        return self.driver.find_element(By.XPATH, self.verify_graph_page_xpath).text

    def session_flow(self):
        self.driver.find_element(By.XPATH, self.session_flow_xpath).click()

    def session_flow__table(self):
        data = self.driver.find_element(By.XPATH, self.session_flow_table_xpath).text
        print(data)

    def session_flow_table_data(self):
        tabel_data = self.driver.find_element(By.XPATH, self.session_flow_table_data_xpath).text
        print(tabel_data)


    def ISP_contributor(self):
        data = self.driver.find_element(By.XPATH, self.ISP_contributor_xpath).text
        print(data)

    def ISP_contributor_table(self):
        data = self.driver.find_element(By.XPATH, self.ISP_contributor_table_xpath).text
        print(data)

    def ISP_contributor_table_data(self):
        tabel_data = self.driver.find_element(By.XPATH, self.ISP_contributor_table_data_xpath).text
        print(tabel_data)

    def city_wise_traffic(self):
        data = self.driver.find_element(By.XPATH, self.city_wise_traffic_xpath).text
        print(data)

    def city_wise_traffic_table(self):
        data = self.driver.find_element(By.XPATH, self.city_wise_traffic_table_xpath).text
        print(data)

    def city_wise_traffic_table_data(self):
        tabel_data = self.driver.find_element(By.XPATH, self.city_wise_traffic_table_data_xpath).text
        print(tabel_data)

    def apps(self):
        data = self.driver.find_element(By.XPATH, self.apps_xpath).text
        print(data)

    def apps_table(self):
        data = self.driver.find_element(By.XPATH, self.apps_table_xpath).text
        print(data)

    def apps_table_data(self):
        tabel_data = self.driver.find_element(By.XPATH, self.apps_table_data_xpath).text
        print(tabel_data)

    def external_communication(self):
        data = self.driver.find_element(By.XPATH,self.external_communication_xpath).text
        print(data)

    def external_communication_table(self):
        data = self.driver.find_element(By.XPATH, self.external_communication_table_xpath).text
        print(data)
    def external_communication_table_data(self):
        tabel_data = self.driver.find_element(By.XPATH, self.external_communication_table_data_xpath).text
        print(tabel_data)

    def internet_activities_page(self):
        self.driver.find_element(By.XPATH,self.internet_activities_page_xpath).click()

    def internet_activities_table(self):
        data = self.driver.find_element(By.XPATH,self.internet_activities_table_xpath).text
        print(data)

    def internet_activities_page(self):
        self.driver.find_element(By.XPATH, self.verify_internet_activities_page_xpath).click()

    def verify_internet_activities_page(self):
        return self.driver.find_element(By.XPATH,self.verify_internet_activities_page_xpath).text

    def internet_hostname_data(self):
        data = self.driver.find_element(By.XPATH,self.internet_hostname_data_xpath).text
        print("instance data:", data)

    def internet_hostname_arrow(self):
        self.driver.find_element(By.XPATH,self.internet_hostname_arrow_xpath).click()

    def internet_instance_hostname(self):
        data = self.driver.find_element(By.XPATH,self.internet_instance_hostname_xpath).text
        print("host name data:", data)


    def internet_button(self):
        self.driver.find_element(By.XPATH,self.internet_button_xpath).click()

    def internet_instance_button(self):
        self.driver.find_element(By.XPATH,self.internet_instance_button_xpath).click()

    def total_instances(self):
        instance = self.driver.find_elements(By.XPATH,self.select_instances_xpath)
        print(len(instance))


    def select_instances(self):
        self.driver.find_element(By.XPATH,self.internet_one_instance_xpath).click()



        # instance = self.driver.find_elements(By.XPATH,self.select_instances_xpath)
        # for element in instance:
        #     if element.text == 'mnmv-zebu':
        #         element.click()
        #         break


    def check_internet_interval_dropdown(self):
        self.driver.find_element(By.XPATH, self.check_internet_interval_dropdown_xpath).click()


    def internet_interval_dropdown(self):
        self.driver.find_element(By.XPATH, self.internet_interval_dropdown_xpath).click()


    def internet_dropdown_list(self):
        list = self.driver.find_elements(By.XPATH,self.internet_interval_dropdown_list_xpath)
        for element in list:
            if element.text == 'Yesterday':
                element.click()
                break

    def internet_instance_submit(self):
        self.driver.find_element(By.XPATH,self.internet_instance_submit_xpath).click()



    def zoomview_instance_graph(self):
        # total_instance = self.driver.find_element(By.XPATH, self.instance_total_xpath).text
        # str1 = total_instance.split()
        # i = [int(s) for s in str1 if s.isdigit()]
        # print(i)
        # for n in i:
        #     print(n)
        #     for a in range(1, n + 1):
        xpath_state = "(//div[contains(@id,'zoomview-graphs')]/div)"
        data = self.driver.find_elements(By.XPATH, xpath_state)
        print(data)
        print("successfully displayed graph data")

    def zoomview_instances_graph(self):
        data = self.driver.find_elements(By.XPATH, self.zoomview_instances_graphs_xpath)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//div[contains(@id,'zoomview-graphs')]/div)[" + str(i) + "]").text
            print(s)
        print("success")


    def verify_graph_instance(self):
        data = self.driver.find_element(By.XPATH,self.verify_graph_instance_page_xpath).text
        print(data)

    def zoomview_graph_instances(self):
        data = self.driver.find_elements(By.XPATH, self.graph_instances_page_xpath)
        # a = self.driver.find_element(By.XPATH, self.graph_instances_page_xpath).text
        # print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//div[@class='MuiBox-root css-f0kha9'])[" + str(i) + "]").text
            print(s)
        print("success")


    def select_graph(self):
        self.driver.find_element(By.XPATH,self.graphs_xpath).click()

    def graph_instance_button(self):
        self.driver.find_element(By.XPATH,self.graphs_instance_button_xpath).click()

    def graph_select_all_instance_check_box(self):
        # self.driver.find_element(By.XPATH, self.select_instance_check_box_xpath).click()
        # time.sleep(1)
        self.driver.find_element(By.XPATH, self.select_all_graph_instance_xpath).click()
    def graph_select_instance_check_box(self):
        self.driver.find_element(By.XPATH, self.select_instance_check_box_xpath).click()

    def graph_service_button(self):
        self.driver.find_element(By.XPATH, self.graph_service_button_xpath).click()

    def graph_service_dropdown_list(self):
        list = self.driver.find_elements(By.XPATH, self.service_dropdown_list_xpath)
        # print(list)
        for i in list:
            if i.text == 'CPU':
                i.click()
                break

    def graph_interval_dropdown(self):
        self.driver.find_element(By.XPATH, self.graph_interval_dropdown_xpath).click()

    def graph_dropdown_listitems(self):
        list = self.driver.find_elements(By.XPATH, self.dropdown_listitems_xpath)
        # print(list)
        for i in list:
            if i.text == 'Today':
                i.click()
                break
    def graph_submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()


    def graph_select_instance_check_box(self):
        self.driver.find_element(By.XPATH, self.select_instance_check_box_xpath).click()

    def pause_alerts(self):
        self.driver.find_element(By.XPATH,self.pause_alerts_xpath).click()

    def pause_alerts_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end=' ')

    def rows_drop_down_button(self):
        self.driver.find_element(By.XPATH, self.rows_button_xpath).click()

    def rows_drop_down(self):
        rows = self.driver.find_elements(By.XPATH,self.rows_dropdown_xpath)
        for element in rows:
            if element.text == "100":
                element.click()
                break

    def service_button(self):
        self.driver.find_element(By.XPATH, self.service_button_xpath).click()

    def row_per_page_button(self):
        self.driver.find_element(By.XPATH,self.rows_button_xpath).click()

    def service_table_data(self):
        # row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr")
        # rows = len(row)
        # column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//th")
        # columns = len(column)
        # for r in range(1, rows+1):
        #     for c in range(1, columns+1):
        #         if r == 1:
        #             data =self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr["+str(r)+"]//th["+str(c)+"]")
        #             print(data.text, end='   ')
        #         else:
        #             data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr["+str(r-1)+"]//td["+str(c)+"]")
        #             print(data.text, end='   ')
        #     print()



        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end=' ')


    def hostname_data(self):
        data = self.driver.find_element(By.XPATH,self.hostname_data_xpath).text
        print(data)

    def instance_data(self):
        data = self.driver.find_element(By.XPATH,self.instance_data_xpath).text
        print(data)

    def hostname_button(self):
        self.driver.find_element(By.XPATH,self.hostname_button_xpath).click()

    def zoomview_service_button(self):
        self.driver.find_element(By.XPATH,self.zoomview_service_instance_xpath).click()
    def service_instance(self):
        data = self.driver.find_element(By.XPATH, self.service_instance_xpath).text
        print("select data:", data)
        services = self.driver.find_element(By.XPATH,self.service_instance_xpath)
        services.click()
        self.driver.find_element(By.XPATH,self.select_instance_button_xpath).click()
    def manage_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)
    def manage_zoomview_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(1)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.manage_zoomview_button_xpath)))
        element.click()
    def verify_zoomview_page(self):
        return self.driver.find_element(By.XPATH,self.verify_zoomview_page_xpath).text