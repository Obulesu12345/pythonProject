import subprocess
import time
import os
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstancePage:

    def __init__(self,driver):
        self.driver = driver

    manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
    instance_button_xpath = "(//div[text()='Instance'])"
    instance_table_rows_xpath = "//table[@class='MuiTable-root css-s064k4']//tr"
    instance_table_columns_xpath = "//table[@class='MuiTable-root css-s064k4']//th"
    table_action_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr/td[@dataindex='action'])[1]"
    performance_button_xpath = "//span[text()='Performance']"
    performance_instance_button_xpath = "//button[text()='Instances']"

    select_instance_check_box_xpath = "(//input[contains(@type,'checkbox')])[4]"
    intervel_dropdown_xpath = "(//div[contains(@role,'button')])[3]"
    dropdown_listitems_xpath = "(//ul[contains(@role,'listbox')])//li"
    submit_button_xpath = "//button[text()='Submit']"
    service_button_xpath ="//div[@id='demo-select-small']"
    service_dropdown_list_xpath = "//ul[contains(@role,'listbox')]//li"

    warning_xpath = "//button[text()='Warnings']"
    warning_table_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"

    criticals_xpath = "//button[text()='Criticals']"
    critical_table_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"

    location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"

    verify_instances_text_xpath = "//p[text()='Instances']"

    table_instance_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr[2]/td)[3]"
    table_instance_notification_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr[2]/td)[9]"

    instance_table_ok_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])"

    instance_table_warn_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])"

    instance_table_crit_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])"

    instance_warning_no_of_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"

    verify_dashboard_manage_page_xpath = "//div[text()='Instance']"

    cpu_utilization_data_xpath  = "//canvas[contains(@role,'img')]"
    select_all_check_box_xpath = "(// input[contains( @ type, 'checkbox')])[1]"
    select_one_check_box_xpath = "(// input[contains( @ type, 'checkbox')])[2]"
    graph_instances_page_xpath = "(//div[@class='MuiBox-root css-f0kha9'])"
    instance_name_text_xpath = "//div[contains(@class,'MuiBox-root css-1l4w6pd')]/p"

    verify_performance_hostname_text_xpath = "//div[@class='MuiBox-root css-9lsp3l']"

    instances_graph_text_xpath = "//div[@id='zoomview-graphs']/div"
    services_ok_xpath = "//p[text()='Services']/parent::div/descendant::div[9]"
    services_total_xpath = "//p[text()='Services']/parent::div/descendant::div[6]"
    services_warn_xpath = "//p[text()='Services']/parent::div/descendant::div[12]"
    services_crit_xpath = "//p[text()='Services']/parent::div/descendant::div[15]"


    graphs_xpath = "(//canvas[contains(@role,'img')])"
    zoomview_graphs_xpath = "(//div[contains(@id,'zoomview-graphs')])/div"


    def graphs_data(self):
        data = self.driver.find_elements(By.XPATH, self.graphs_xpath)
        total = len(data)
        for n in range(total):
            # print(n)
            for a in range(1,n+1):
                xpath_state = "(//canvas[contains(@role,'img')])["+str(a)+"]"
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_state)))
                self.driver.execute_script("arguments[0].click();", element)
                print("successfully displayed graph data:", element.text)

        # cpu = self.driver.find_element(By.XPATH, self.graphs_xpath).text
        # print("graph data:", cpu)

    def zoomview_graphs_data(self):
        data = self.driver.find_elements(By.XPATH, self.zoomview_graphs_xpath)
        i = len(data)
        for n in range(i):
            # print(n)
            for a in range(1,n+1):
                xpath_state = "(//div[contains(@id,'zoomview-graphs')])/div["+str(a)+"]"
                element = WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable((By.XPATH, xpath_state)))
                self.driver.execute_script("arguments[0].click();", element)
                print("successfully displayed zoom view data:", element.text)
        # cpu = self.driver.find_element(By.XPATH, self.zoomview_graphs_xpath).text
        # print("zommview data:", cpu)

    def verify_instance_table_crit_and_dashboard_crit(self):
        dashboard_crit = self.driver.find_element(By.XPATH,self.services_crit_xpath).text
        print("dash board service warn is:", dashboard_crit)

        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()

        data = self.driver.find_elements(By.XPATH, self.instance_table_crit_button_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
            l.append(int(s))
        crit= sum(l)
        print("total criticals:", crit)


        if dashboard_crit == crit:
            print("matched")
        else:
            print("not matched")


    def verify_instance_table_warn_and_dashboard_warn(self):
        dashboard_warn = self.driver.find_element(By.XPATH,self.services_warn_xpath).text
        print("dash board service warn is:", dashboard_warn)
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()

        data = self.driver.find_elements(By.XPATH, self.instance_table_warn_button_xpath)
        l=[]
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])["+str(i)+"]").text
            try:
                l.append(int(s))
            except ValueError:
                print("value:", s)

        instance_warn = sum(l)
        print("total instance ok is:", instance_warn)

        if instance_warn == dashboard_warn:
            print("matched")
        else:
            print("not matched")

    def verify_instance_table_ok_and_dashboard_ok(self):
        dashboard_ok = self.driver.find_element(By.XPATH,self.services_ok_xpath).text
        print(" dash boardservice ok:", dashboard_ok)
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()

        data = self.driver.find_elements(By.XPATH, self.instance_table_ok_button_xpath)
        l=[]
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])["+str(i)+"]").text
            try:
                l.append(int(s))
            except ValueError:
                print("value:", s)

        instance_ok = sum(l)
        print("total instance ok is:", instance_ok)

        if instance_ok == dashboard_ok:
            print("matched")
        else:
            print("not matched")



    def service_ok(self):
        ok = self.driver.find_element(By.XPATH,self.services_ok_xpath).text
        print("service ok:", ok)

    def instance_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()









    def instances_graph_text(self):
        data = self.driver.find_elements(By.XPATH, self.instances_graph_text_xpath)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//div[@id='zoomview-graphs']/div)[" + str(i) + "]").text
            print(s)




    def verify_performance_hostname_text(self):
        hostname =  self.driver.find_element(By.XPATH, self.verify_performance_hostname_text_xpath).text
        print("host name is:", hostname)
    def cpu_graph_instances(self):
        data = self.driver.find_elements(By.XPATH, self.graph_instances_page_xpath)
        a = self.driver.find_element(By.XPATH, self.graph_instances_page_xpath).text
        print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//div[@class='MuiBox-root css-f0kha9'])[" + str(i) + "]").text
            print(s)

        data = self.driver.find_elements(By.XPATH, self.instance_name_text_xpath)
        a = self.driver.find_element(By.XPATH, self.instance_name_text_xpath).text
        print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//div[contains(@class,'MuiBox-root css-1l4w6pd')]/p)[" + str(i) + "]").text
            print(s)

        cpu = self.driver.find_elements(By.XPATH, self.cpu_utilization_data_xpath)
        c = self.driver.find_element(By.XPATH, self.cpu_utilization_data_xpath).text
        print("cpu:", c)
        for i in range(1, len(cpu) + 1):
            s = self.driver.find_element(By.XPATH, "(//canvas[contains(@role,'img')])[" + str(i) + "]").text
            # print(s)
            print("cpu utilization data:", s)



    def cpu_utilization_data(self):
        cpu = self.driver.find_element(By.XPATH, self.cpu_utilization_data_xpath).text
        print("cpu utilization data:", cpu)


    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def manage_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()

    def verify_dashboard_manage_page(self):
        return self.driver.find_element(By.XPATH, self.verify_dashboard_manage_page_xpath).text


    def instance_no_of_criticals(self):
        warnings_data = self.driver.find_elements(By.XPATH, self.instance_warning_no_of_xpath)
        print(len(warnings_data))

    def instance_no_of_warnings(self):
        warnings_data = self.driver.find_elements(By.XPATH, self.instance_warning_no_of_xpath)
        print(len(warnings_data))


    def verify_total_service(self):
        dashboard_total = self.driver.find_element(By.XPATH,self.services_total_xpath).text
        print("dash board service warn is:", dashboard_total)

        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(1)
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()

        data = self.driver.find_elements(By.XPATH, self.instance_table_crit_button_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
            l.append(int(s))
        print(sum(l))
        crit = sum(l)

        data = self.driver.find_elements(By.XPATH, self.instance_table_warn_button_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])[" + str(i) + "]").text
            l.append(int(s))
        print(sum(l))
        warn = sum(l)

        data = self.driver.find_elements(By.XPATH, self.instance_table_ok_button_xpath)
        l=[]
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])["+str(i)+"]").text
            l.append(int(s))
        print(sum(l))
        ok = sum(l)

        total = crit + warn + ok
        print("total instance is :", total)

        if dashboard_total == total:
            print("total is matched")
        else:
            print("not matched")








    def instance_table_crit_button(self):
        data = self.driver.find_elements(By.XPATH, self.instance_table_crit_button_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
            l.append(int(s))
        crit = sum(l)
        print("total criticals:", crit)

        self.driver.find_element(By.XPATH,"//button[text()='Criticals']").click()
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-ada2d3'])//tr")
        rows = len(row)
        print("length of rows:", rows)
        if crit == rows:
            print("matched")
        else:
            print("not matched")

    def instance_table_warn_button(self):
        data = self.driver.find_elements(By.XPATH, self.instance_table_warn_button_xpath)
        l=[]
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])["+str(i)+"]").text
            try:
                l.append(int(s))
            except ValueError:
                print("value:", s)
        warn = sum(l)
        print("total warnings:", warn)
        self.driver.find_element(By.XPATH,"//button[text()='Warnings']").click()
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-ada2d3'])//tr")
        rows = len(row)
        print("length of rows:",rows)

        if warn == rows:
            print("matched")
        else:
            print("not matched")



        # print("success")

    def instance_table_ok_button(self):
        dash_ok = self.driver.find_element(By.XPATH, self.services_ok_xpath).text
        print("service ok:", dash_ok)

        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()

        data = self.driver.find_elements(By.XPATH, self.instance_table_ok_button_xpath)
        l=[]
        a=self.driver.find_element(By.XPATH, self.instance_table_ok_button_xpath).text
        for i in range(1, len(data)+1):
            s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])["+str(i)+"]").text
            try:
                l.append(int(s))
            except ValueError:
                print("value:", s)
            # l.append(int(s))
        instance_ok = sum(l)
        print("instance total ok:", instance_ok)
        if dash_ok == instance_ok:
            print("matched ok instance")
        else:
            print("not matched")
        # print("success")

    def table_instance_notification_button(self):
        self.driver.find_element(By.XPATH, self.table_instance_notification_button_xpath).click()

    def table_instance_notification_data(self):
        tbody = self.driver.find_element(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table//td")]
            data.append(row)
        print(data, end=' ')


    def instance_page_under_notification_table_data(self):
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='   ')
                else:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='   ')
            print()

    def table_instance_button(self):
        element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.table_instance_button_xpath)))
        element.click()
        # self.driver.find_element(By.XPATH, self.table_instance_button_xpath).click()

    def table_instance_data(self):
        tbody = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table//td")]
            data.append(row)
        print(data, end=' ')

    def instance_page_under_table_data(self):
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='   ')
                else:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4'])[2]//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='   ')
            print()



    def verify_instances_text(self):
        return self.driver.find_element(By.XPATH, self.verify_instances_text_xpath).text

    def location(self):
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def location_dropdown(self):

        element = self.driver.find_element(By.XPATH, self.dropdown_elements_xpath)
        element.click()
        # for location in element:
        #     if location.text == "India (Mumbai) IN-MUM-WEST-2":
        #         location.click()
        #         break

    def instance_criticals(self):
        self.driver.find_element(By.XPATH, self.criticals_xpath).click()

    def critical_table(self):
        data = self.driver.find_element(By.XPATH, self.critical_table_xpath).text
        print(data)

    def critical_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//td")]
            data.append(row)
        print(data, end=' ')



    def instance_warnings(self):
        self.driver.find_element(By.XPATH,self.warning_xpath).click()

    def warning_table(self):
        data = self.driver.find_element(By.XPATH,self.warning_table_xpath).text
        print(data)

    def warning_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//td")]
            data.append(row)
        print(data, end=' ')

    def instance_page_warning_table_data(self):
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-ada2d3'])//tr")
        rows = len(row)
        print("length of rows:",rows)
        # column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-ada2d3'])//th")
        # columns = len(column)
        for r in range(1, rows+1):
            # for c in range(1, columns+1):
            #     if r == 1:
            data =self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-ada2d3'])//tr["+str(r)+"]")
            print(data.text, end='   ')
            # else:
            #     data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-ada2d3'])//tr["+str(r-1)+"]//td["+str(c)+"]")
            #         print(data.text, end='   ')
            # print()


    def service_button(self):
        self.driver.find_element(By.XPATH, self.service_button_xpath).click()

    def service_dropdown_list(self):
        list = self.driver.find_elements(By.XPATH, self.service_dropdown_list_xpath)
        # print(list)
        for i in list:
            if i.text == 'CPU':
                i.click()
                break
    def dropdown_listitems(self):
        list = self.driver.find_elements(By.XPATH, self.dropdown_listitems_xpath)
        # print(list)
        for i in list:
            if i.text == 'Today':
                i.click()
                break
    def submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()


    def select_instance_check_box(self):
        self.driver.find_element(By.XPATH, self.select_all_check_box_xpath).click()

    def select_one_instance_check_box(self):
        self.driver.find_element(By.XPATH, self.select_one_check_box_xpath).click()

    def performance_instance_button(self):
        self.driver.find_element(By.XPATH, self.performance_instance_button_xpath).click()

    def intervel_dropdown(self):
        self.driver.find_element(By.XPATH, self.intervel_dropdown_xpath).click()

    def instances_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

    def instance_page(self):
        self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
        element.click()

    def table_instance_action_performance(self):
        self.driver.find_element(By.XPATH, self.table_action_button_xpath).click()

    def action_performance(self):
        self.driver.find_element(By.XPATH,self.performance_button_xpath).click()

    def instance_total_rows(self):
        rows = self.driver.find_elements(By.XPATH,self.instance_table_rows_xpath)
        return print(len(rows))
    def instance_total_columns(self):
        columns = self.driver.find_elements(By.XPATH, self.instance_table_columns_xpath)
        return print(len(columns))

    def instance_table_data(self):
        thead = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1fpff4c']/table/thead")
        data = []
        for tr in thead.find_elements(By.XPATH, "//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, ".//th")]
            data.append(row)
            import os
            directory = 'output'
            if not os.path.exists(directory):
                os.makedirs(directory)
            output_text = ['\t'.join(map(str, sublist)) for sublist in data]
            file_path = os.path.join(directory, 'instance_output.txt')
            with open(file_path, 'w') as file:
                file.write('\n'.join(output_text))
            subprocess.Popen(['notepad.exe', 'instance_output.txt'])

        tbody =self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1fpff4c']/table/tbody")
        data= []
        for tr in tbody.find_elements(By.XPATH, "//tr"):
            row =[item.text for item in tr.find_elements(By.XPATH, ".//td")]
            data.append(row)
            import os
            # Check if the directory exists, if not create it
            directory = 'output'
            if not os.path.exists(directory):
                os.makedirs(directory)

            output_text = ['\t'.join(map(str, sublist)) for sublist in data]

            file_path = os.path.join(directory, 'instance_output.txt')
            with open(file_path, 'w') as file:
                file.write('\n'.join(output_text))
            subprocess.Popen(['notepad.exe', 'instance_output.txt'])


            # # Write the output to a temporary text file
            # with open('instance_output.txt', 'w') as file:
            #     file.write('\n'.join(output_text))



        # tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        # data = []
        # for tr in tbody.find_elements(By.XPATH, "//tr"):
        #     row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table)//td")]
        #     data.append(row)
        # print(data, end=' ')


    def instance_page_table_data(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//th")
        columns = len(column)
        th = []
        tb = []
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r)+"]//th["+str(c)+"]")
                    th.append(data.text)
                    # print(data.text, end='   ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r-1)+"]//td["+str(c)+"]")
                    tb.append(data.text)
                    # print(data.text, end='   ')
            print()
            # import os
            # # Check if the directory exists, if not create it
            # directory = 'output'
            # if not os.path.exists(directory):
            #     os.makedirs(directory)
            #
            # output_text = ['\t'.join(map(str, sublist)) for sublist in data]
            #
            # file_path = os.path.join(directory, 'instance_output.txt')
            # with open(file_path, 'w') as file:
            #     file.write('\n'.join(output_text))
            # subprocess.Popen(['notepad.exe', 'instance_output.txt'])











































