import os
import subprocess
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SummaryReport:

    def __init__(self,driver):
        self.driver = driver

    report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
    verify_reports_page = "//*[text()='Reports']"
    ip_tracking_page_xpath = "//*[text()='Summary Report']"
    verify_summary_page_xpath = "(//div[contains(@class,'MuiBox-root css-1c1kq07')])[1]"

    public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
    public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
    submit_button_xpath = "//button[text()='Submit']"

    table_title_xpath = "//div[contains(@class,'MuiBox-root css-1c1kq07')]"
    summary_table_title_xpath = "(//div[contains(@class,'MuiBox-root css-1c1kq07')])[1]"

    external_communication_table_received_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3]"
    external_communication_table_transmitted_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4]"
    external_communication_table_total_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5]"

    apps_table_received_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[4])"
    apps_table_transmitted_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[5])"
    apps_table_total_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[6])"

    city_wise_traffic_table_xpath = "//*[contains(@class,'MuiBox-root css-14w0bz')]/div"
    # city_wise_traffic_table_xpath = "//p[text()='No Data']"
    csv_xpath = "//label[contains(@aria-label,'csv')]"

    def csv(self):
        self.driver.find_element(By.XPATH, self.csv_xpath).click()

    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)


    def total_table_data_for_each_single_row_for_apps(self):
        row = self.driver.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr)")
        print(len(row))
        t_App = []
        t_Active = []
        t_Total_Connection = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(1, len(row) + 1):
            App = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[1])[" + str(r) + "]").text
            Active = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[2])[" + str(r) + "]").text
            Total_Connection = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[3])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[4])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[5])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[6])[" + str(r) + "]").text
            t_App.append(App)
            t_Active.append(Active)
            t_Total_Connection.append(Total_Connection)
            t_received.append(received)
            t_transmitted.append(transmitted)
            t_total.append(total)
        print(t_App)
        print(t_Active)
        print(t_Total_Connection)
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
                print("app address:", t_App[i])
                print("active connection:", t_Active[i])
                print("Received:", r_sizes_in_bytes[i])
                print("Transmitted:", tr_sizes_in_bytes[i])
                print("total data:", to_sizes_in_bytes[i])
                total_tr =  r_sizes_in_bytes[i] + tr_sizes_in_bytes[i]
                print("the sum of received and transmitted data",total_tr)
                if total_tr == to_sizes_in_bytes[i]:
                    print("Total data meets the condition")
                else:
                    print("Total data does not meet the condition")




    def total_table_data_for_each_single_row_for_city_wise_traffic(self):
        row = self.driver.find_elements(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr")
        print(len(row))
        t_Domain = []
        t_pubilc = []
        t_Country = []
        t_State = []
        t_City = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(1, len(row) + 1):
            Domain = self.driver.find_element(By.XPATH,"((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[1])[" + str(r) + "]").text
            pubilc = self.driver.find_element(By.XPATH, "((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[2])[" + str(r) + "]").text
            Country = self.driver.find_element(By.XPATH, "((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[3])[" + str(r) + "]").text
            state = self.driver.find_element(By.XPATH,"((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[4])[" + str(r) + "]").text
            city = self.driver.find_element(By.XPATH,"((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[5])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH,"((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[6])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH,"((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[7])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH,"((//*[@class='MuiBox-root css-1fpff4c']/table)[3]/tbody/tr/descendant::td[8])[" + str(r) + "]").text
            t_Domain.append(Domain)
            t_pubilc.append(pubilc)
            t_Country.append(Country)
            t_State.append(state)
            t_City.append(city)
            t_received.append(received)
            t_transmitted.append(transmitted)
            t_total.append(total)
        print(t_Domain)
        print(t_pubilc)
        print(t_Country)
        print(t_State)
        print(t_City)
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
                print("domain:", t_Domain[i])
                print("public:", t_pubilc[i])
                print("Received:", r_sizes_in_bytes[i])
                print("Transmitted:", tr_sizes_in_bytes[i])
                print("total data:", to_sizes_in_bytes[i])
                total_tr =  r_sizes_in_bytes[i] + tr_sizes_in_bytes[i]
                print("the sum of received and transmitted data",total_tr)
                if total_tr == to_sizes_in_bytes[i]:
                    print("Total data meets the condition")
                else:
                    print("Total data does not meet the condition")






    def total_table_data_for_each_single_row(self):
        row = self.driver.find_elements(By.XPATH, "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr")
        print(len(row))
        t_Internal = []
        t_External = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(1, len(row) + 1):
            Internal = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[1])[" + str(r) + "]").text
            External = self.driver.find_element(By.XPATH, "(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[2])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5])[" + str(r) + "]").text
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


    def city_wise_traffic_table_data(self):
        data = self.driver.find_element(By.XPATH, self.city_wise_traffic_table_xpath).text
        print(data)
        # for element in data:
        #     text_content = element.text
        #     print(text_content)
        # print("city wise traffic :", text_content)

        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "city_wise_traffic_table.png")
        self.driver.save_screenshot(screenshot_path)

    def summary_table_data(self):
        row = self.driver.find_elements(By.XPATH, "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//th")
        columns = len(column)
        for r in range(1, rows + 1):
            for c in range(1, columns + 1):
                if r == 1:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr[" + str(r) + "]//th[" + str(c) + "]")
                    print(data.text, end='       ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr[" + str(r - 1) + "]//td[" + str(c) + "]")
                    print(data.text, end='    ')
            print()




        # tbody =self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table/tbody")
        # data= []
        # for tr in tbody.find_elements(By.XPATH, "//tr"):
        #     row =[item.text for item in tr.find_elements(By.XPATH, ".//td")]
        #     data.append(row)
        #     # print(data, end='')
        #     output_text = ['\t'.join(map(str, sublist)) for sublist in data]
        #
        #     # Write the output to a temporary text file
        #     with open('geo_output.txt', 'w') as file:
        #         file.write('\n'.join(output_text))
        #
        #     subprocess.Popen(['notepad.exe', 'geo_output.txt'])


    def verify_apps_table_data(self):
        data = self.driver.find_elements(By.XPATH, self.apps_table_total_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5])[" + str(i) + "]").text
            l.append(s)
        sizes = l
        converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    converted_sizes.append(float(value))
                elif unit == 'MB':
                    converted_sizes.append(float(value) * 1024)
            else:
                print("total data:", size)
        print(converted_sizes)
        total_data = sum(converted_sizes)
        print("total data:", total_data)

        data = self.driver.find_elements(By.XPATH, self.apps_table_received_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3])[" + str(i) + "]").text
            l.append(s)
        sizes = l
        converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    converted_sizes.append(float(value))
                elif unit == 'MB':
                    converted_sizes.append(float(value) * 1024)
            else:
                print("received data:", size)
        print(converted_sizes)
        received_data = sum(converted_sizes)
        print("received data:",received_data)

        data = self.driver.find_elements(By.XPATH, self.apps_table_transmitted_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4])[" + str(i) + "]").text
            l.append(s)
        sizes = l
        converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    converted_sizes.append(float(value))
                elif unit == 'MB':
                    converted_sizes.append(float(value) * 1024)
            else:
                print("transmitted data:", size)
        print(converted_sizes)
        transmitted_data = sum(converted_sizes)
        print("transmitted data:",transmitted_data)

        total = received_data + transmitted_data
        print("received and transmitted data:",total)
        if total==total_data:
            print("total data matched")
        else:
            print("not matched")

        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "summary_apps_table.png")
        self.driver.save_screenshot(screenshot_path)



    def verify_external_communication_table_data(self):
        data = self.driver.find_elements(By.XPATH, self.external_communication_table_total_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5])[" + str(i) + "]").text
            l.append(s)
        sizes = l
        converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    converted_sizes.append(float(value))
                elif unit == 'MB':
                    converted_sizes.append(float(value) * 1024)
            else:
                print("total data:", size)
        print(converted_sizes)
        total_data = sum(converted_sizes)
        print("total data:", total_data)

        data = self.driver.find_elements(By.XPATH, self.external_communication_table_received_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3])[" + str(i) + "]").text
            l.append(s)
        sizes = l
        converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    converted_sizes.append(float(value))
                elif unit == 'MB':
                    converted_sizes.append(float(value) * 1024)
            else:
                print("received data:", size)
        print(converted_sizes)
        received_data = sum(converted_sizes)
        print("received data:",received_data)

        data = self.driver.find_elements(By.XPATH, self.external_communication_table_transmitted_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4])[" + str(i) + "]").text
            l.append(s)
        sizes = l
        converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    converted_sizes.append(float(value))
                elif unit == 'MB':
                    converted_sizes.append(float(value) * 1024)
            else:
                print("transmitted data:", size)
        print(converted_sizes)
        transmitted_data = sum(converted_sizes)
        print("transmitted data:",transmitted_data)

        total = received_data + transmitted_data
        print("received and transmitted data:",total)
        if total==total_data:
            print("total data matched")
        else:
            print("not matched")

        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "external_communication_table.png")
        self.driver.save_screenshot(screenshot_path)

    def verify_table_title(self):
        return self.driver.find_element(By.XPATH, self.summary_table_title_xpath).text

    def table_title(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        print("title of the table:", title)
        title_head = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/thead)[1]").text
        print(title_head)

    def summary_table_dat(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end=' ')


    def submit_button(self):
        self.driver.find_element(By.XPATH, self.submit_button_xpath).click()

    def public_ip_dropdown_button(self):
        self.driver.find_element(By.XPATH, self.public_ip_dropdown_button_xpath).click()

    def public_ip_list(self):
        list = self.driver.find_elements(By.XPATH, self.public_ip_list_xpath)
        for ele in list:
            if ele.text == "154.83.3.29":
                ele.click()
                break
    def from_date(self):
        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[3]")
        element.click()
        mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        while True:
            if mon_yy == "April 2024":
                break
            else:
                self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
        dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
        for ele in dates:
            if ele.text == "11":
                ele.click()
                break

        hour = self.driver.find_element(By.XPATH, "(//span[contains(@data-index,'0')])[1]")
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(hour, 100, 0).perform()

        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[3]")
        element.click()
        time.sleep(2)
        minute = self.driver.find_element(By.XPATH, "(//span[contains(@data-index,'0')])[2]")
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(minute, 100, 0).perform()


    def to_date(self):
        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[4]")
        element.click()
        mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        while True:
            if mon_yy == "April 2024":
                break
            else:
                self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
        dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
        for ele in dates:
            if ele.text == "18":
                ele.click()
                break

        hour = self.driver.find_element(By.XPATH, "(//span[contains(@data-index,'0')])[1]")
        actions = ActionChains(self.driver)
        # for i in range(100, 0, -1):
        #     actions.drag_and_drop_by_offset(hour, -i, 0).perform()
        actions.drag_and_drop_by_offset(hour, 100, 0).perform()
        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[4]")
        element.click()
        time.sleep(2)
        minute = self.driver.find_element(By.XPATH, "(//span[contains(@data-index,'0')])[2]")
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(minute, 100, 0).perform()



    def verify_summary_page(self):
        return self.driver.find_element(By.XPATH, self.verify_summary_page_xpath).text
    def verify_report_button(self):
        return self.driver.find_element(By.XPATH, self.verify_reports_page).text

    def report_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()

    def summary_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ip_tracking_page_xpath)))
        element.click()

























