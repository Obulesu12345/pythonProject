import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Clod_Connect:

    def __init__(self,driver):
        self.driver = driver

    manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
    cloud_connect_text_xpath = "//div[text()='Cloud Connect']"
    cloud_connect_verify_text_xpath = "//button[text()='Overview']"

    link_status_text_xpath = "//h4[text()='Link Status']"
    link_status_data_xpath = "//div[@class='MuiBox-root css-1lekzkb']/div"

    device_status_text_xpath = "//h4[text()='Device Status']"
    # device_status_arrow_button_xpath = "(//*[contains(@data-testid,'ArrowDropDownIcon')])[3]"
    device_status_arrow_routers_button_xpath = "(//*[contains(@role,'button')])[2]"
    routers_list_xpath = "(//ul[contains(@role,'listbox')]/li)"
    device_status_data_xpath = "(//div[contains(@class,'MuiBox-root css-lmo2x')]/div)"

    exchange_button_xpath = "//button[text()='Exchange']"
    exchange_list_data_text_xpath = "(//div[@class='MuiBox-root css-13f2nv4']/div)"

    public_button_xpath = "//button[text()='Public']"
    public_button_data_xpath = "//div[@class='MuiBox-root css-17a5us']"

    cc_dci_button_xpath = "//button[text()='CC-DCI']"
    cc_dci_button_data_xpath = "//div[@class='MuiBox-root css-17a5us']"

    message_button_xpath = "//button[text()='Message']"
    message_links_arrow_button_xpath = "(//*[contains(@role,'button')])[3]"
    message_links_list_xpath = "(//*[contains(@role,'listbox')]/li)"
    message_graph_xpath = "(//canvas[contains(@role,'img')])[2]"
    message_commodity_text_xpath = "(//div[@class='MuiBox-root css-0']/p)"

    app_latency_button_xpath = "(//button[text()='App latency'])"
    app_latency_links_arrow_button_xpath = "(//*[contains(@role,'button')])[3]"
    app_latency_links_list_xpath = "(//*[contains(@role,'listbox')]/li)"
    app_latency_commodity_text_xpath = "(//div[@class='MuiBox-root css-0']/p)"

    app_event_logs_button_xpath = "(//button[text()='App Event Logs'])"
    app_event_logs_data_xpath = "(//div[@class='MuiBox-root css-wkixd3']/div)"

    ha_logs_button_xpath = "//button[text()='HA Logs']"
    ha_logs_protocol_drop_down_xpath = "(//div[contains(@role,'button')])[4]"
    ha_logs_protocol_drop_down_list_items_xpath = "(//ul[contains(@role,'listbox')]/li)"
    ha_logs_protocol_drop_down_list_data_xpath = "(//div[@class='MuiBox-root css-9yh4ja']//self::div)"

    configuration_button_xpath = "//button[text()='Configuration']"
    verify_configuration_page_text_xpath = "//p[text()='Router Configuration']"
    configuration_state_xpath = "(//*[contains(@class,'MuiTable-root css-1udbzah')]/tbody/tr/descendant::td[1])"
    configuration_table_action_button_xpath = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr[1]/td[9])"
    configuration_table_action_button_list_items_xpath = "(//ul[contains(@role,'menu')]/div)"

    configuration_add_button_xpath = "//button[text()='Add']"
    verify_configuration_add_page_text_xpath = "//div[contains(@role,'dialog')]/h2"
    configuration_csv_button_xpath = "//label[contains(@aria-label,'csv')]"

    usage_button_xpath = "//button[text()='Usage']"
    verify_usage_page_xpath = "//label[text()='Router Name']"

    routers_dropdown_button_xpath = "(//div[contains(@role,'button')])[2]"
    routers_drop_down_list_items_xpath = "(//ul[contains(@role,'listbox')]/li)"
    verify_page_for_routers_xpath = "(//button[text()='Bandwidth'])"

    interval_dropdown_button_xpath = "(//div[contains(@role,'button')])[3]"
    interval_drop_down_list_items_xpath = "(//ul[contains(@role,'listbox')]/li)"

    usage_graph_xpath = "//canvas[contains(@role,'img')]"
    usage_table_title_xpath = "//div[@class='MuiBox-root css-gg4vpm']/p"

    rows_per_page_down_button_xpath = "(//div[contains(@role,'button')])[4]"
    rows_per_page_list_items_xpath = "(//ul[contains(@role,'listbox')]/li)"


    def usage_table_data_for_top_apps_airtel(self):
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//th")
        columns = len(column)
        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                if r == 1:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr[" + str(r) + "]//th[" + str(c) + "]")
                    print(data.text, end='    ')
                else:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr[" + str(r - 1) + "]//td[" + str(c) + "]")
                    print(data.text, end='    ')
                    # l.append(data.text)
            print()

    def rows_per_page_down_button(self):
        self.driver.find_element(By.XPATH, self.rows_per_page_down_button_xpath).click()
        time.sleep(1)
        data = self.driver.find_elements(By.XPATH, self.rows_per_page_list_items_xpath)
        print(len(data))
        for element in data:
            if element.text == "100":
                element.click()
                break




    def total_table_data_for_each_single_row(self):
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[1]//tr")
        print(len(row))
        t_Internal = []
        t_External = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(0, len(row) + 1):
            Internal = self.driver.find_element(By.XPATH, "((//table[@class='MuiTable-root css-s064k4'])[1]//tr/descendant::td[1])[" + str(r) + "]").text
            External = self.driver.find_element(By.XPATH, "((//table[@class='MuiTable-root css-s064k4'])[1]//tr/descendant::td[2])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH, "((//table[@class='MuiTable-root css-s064k4'])[1]//tr/descendant::td[3])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH, "((//table[@class='MuiTable-root css-s064k4'])[1]//tr/descendant::td[4])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH, "((//table[@class='MuiTable-root css-s064k4'])[1]//tr/descendant::td[5])[" + str(r) + "]").text
            t_Internal.append(Internal)
            t_External.append(External)
            t_received.append(received)
            t_transmitted.append(transmitted)
            t_total.append(total)
        print(t_Internal)
        print(t_External)
        print(t_received)
        print(t_transmitted)
        print(t_total)

        sizes = t_received
        def size_to_bytes(sizes):
            numeric_value, unit = sizes.split()
            numeric_value = float(numeric_value)
            unit = unit.lower()
            conversion_factors = {
                'gb': 1024 ** 3,
                'mb': 1024 ** 2,
                'kb': 1024,
                'b': 1
            }
            bytes = numeric_value * conversion_factors.get(unit, 1)
            return bytes

        r_sizes_in_bytes = [size_to_bytes(size) for size in sizes]
        print("received data:",r_sizes_in_bytes)

        sizes = t_transmitted
        def size_to_bytes(sizes):
            numeric_value, unit = sizes.split()
            numeric_value = float(numeric_value)
            unit = unit.lower()
            conversion_factors = {
                'gb': 1024 ** 3,
                'mb': 1024 ** 2,
                'kb': 1024,
                'b': 1
            }
            bytes = numeric_value * conversion_factors.get(unit, 1)
            return bytes

        tr_sizes_in_bytes = [size_to_bytes(size) for size in sizes]
        print("transmitted data:", tr_sizes_in_bytes)

        sizes = t_total
        def size_to_bytes(sizes):
            numeric_value, unit = sizes.split()
            numeric_value = float(numeric_value)
            unit = unit.lower()
            conversion_factors = {
                'gb': 1024 ** 3,
                'mb': 1024 ** 2,
                'kb': 1024,
                'b': 1
            }
            bytes = numeric_value * conversion_factors.get(unit, 1)
            return bytes

        to_sizes_in_bytes = [size_to_bytes(size) for size in sizes]
        print("total data:", to_sizes_in_bytes)
        if len(r_sizes_in_bytes) != len(tr_sizes_in_bytes):
            print("Error: Lists have different lengths.")
        else:
            for i in range(len(r_sizes_in_bytes)):
                print("Index:", i)
                print("internal address:", t_Internal[i])
                print("external ip address:", t_External[i])
                print("Received:", r_sizes_in_bytes[i])
                print("Transmitted:", tr_sizes_in_bytes[i])
                print("total data:", to_sizes_in_bytes[i])
                total_tr =  r_sizes_in_bytes[i] + tr_sizes_in_bytes[i]
                print("the sum of received and transmitted data",total_tr)
                if total_tr == to_sizes_in_bytes[i]:
                    print("Total data meets the condition")
                else:
                    print("Total data does not meet the condition")





    def usage_table_data(self):
        title = self.driver.find_element(By.XPATH, self.usage_table_title_xpath).text
        print("table title is:", title)
        # table_header = self.driver.find_element(By.XPATH, "(//div[1][@class='MuiBox-root css-ohbggj']/div[2]//table/thead/tr)").text
        # print(table_header)
        # tbody =self.driver.find_element(By.XPATH, "(//div[1][@class='MuiBox-root css-ohbggj']/div[2]//table/tbody)")
        # data= []
        # for tr in tbody.find_elements(By.XPATH, "//tr"):
        #     row =[item.text for item in tr.find_elements(By.XPATH, ".//td")]
        #     data.append(row)
        #     print(data)


        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[1]//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[1]//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[1]//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end=' ')
                else:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[1]//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='    ')
                    # l.append(data.text)
            print()


    def usage_graph(self):
        data = self.driver.find_element(By.XPATH, self.usage_graph_xpath).text
        print("graph data is:", data)

    def interval_drop_down_list_items(self):
        data = self.driver.find_elements(By.XPATH, self.interval_drop_down_list_items_xpath)
        print(len(data))
        for element in data:
            if element.text == "Today":
                element.click()
                break

    def interval_dropdown_button(self):
        self.driver.find_element(By.XPATH, self.interval_dropdown_button_xpath).click()

    def verify_page_for_routers(self):
        return self.driver.find_element(By.XPATH, self.verify_page_for_routers_xpath).text

    def routers_drop_down_list_items(self):
        data = self.driver.find_elements(By.XPATH, self.routers_drop_down_list_items_xpath)
        print(len(data))
        for element in data:
            if element.text == "NSE-AIRTEL-R1":
                element.click()
                break

    def routers_dropdown_button(self):
        self.driver.find_element(By.XPATH, self.routers_dropdown_button_xpath).click()

    def verify_usage_page(self):
        return self.driver.find_element(By.XPATH, self.verify_usage_page_xpath).text

    def usage_button(self):
        self.driver.find_element(By.XPATH, self.usage_button_xpath).click()

    def configuration_csv_button(self):
        self.driver.find_element(By.XPATH, self.configuration_csv_button_xpath).click()
    def verify_configuration_add_page_text(self):
        return self.driver.find_element(By.XPATH, self.verify_configuration_add_page_text_xpath).text

    def configuration_add_button(self):
        self.driver.find_element(By.XPATH, self.configuration_add_button_xpath).click()

    def configuration_table_action_button_list_items(self):
        lists = self.driver.find_elements(By.XPATH, self.configuration_table_action_button_list_items_xpath)
        data = len(lists)
        print(data)
        lists = self.driver.find_element(By.XPATH, self.configuration_table_action_button_list_items_xpath).text
        print(lists)

    def configuration_table_action_button(self):
        self.driver.find_element(By.XPATH, self.configuration_table_action_button_xpath).click()

    def configuration_state_button(self):
        n = len(self.driver.find_elements(By.XPATH, self.configuration_state_xpath))
        for a in range(1,n+1):
            xpath_state = "(//table[@class='MuiTable-root css-1udbzah']/tbody/tr/td[1])[" + str(a) + "]"
            element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_state)))
            self.driver.execute_script("arguments[0].click();", element)
            state_data = "(//*[contains(@class,'MuiTable-root css-1udbzah')]/tbody/tr/descendant::td[1])[" + str(a) + "]"
            data = self.driver.find_element(By.XPATH, state_data).text
            print(data)

    def verify_configuration_page_text(self):
        return self.driver.find_element(By.XPATH, self.verify_configuration_page_text_xpath).text

    def configuration_table_data(self):
        title = self.driver.find_element(By.XPATH, self.verify_configuration_page_text_xpath).text
        print("table title is:", title)
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end=' ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-1udbzah']//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='    ')
                    # l.append(data.text)
            print()

    def configuration_button(self):
        self.driver.find_element(By.XPATH, self.configuration_button_xpath).click()

    def ha_logs_protocol_drop_down_list_data(self):
        data = self.driver.find_elements(By.XPATH, self.ha_logs_protocol_drop_down_list_data_xpath)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//div[@class='MuiBox-root css-9yh4ja']//self::div)[" + str(i) + "]").text
            print(s, end="   ")

    def ha_logs_protocol_drop_down_list_items(self):
        data = self.driver.find_elements(By.XPATH, self.ha_logs_protocol_drop_down_list_items_xpath)
        print(len(data))
        for element in data:
            if element.text == "HSRP":
                element.click()
                break

    def ha_logs_protocol_drop_down(self):
        self.driver.find_element(By.XPATH, self.ha_logs_protocol_drop_down_xpath).click()

    def ha_logs_button(self):
        self.driver.find_element(By.XPATH, self.ha_logs_button_xpath).click()

    def app_event_logs_data(self):
        data = self.driver.find_elements(By.XPATH, self.app_event_logs_data_xpath)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//div[@class='MuiBox-root css-wkixd3']/div)[" + str(i) + "]").text
            print(s)

    def app_event_logs_button(self):
        self.driver.find_element(By.XPATH, self.app_event_logs_button_xpath).click()

    def app_latency_commodity_text(self):
        data = self.driver.find_element(By.XPATH, self.app_latency_commodity_text_xpath).text
        print(data)

    def app_latency_links_list(self):
        data = self.driver.find_elements(By.XPATH, self.app_latency_links_list_xpath)
        print(len(data))
        for element in data:
            if element.text == "BSE-TCL-TJ":
                element.click()
                break


    def app_latency_links_length_list(self):
        data = self.driver.find_elements(By.XPATH, self.app_latency_links_list_xpath)
        list = len(data)
        print("no of links in a list:", list)

    def app_latency_links_arrow_button(self):
        self.driver.find_element(By.XPATH, self.app_latency_links_arrow_button_xpath).click()

    def app_latency_button(self):
        self.driver.find_element(By.XPATH, self.app_latency_button_xpath).click()

    def message_graph(self):
        data = self.driver.find_element(By.XPATH, self.message_graph_xpath).text
        print(data)

    def message_commodity_text(self):
        data = self.driver.find_element(By.XPATH, self.message_commodity_text_xpath).text
        print(data)

    def message_links_list(self):
        data = self.driver.find_elements(By.XPATH, self.message_links_list_xpath)
        print(len(data))
        for element in data:
            if element.text == "BSE-TCL-TJ":
                element.click()
                break


    def message_links_length_list(self):
        data = self.driver.find_elements(By.XPATH, self.message_links_list_xpath)
        list = len(data)
        print("no of links in a list:", list)

    def message_links_arrow_button(self):
        self.driver.find_element(By.XPATH, self.message_links_arrow_button_xpath).click()

    def message_button(self):
        self.driver.find_element(By.XPATH, self.message_button_xpath).click()

    def cc_dci_button_data(self):
        data = self.driver.find_element(By.XPATH, self.cc_dci_button_data_xpath).text
        print(data)

    def cc_dci_button(self):
        self.driver.find_element(By.XPATH, self.cc_dci_button_xpath).click()

    def public_button_data(self):
        data = self.driver.find_element(By.XPATH, self.public_button_data_xpath).text
        print(data)

    def public_button(self):
        self.driver.find_element(By.XPATH, self.public_button_xpath).click()

    def exchange_list_data_text(self):
        d = []
        data = self.driver.find_elements(By.XPATH, self.exchange_list_data_text_xpath)
        list = len(data)
        print(list)
        for element in data:
            text = element.text.strip().replace('\n', '  ')
            d.append(text)
        print(d)


    def exchange_button(self):
        self.driver.find_element(By.XPATH, self.exchange_button_xpath).click()

    def device_status_data(self):
        d = []
        data = self.driver.find_elements(By.XPATH, self.device_status_data_xpath)
        for element in data:
            text = element.text.strip().replace('\n', '  ')
            d.append(text)
        print(d)

    def routers_lengtn_list(self):
        data = self.driver.find_elements(By.XPATH, self.routers_list_xpath)
        list = len(data)
        print("no of routers in a list:", list)

    def routers_list(self):
        data = self.driver.find_elements(By.XPATH, self.routers_list_xpath)
        print(len(data))
        for element in data:
            if element.text == 'NSE-AIRTEL-R1':
                element.click()
                break


    def device_status_arrow_routers_button(self):
        self.driver.find_element(By.XPATH, self.device_status_arrow_routers_button_xpath).click()

    def device_status_text(self):
        data = self.driver.find_element(By.XPATH, self.device_status_text_xpath).text
        print(data)

    def link_status_data(self):
        data = self.driver.find_element(By.XPATH, self.link_status_data_xpath).text
        print(data)

    def link_status_text(self):
        data = self.driver.find_element(By.XPATH, self.link_status_text_xpath).text
        print(data)

    def overview_button(self):
        self.driver.find_element(By.XPATH, self.cloud_connect_verify_text_xpath).click()

    def cloud_connect_verify_text(self):
        return self.driver.find_element(By.XPATH, self.cloud_connect_verify_text_xpath).text


    def cloud_connect_button(self):
        self.driver.find_element(By.XPATH, self.cloud_connect_text_xpath).click()

    def verify_cloud_connect_text(self):
        return self.driver.find_element(By.XPATH, self.cloud_connect_text_xpath).text

    def manage_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()

    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)