import os
import subprocess
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Topapps:

    def __init__(self,driver):
        self.driver = driver

    verify_reports_page = "//*[text()='Reports']"
    report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
    topapps_page_xpath = "//*[text()='Top Apps']"
    verify_apps_page_xpath = "//label[text()='From']"

    location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"

    public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
    public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
    submit_button_xpath = "//button[text()='Submit']"


    received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])"
    transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])"
    total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])"

    rows_per_page_xpath = "(//div[contains(@role,'button')])[2]"
    rows_per_page_dropdown_xpath = "(//ul[contains(@role,'listbox')])/li"

    table_title_xpath = "(//div[contains(@class,'MuiBox-root css-1c1kq07')])[1]"

    alert_otp_msg_xpath = "//div[contains(@role,'alert')]"
    csv_xpath = "//label[contains(@aria-label,'csv')]"

    def csv(self):
        self.driver.find_element(By.XPATH, self.csv_xpath).click()

    def alert_otp_msg(self):
        return self.driver.find_element(By.XPATH, self.alert_otp_msg_xpath).text
    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def table_title(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        print("title of the table:", title)
        title_head = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/thead)[1]").text
        print(title_head)


    def topapps_table_received_data(self):
        data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
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
                print("Invalid size format:", size)
        print(converted_sizes)
        print(sum(converted_sizes))
        print("success")



    def verify_data(self):
        data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
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
                print("total data:", size)
        print(converted_sizes)
        total_data = sum(converted_sizes)
        print("total data:", total_data)

        data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
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
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
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
        screenshot_path = os.path.join(folder_path, "top_apps_table.png")
        self.driver.save_screenshot(screenshot_path)


    def topapps_table_data(self):
        row = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']//tr)")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']//th)")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']//tr)["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='       ')
                else:
                    data = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']//tr)["+str(r-1)+"]//td["+str(c)+"]")
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
        #     with open('top_apps_output.txt', 'w') as file:
        #         file.write('\n'.join(output_text))
        #
        #     subprocess.Popen(['notepad.exe', 'top_apps_output.txt'])

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
        # print(mon_yy)
        while True:
            if mon_yy == "April 2024":
                break
            else:
                self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
        dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
        # print(len(dates))
        for ele in dates:
            # print(ele.text)
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
        # print(mon_yy)
        while True:
            if mon_yy == "April 2024":
                break
            else:
                self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
        dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
        # print(len(dates))
        for ele in dates:
            # print(ele.text)
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

    def verify_apps_page(self):
        return self.driver.find_element(By.XPATH, self.verify_apps_page_xpath).text

    def verify_topapps_page(self):
        return self.driver.find_element(By.XPATH, self.topapps_page_xpath).text

    def verify_report_button(self):
        return self.driver.find_element(By.XPATH, self.verify_reports_page).text

    def report_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()

    def topapps_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.topapps_page_xpath)))
        element.click()

    def location(self):
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def location_dropdown(self):
        element = self.driver.find_element(By.XPATH,self.dropdown_elements_xpath)
        element.click()

    def rows_per_page(self):
        self.driver.find_element(By.XPATH, self.rows_per_page_xpath).click()

    def rows_per_page_dropdown(self):
        list = self.driver.find_elements(By.XPATH, self.rows_per_page_dropdown_xpath)
        for i in list:
            if i.text == '100':
                i.click()
                break

    def total_table_data_for_single_row(self):
        r = []
        t = []
        t_data = []
        received = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[4])").text
        transmitted = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[5])").text
        total = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[6])").text
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
        t_app = []
        t_active = []
        t_connection = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(1, len(row) + 1):
            app = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[1])[" + str(r) + "]").text
            active_connection = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[2])[" + str(r) + "]").text
            total_connection = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[3])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[4])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[5])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[6])[" + str(r) + "]").text
            t_app.append(app)
            t_active.append(active_connection)
            t_connection.append(total_connection)
            t_received.append(received)
            t_transmitted.append(transmitted)
            t_total.append(total)
        print(t_app)
        print(t_active)
        print(t_connection)
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
                print("top app ip address:", t_app[i])
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
# class Topapps:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     verify_reports_page = "//*[text()='Reports']"
#     report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
#     topapps_page_xpath = "//*[text()='Top Apps']"
#     verify_apps_page_xpath = "//label[text()='From']"
#
#     location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
#     dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"
#
#     public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
#     public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
#     submit_button_xpath = "//button[text()='Submit']"
#
#
#     received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])"
#     transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])"
#     total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[6])"
#
#
#
#     def topapps_table_received_data(self):
#         data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
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
#                 print("Invalid size format:", size)
#         print(converted_sizes)
#         print(sum(converted_sizes))
#         print("success")
#
#
#
#     def verify_data(self):
#         data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
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
#                 print("total data:", size)
#         print(converted_sizes)
#         total_data = sum(converted_sizes)
#         print("total data:", total_data)
#
#         data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
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
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
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
#         screenshot_path = os.path.join(folder_path, "top_apps_table.png")
#         self.driver.save_screenshot(screenshot_path)
#
#
#     def topapps_table_data(self):
#         tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
#         data = []
#         for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
#             row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
#             data.append(row)
#         print(data, end=' ')
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
#
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
#             if ele.text == "3":
#                 ele.click()
#                 break
#
#
#     def verify_apps_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_apps_page_xpath).text
#
#     def verify_topapps_page(self):
#         return self.driver.find_element(By.XPATH, self.topapps_page_xpath).text
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
#         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.topapps_page_xpath)))
#         element.click()
#
#     def location(self):
#         self.driver.find_element(By.XPATH, self.location_xpath).click()
#
#     def location_dropdown(self):
#
#         element = self.driver.find_element(By.XPATH,self.dropdown_elements_xpath)
#         element.click()