# import os
# import time
#
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# class SummaryReport:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
#     verify_reports_page = "//*[text()='Reports']"
#     ip_tracking_page_xpath = "//*[text()='Summary Report']"
#     verify_summary_page_xpath = "(//div[contains(@class,'MuiBox-root css-1c1kq07')])[1]"
#
#     public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
#     public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
#     submit_button_xpath = "//button[text()='Submit']"
#
#     table_title_xpath = "//div[contains(@class,'MuiBox-root css-1c1kq07')]"
#
#     external_communication_table_received_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3]"
#     external_communication_table_transmitted_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4]"
#     external_communication_table_total_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5]"
#
#     apps_table_received_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[4])"
#     apps_table_transmitted_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[5])"
#     apps_table_total_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[6])"
#
#     city_wise_traffic_table_xpath = "//*[contains(@class,'MuiBox-root css-14w0bz')]/div"
#     # city_wise_traffic_table_xpath = "//p[text()='No Data']"
#
#     def city_wise_traffic_table_data(self):
#         data = self.driver.find_element(By.XPATH, self.city_wise_traffic_table_xpath).text
#         print(data)
#         # for element in data:
#         #     text_content = element.text
#         #     print(text_content)
#         # print("city wise traffic :", text_content)
#
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "city_wise_traffic_table.png")
#         self.driver.save_screenshot(screenshot_path)
#
#     def verify_apps_table_data(self):
#         data = self.driver.find_elements(By.XPATH, self.apps_table_total_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5])[" + str(i) + "]").text
#             l.append(s)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     converted_sizes.append(float(value) * 1024)
#             else:
#                 print("total data:", size)
#         print(converted_sizes)
#         total_data = sum(converted_sizes)
#         print("total data:", total_data)
#
#         data = self.driver.find_elements(By.XPATH, self.apps_table_received_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3])[" + str(i) + "]").text
#             l.append(s)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     converted_sizes.append(float(value) * 1024)
#             else:
#                 print("received data:", size)
#         print(converted_sizes)
#         received_data = sum(converted_sizes)
#         print("received data:",received_data)
#
#         data = self.driver.find_elements(By.XPATH, self.apps_table_transmitted_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4])[" + str(i) + "]").text
#             l.append(s)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     converted_sizes.append(float(value) * 1024)
#             else:
#                 print("transmitted data:", size)
#         print(converted_sizes)
#         transmitted_data = sum(converted_sizes)
#         print("transmitted data:",transmitted_data)
#
#         total = received_data + transmitted_data
#         print("received and transmitted data:",total)
#         if total==total_data:
#             print("total data matched")
#         else:
#             print("not matched")
#
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "summary_apps_table.png")
#         self.driver.save_screenshot(screenshot_path)
#
#
#
#     def verify_external_communication_table_data(self):
#         data = self.driver.find_elements(By.XPATH, self.external_communication_table_total_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5])[" + str(i) + "]").text
#             l.append(s)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     converted_sizes.append(float(value) * 1024)
#             else:
#                 print("total data:", size)
#         print(converted_sizes)
#         total_data = sum(converted_sizes)
#         print("total data:", total_data)
#
#         data = self.driver.find_elements(By.XPATH, self.external_communication_table_received_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3])[" + str(i) + "]").text
#             l.append(s)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     converted_sizes.append(float(value) * 1024)
#             else:
#                 print("received data:", size)
#         print(converted_sizes)
#         received_data = sum(converted_sizes)
#         print("received data:",received_data)
#
#         data = self.driver.find_elements(By.XPATH, self.external_communication_table_transmitted_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4])[" + str(i) + "]").text
#             l.append(s)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     converted_sizes.append(float(value) * 1024)
#             else:
#                 print("transmitted data:", size)
#         print(converted_sizes)
#         transmitted_data = sum(converted_sizes)
#         print("transmitted data:",transmitted_data)
#
#         total = received_data + transmitted_data
#         print("received and transmitted data:",total)
#         if total==total_data:
#             print("total data matched")
#         else:
#             print("not matched")
#
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "external_communication_table.png")
#         self.driver.save_screenshot(screenshot_path)
#
#     def table_title(self):
#         title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
#         print("title of the table:", title)
#         title_head = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/thead)[1]").text
#         print(title_head)
#
#     def summary_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
#             data.append(row)
#         print(data, end=' ')
#
#
#     def submit_button(self):
#         self.driver.find_element(By.XPATH, self.submit_button_xpath).click()
#
#     def public_ip_dropdown_button(self):
#         self.driver.find_element(By.XPATH, self.public_ip_dropdown_button_xpath).click()
#
#     def public_ip_list(self):
#         list = self.driver.find_elements(By.XPATH, self.public_ip_list_xpath)
#         for ele in list:
#             if ele.text == "103.174.106.87":
#                 ele.click()
#                 break
#     def from_date(self):
#         element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[3]")
#         element.click()
#         mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
#         print(mon_yy)
#         while True:
#             if mon_yy == "April 2024":
#                 break
#             else:
#                 self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
#         dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
#         print(len(dates))
#         for ele in dates:
#             print(ele.text)
#             if ele.text == "1":
#                 ele.click()
#                 break
#
#
#     def to_date(self):
#         element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[4]")
#         element.click()
#         mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
#         print(mon_yy)
#         while True:
#             if mon_yy == "April 2024":
#                 break
#             else:
#                 self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
#         dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
#         print(len(dates))
#         for ele in dates:
#             print(ele.text)
#             if ele.text == "2":
#                 ele.click()
#                 break
#
#
#
#
#     def verify_summary_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_summary_page_xpath).text
#     def verify_report_button(self):
#         return self.driver.find_element(By.XPATH, self.verify_reports_page).text
#
#     def report_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#
#     def summary_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#         time.sleep(5)
#
#         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ip_tracking_page_xpath)))
#         element.click()