# import time
#
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class InstancePage:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     manage_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[2]"
#     instance_button_xpath = "(//div[text()='Instance'])"
#     instance_table_rows_xpath = "//table[@class='MuiTable-root css-s064k4']//tr"
#     instance_table_columns_xpath = "//table[@class='MuiTable-root css-s064k4']//th"
#     table_action_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr/td[@dataindex='action'])[1]"
#     performance_button_xpath = "//span[text()='Performance']"
#     performance_instance_button_xpath = "//button[text()='Instances']"
#
#     select_instance_check_box_xpath = "(//input[contains(@type,'checkbox')])[4]"
#     intervel_dropdown_xpath = "(//div[contains(@role,'button')])[3]"
#     dropdown_listitems_xpath = "(//ul[contains(@role,'listbox')])//li"
#     submit_button_xpath = "//button[text()='Submit']"
#     service_button_xpath ="//div[@id='demo-select-small']"
#     service_dropdown_list_xpath = "//ul[contains(@role,'listbox')]//li"
#
#     warning_xpath = "//button[text()='Warnings']"
#     warning_table_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"
#
#     criticals_xpath = "//button[text()='Criticals']"
#     critical_table_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"
#
#     location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
#     dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"
#
#     verify_instances_text_xpath = "//p[text()='Instances']"
#
#     table_instance_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr[2]/td)[3]"
#     table_instance_notification_button_xpath = "(//table[@class='MuiTable-root css-s064k4']//tr[2]/td)[9]"
#
#     instance_table_ok_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])"
#
#     instance_table_warn_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])"
#
#     instance_table_crit_button_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])"
#
#     instance_warning_no_of_xpath = "//tbody[@class='MuiTableBody-root css-1xnox0e']//tr"
#
#
#     def instance_no_of_criticals(self):
#         warnings_data = self.driver.find_elements(By.XPATH, self.instance_warning_no_of_xpath)
#         print(len(warnings_data))
#
#     def instance_no_of_warnings(self):
#         warnings_data = self.driver.find_elements(By.XPATH, self.instance_warning_no_of_xpath)
#         print(len(warnings_data))
#
#
#     def verify_total_service(self):
#         data = self.driver.find_elements(By.XPATH, self.instance_table_crit_button_xpath)
#         l = []
#         # a = self.driver.find_element(By.XPATH, self.instance_table_crit_button_xpath).text
#         # print(a)
#         # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
#         # print(sum(data))
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
#             l.append(int(s))
#         print(sum(l))
#         crit = sum(l)
#
#         data = self.driver.find_elements(By.XPATH, self.instance_table_warn_button_xpath)
#         l = []
#         # a = self.driver.find_element(By.XPATH, self.instance_table_warn_button_xpath).text
#         # print(a)
#         # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
#         # print(sum(data))
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])[" + str(i) + "]").text
#             l.append(int(s))
#         print(sum(l))
#         warn = sum(l)
#
#         data = self.driver.find_elements(By.XPATH, self.instance_table_ok_button_xpath)
#         l=[]
#         # a=self.driver.find_element(By.XPATH, self.instance_table_ok_button_xpath).text
#         # print(a)
#         # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
#         # print(sum(data))
#         for i in range(1, len(data)+1):
#             s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])["+str(i)+"]").text
#             l.append(int(s))
#         print(sum(l))
#         ok = sum(l)
#
#         total = crit + warn + ok
#         print("total instance is :", total)
#
#
#
#
#
#
#
#
#     def instance_table_crit_button(self):
#         data = self.driver.find_elements(By.XPATH, self.instance_table_crit_button_xpath)
#         l = []
#         a = self.driver.find_element(By.XPATH, self.instance_table_crit_button_xpath).text
#         # print(a)
#         # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
#         # print(sum(data))
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
#             l.append(int(s))
#         print(sum(l))
#         print("success")
#
#     def instance_table_warn_button(self):
#         data = self.driver.find_elements(By.XPATH, self.instance_table_warn_button_xpath)
#         l=[]
#         a=self.driver.find_element(By.XPATH, self.instance_table_warn_button_xpath).text
#         # print(a)
#         # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
#         # print(sum(data))
#         for i in range(1, len(data)+1):
#             s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])["+str(i)+"]").text
#             try:
#                 l.append(int(s))
#             except ValueError:
#                 print("value:", s)
#             # l.append(int(s))
#         print(sum(l))
#         print("success")
#
#     def instance_table_ok_button(self):
#         data = self.driver.find_elements(By.XPATH, self.instance_table_ok_button_xpath)
#         l=[]
#         a=self.driver.find_element(By.XPATH, self.instance_table_ok_button_xpath).text
#         # print(a)
#         # s = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])")
#         # print(sum(data))
#         for i in range(1, len(data)+1):
#             s=self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])["+str(i)+"]").text
#             try:
#                 l.append(int(s))
#             except ValueError:
#                 print("value:", s)
#             # l.append(int(s))
#         print(sum(l))
#         print("success")
#
#     def table_instance_notification_button(self):
#         self.driver.find_element(By.XPATH, self.table_instance_notification_button_xpath).click()
#
#     def table_instance_notification_data(self):
#         tbody = self.driver.find_element(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "(//div[@class='MuiBox-root css-1fpff4c'])[2]//table//td")]
#             data.append(row)
#         print(data, end=' ')
#
#     def table_instance_button(self):
#         element = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, self.table_instance_button_xpath)))
#         element.click()
#         # self.driver.find_element(By.XPATH, self.table_instance_button_xpath).click()
#
#     def table_instance_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "//div[@class='MuiBox-root css-1l3xj4b']/table//td")]
#             data.append(row)
#         print(data, end=' ')
#
#
#
#     def verify_instances_text(self):
#         return self.driver.find_element(By.XPATH, self.verify_instances_text_xpath).text
#
#     def location(self):
#         self.driver.find_element(By.XPATH, self.location_xpath).click()
#
#     def location_dropdown(self):
#
#         element = self.driver.find_element(By.XPATH, self.dropdown_elements_xpath)
#         element.click()
#         # for location in element:
#         #     if location.text == "India (Mumbai) IN-MUM-WEST-2":
#         #         location.click()
#         #         break
#
#     def instance_criticals(self):
#         self.driver.find_element(By.XPATH, self.criticals_xpath).click()
#
#     def critical_table(self):
#         data = self.driver.find_element(By.XPATH, self.critical_table_xpath).text
#         print(data)
#
#     def critical_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//td")]
#             data.append(row)
#         print(data, end=' ')
#
#
#
#     def instance_warnings(self):
#         self.driver.find_element(By.XPATH,self.warning_xpath).click()
#
#     def warning_table(self):
#         data = self.driver.find_element(By.XPATH,self.warning_table_xpath).text
#         print(data)
#
#     def warning_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1j2is0p']/table//td")]
#             data.append(row)
#         print(data, end=' ')
#
#     def service_button(self):
#         self.driver.find_element(By.XPATH, self.service_button_xpath).click()
#
#     def service_dropdown_list(self):
#         list = self.driver.find_elements(By.XPATH, self.service_dropdown_list_xpath)
#         print(list)
#         for i in list:
#             if i.text == 'CPU':
#                 i.click()
#                 break
#     def dropdown_listitems(self):
#         list = self.driver.find_elements(By.XPATH, self.dropdown_listitems_xpath)
#         print(list)
#         for i in list:
#             if i.text == 'Today':
#                 i.click()
#                 break
#     def submit_button(self):
#         self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
#
#
#     def select_instance_check_box(self):
#         self.driver.find_element(By.XPATH, self.select_instance_check_box_xpath).click()
#
#     def performance_instance_button(self):
#         self.driver.find_element(By.XPATH, self.performance_instance_button_xpath).click()
#
#     def intervel_dropdown(self):
#         self.driver.find_element(By.XPATH, self.intervel_dropdown_xpath).click()
#
#     def instances_page(self):
#         self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
#         time.sleep(5)
#
#     def instance_page(self):
#         self.driver.find_element(By.XPATH, self.manage_button_xpath).click()
#         time.sleep(5)
#
#         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.instance_button_xpath)))
#         element.click()
#
#     def table_instance_action_performance(self):
#         self.driver.find_element(By.XPATH, self.table_action_button_xpath).click()
#
#     def action_performance(self):
#         self.driver.find_element(By.XPATH,self.performance_button_xpath).click()
#
#     def instance_total_rows(self):
#         rows = self.driver.find_elements(By.XPATH,self.instance_table_rows_xpath)
#         return print(len(rows))
#     def instance_total_columns(self):
#         columns = self.driver.find_elements(By.XPATH, self.instance_table_columns_xpath)
#         return print(len(columns))
#
#     def instance_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table)//td")]
#             data.append(row)
#         print(data, end=' ')
#
