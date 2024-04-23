import os
import subprocess
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GeoTraffic:

    def __init__(self,driver):
        self.driver = driver

    verify_reports_page = "//*[text()='Reports']"
    report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
    geo_traffic_page_xpath = "//*[text()='Geo Traffic']"
    verify_geo_traffic_page_xpath = "//label[text()='Public IP']"

    public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
    public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
    submit_button_xpath = "//button[text()='Submit']"

    location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"

    received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])"
    transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])"
    total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])"

    table_title_xpath = "//div[contains(@class,'MuiBox-root css-1c1kq07')]"

    rows_per_page_xpath = "(//div[contains(@role,'button')])[2]"
    rows_per_page_dropdown_xpath = "(//ul[contains(@role,'listbox')])/li"
    alert_otp_msg_xpath = "//div[contains(@role,'alert')]"
    csv_xpath = "//label[contains(@aria-label,'csv')]"

    def alert_otp_msg(self):
        return self.driver.find_element(By.XPATH, self.alert_otp_msg_xpath).text

    def csv(self):
        self.driver.find_element(By.XPATH, self.csv_xpath).click()
    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)


    def rows_per_page(self):
        self.driver.find_element(By.XPATH, self.rows_per_page_xpath).click()

    def rows_per_page_dropdown(self):
        list = self.driver.find_elements(By.XPATH, self.rows_per_page_dropdown_xpath)
        for i in list:
            if i.text == '100':
                i.click()
                break

    def table_title(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        print("title of the table:", title)
        title_head = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/thead)[1]").text
        print(title_head)

    def geo_traffic_table_data(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr")
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

    def ip_tracking_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end='  ')

    def verify_data(self):
        data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
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

        data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])[" + str(i) + "]").text
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

        data = self.driver.find_elements(By.XPATH, self.transmitted_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])[" + str(i) + "]").text
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
        print("verify total data:",total)
        if total==total_data:
            print("total data matched")
        else:
            print("not matched")
        current_url = self.driver.current_url
        print(current_url)
        folder_path = "screenshots"
        screenshot_path = os.path.join(folder_path, "verify_geotraffice_table.png")
        self.driver.save_screenshot(screenshot_path)










    def location(self):
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def location_dropdown(self):

        element = self.driver.find_element(By.XPATH, self.dropdown_elements_xpath)
        element.click()


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
            if ele.text == "1":
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
            if ele.text == "5":
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

    def verify_geo_traffic_page(self):
        return self.driver.find_element(By.XPATH, self.verify_geo_traffic_page_xpath).text

    def verify_report_button(self):
        return self.driver.find_element(By.XPATH, self.verify_reports_page).text

    def report_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()

    def topapps_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.geo_traffic_page_xpath)))
        element.click()


    def total_table_data_for_single_row(self):
        r = []
        t = []
        t_data = []
        received = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[6])").text
        transmitted = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[7])").text
        total = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[8])").text
        r.append(received)
        t.append(transmitted)
        t_data.append(total)
        print(r)
        print(t)
        print(t_data)

        sizes = r
        r_converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    r_converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    r_converted_sizes.append(float(value))
                elif unit == 'MB':
                    r_converted_sizes.append(float(value) * 1024)
                elif unit == "GB":
                    r_converted_sizes.append(float(value) * 1024 * 1024 * 1024)
            else:
                print("received data:", size)
        print(r_converted_sizes)
        received_data = r_converted_sizes

        sizes= t
        t_converted_sizes = []
        for size in sizes:
            parts = size.split()
            if len(parts) == 2:
                value, unit = parts
                if unit == 'Bytes':
                    t_converted_sizes.append(float(value) / 1024)
                elif unit == 'KB':
                    t_converted_sizes.append(float(value))
                elif unit == 'MB':
                    t_converted_sizes.append(float(value) * 1024)
                elif unit == "GB":
                    t_converted_sizes.append(float(value) * 1024 * 1024 * 1024)
            else:
                print("transmitt data:", size)
        print(t_converted_sizes)
        transmitt_data = t_converted_sizes


        sizes = t_data
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
                elif unit == "GB":
                    converted_sizes.append(float(value) * 1024 * 1024 * 1024)
            else:
                print("total data:", size)
        print(converted_sizes)
        total_data = converted_sizes
        print("total data:", total_data)

        total = sum(received_data + transmitt_data)
        print("total received and transmitted data:",total)
        if total_data == total:
            print("Total data meets the condition")
        else:
            print("Total data does not meet the condition")




    def total_table_data_for_each_single_row(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tbody/tr")
        print(len(row))
        t_Domain = []
        t_Public_IP = []
        t_Country = []
        t_State = []
        t_City = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(1, len(row) + 1):
            Domain = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[1])[" + str(r) + "]").text
            Public_IP = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[2])[" + str(r) + "]").text
            Country = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[3])[" + str(r) + "]").text
            State = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[4])[" + str(r) + "]").text
            City = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[5])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[6])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[7])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[8])[" + str(r) + "]").text
            t_Domain.append(Domain)
            t_Public_IP.append(Public_IP)
            t_Country.append(Country)
            t_State.append(State)
            t_City.append(City)
            t_received.append(received)
            t_transmitted.append(transmitted)
            t_total.append(total)
        print(t_Domain)
        print(t_Public_IP)
        print(t_Country)
        print()
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
                print("domain address:", t_Domain[i])
                print("Public ip address:", t_Public_IP[i])
                print("Received:", r_sizes_in_bytes[i])
                print("Transmitted:", tr_sizes_in_bytes[i])
                print("total data:", to_sizes_in_bytes[i])
                total_tr =  r_sizes_in_bytes[i] + tr_sizes_in_bytes[i]
                print("the sum of received and transmitted data",total_tr)
                if total_tr == to_sizes_in_bytes[i]:
                    print("Total data meets the condition")
                else:
                    print("Total data does not meet the condition")





















