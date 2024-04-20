import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FirewallPage:

    def __init__(self,driver):
        self.driver = driver

    manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
    manage_firewall_button_xpath = "(//div[text()='Firewall'])"

    overview_button_xpath = "(//*[text()='Overview'])"
    firewall_policy_button_xpath = "(//*[text()='Firewall Policy'])"

    activity_button_xpath = "//button[text()='Activity']"

    incoming_button_xpath = "//button[text()='Incoming']"
    incoming_wan_button_xpath = "//button[text()='WAN']"
    incoming_captive_button_xpath = "//button[text()='Captive']"
    incoming_others_button_xpath = "//button[text()='Others']"

    outgoing_button_xpath = "//button[text()='Outgoing']"
    outgoing_wan_button_xpath = "//button[text()='WAN']"
    outgoing_captive_button_xpath = "//button[text()='Captive']"
    outgoing_lan_others_button_xpath = "//button[text()='LAN/Others']"

    dropdown_arrow_button_xpath = "(//*[contains(@role,'button')])[2]"
    all_intsance_button_xpath = "(//*[contains(@role,'listbox')])/li"

    verify_firewall_page_text_xpath = "//div[text()='Firewall Assessment last 30 days']"

    verify_incoming_page_text_xpath = "// button[text() = 'WAN']"
    incoming_select_instance_all_button_xpath = "(//*[contains(@aria-haspopup,'listbox')])[2]"
    incoming_total_instance_xpath = "(//*[contains(@role,'listbox')])//li"
    incoming_others_table_button_xpath = "//button[text()='Others']"

    verify_outgoing_page_text_xpath = "//button[text()='Captive']"


    def verify_outgoing_page_text(self):
        return self.driver.find_element(By.XPATH, self.verify_outgoing_page_text_xpath).text

    def firewall_incoming_others_table_row_data(self):
        data = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr").text
        print(data)

    def firewall_incoming_others_table_data(self):
        data = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-17a5us']/*)[2]").text
        print(data)

    def incoming_others_table_button(self):
        self.driver.find_element(By.XPATH, self.incoming_others_table_button_xpath).click()



    def incoming_select_instance_all_button(self):
        self.driver.find_element(By.XPATH, self.incoming_select_instance_all_button_xpath).click()
        list = self.driver.find_elements(By.XPATH, self.incoming_total_instance_xpath)

        for ele in list:
            if ele.text == "All":
                ele.click()
                break


    def incoming_select_one_instance_button(self):
        self.driver.find_element(By.XPATH, self.incoming_select_instance_all_button_xpath).click()
        time.sleep(3)
        list = self.driver.find_elements(By.XPATH, self.incoming_total_instance_xpath)

        for ele in list:
            if ele.text == "10.187.1.74-TulasiramTesting":
                ele.click()
                break


    def verify_incoming_page_text(self):
        return self.driver.find_element(By.XPATH, self.verify_incoming_page_text_xpath).text
    def verify_firewall_page_text(self):
        return self.driver.find_element(By.XPATH, self.verify_firewall_page_text_xpath).text

    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def firewall_page_policy_table_data(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-oedx3l']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-oedx3l']//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-oedx3l']//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='   ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-oedx3l']//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='   ')
            print()


    def firewall_policy_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1mmgwpd']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1mmgwpd']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1mmgwpd']/table//td")]
            data.append(row)
        print(data, end=' ')

    def dropdown_arrow_button(self):
        self.driver.find_element(By.XPATH, self.dropdown_arrow_button_xpath).click()

    def all_button(self):
        data = self.driver.find_elements(By.XPATH, self.all_intsance_button_xpath)
        # print(len(data))
        print("total instances:", len(data))

    def outgoing_lan_others_button(self):
        self.driver.find_element(By.XPATH, self.outgoing_lan_others_button_xpath).click()

    def firewall_outgoing_lan_others_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//td")]
            data.append(row)
        print(data, end=' ')

    def outgoing_captive_button(self):
        self.driver.find_element(By.XPATH,self.outgoing_captive_button_xpath).click()

    def firewall_outgoing_captive_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//td")]
            data.append(row)
        print(data, end=' ')

    def outgoing_button(self):
        self.driver.find_element(By.XPATH, self.outgoing_button_xpath).click()

    def outgoing_wan_button(self):
        self.driver.find_element(By.XPATH,self.outgoing_wan_button_xpath).click()

    def firewall_outgoing_wan_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//td")]
            data.append(row)
        print(data, end=' ')






    def incoming_others_button(self):
        self.driver.find_element(By.XPATH, self.incoming_others_button_xpath).click()

    def firewall_incoming_others_table_row_data(self):
        data = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr").text
        print(data)

    def firewall_incoming_others_table_data(self):
        data = self.driver.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17a5us']/*")
        print(data)

    def incoming_captive_button(self):
        self.driver.find_element(By.XPATH, self.incoming_captive_button_xpath).click()

    def firewall_incoming_captive_table_row_data(self):
        data = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr").text
        print(data)

    def firewall_incoming_captive_table_data(self):
        data = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-17a5us']/*)[2]").text
        print(data)

    # def firewall_incoming_wan_table_data(self):
    #     tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table")
    #     data = []
    #     for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr"):
    #         row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//td")]
    #         data.append(row)
    #     print(data, end=' ')




    def firewall_incoming_wan_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-17ad883']/table//td")]
            data.append(row)
        print(data, end=' ')


    def incoming_button(self):
        self.driver.find_element(By.XPATH, self.incoming_button_xpath).click()

    def incoming_wan_button(self):
        self.driver.find_element(By.XPATH, self.incoming_wan_button_xpath).click()



    def firewall_policy_overview_activity_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end=' ')

    def overview_activity_table(self):
        self.driver.find_element(By.XPATH,self.activity_button_xpath).click()


    def firewall_policy_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1mmgwpd']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1mmgwpd']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1mmgwpd']/table//td")]
            data.append(row)
        print(data, end=' ')

    def overview_button(self):
        self.driver.find_element(By.XPATH,self.overview_button_xpath).click()

    def firewall_policy_button(self):
        self.driver.find_element(By.XPATH,self.firewall_policy_button_xpath).click()

    def manage_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

    def verify_firewall_page(self):
        return self.driver.find_element(By.XPATH, self.manage_firewall_button_xpath).text
    def manage_firewall_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.manage_firewall_button_xpath)))
        element.click()