# import os
# import time
#
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# class GeoTraffic:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     verify_reports_page = "//*[text()='Reports']"
#     report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
#     geo_traffic_page_xpath = "//*[text()='Geo Traffic']"
#     verify_geo_traffic_page_xpath = "//*[contains(@class,'MuiBox-root css-1c1kq07')]/p"
#
#     public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
#     public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
#     submit_button_xpath = "//button[text()='Submit']"
#
#     location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
#     dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"
#
#     received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])"
#     transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])"
#     total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])"
#
#     table_title_xpath = "//div[contains(@class,'MuiBox-root css-1c1kq07')]"
#
#     rows_per_page_xpath = "(//div[contains(@role,'button')])[2]"
#     rows_per_page_dropdown_xpath = "(//ul[contains(@role,'listbox')])/li"
#
#
#     def rows_per_page(self):
#         self.driver.find_element(By.XPATH, self.rows_per_page_xpath).click()
#
#     def rows_per_page_dropdown(self):
#         list = self.driver.find_elements(By.XPATH, self.rows_per_page_dropdown_xpath)
#         print(list)
#         for i in list:
#             if i.text == '100':
#                 i.click()
#                 break
#
#     def table_title(self):
#         title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
#         print("title of the table:", title)
#
#     def summary_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
#             data.append(row)
#         print(data, end=' ')
#
#     def ip_tracking_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
#             data.append(row)
#         print(data, end=' ')
#
#     def verify_data(self):
#         data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[8])[" + str(i) + "]").text
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
#         data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])[" + str(i) + "]").text
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
#         data = self.driver.find_elements(By.XPATH, self.transmitted_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[7])[" + str(i) + "]").text
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
#         total = received_data + transmitted_data
#         print("verify total data:",total)
#         if total==total_data:
#             print("total data matched")
#         else:
#             print("not matched")
#         current_url = self.driver.current_url
#         print(current_url)
#         folder_path = "screenshots"
#         screenshot_path = os.path.join(folder_path, "verify_geotraffice_table.png")
#         self.driver.save_screenshot(screenshot_path)
#
#
#
#
#
#
#
#
#
#
#     def location(self):
#         self.driver.find_element(By.XPATH, self.location_xpath).click()
#
#     def location_dropdown(self):
#
#         element = self.driver.find_element(By.XPATH, self.dropdown_elements_xpath)
#         element.click()
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
#             if ele.text == "154.83.3.29":
#                 ele.click()
#                 break
#
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
#             if ele.text == "5":
#                 ele.click()
#                 break
#
#     def verify_geo_traffic_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_geo_traffic_page_xpath).text
#
#     def verify_report_button(self):
#         return self.driver.find_element(By.XPATH, self.verify_reports_page).text
#
#     def report_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#
#     def topapps_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#         time.sleep(5)
#
#         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.geo_traffic_page_xpath)))
#         element.click()