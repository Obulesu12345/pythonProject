import subprocess
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class Iptracking:

    def __init__(self,driver):
        self.driver = driver

    report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
    verify_reports_page = "//*[text()='Reports']"
    ip_tracking_page_xpath = "//*[text()='IP Tracking']"
    verify_ip_tracking_page_xpath = "//*[@class='MuiBox-root css-1c1kq07']"

    public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
    public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
    submit_button_xpath = "//button[text()='Submit']"

    received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])"
    transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])"
    total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])"

    table_title_xpath = "//div[contains(@class,'MuiBox-root css-1c1kq07')]"

    csv_xpath = "//label[contains(@aria-label,'csv')]"

    verify_otp_for_csv_xpath = "//*[text()='Downloading CSV...']"

    def verify_otp_for_csv(self):
        return self.driver.find_element(By.XPATH, self.verify_otp_for_csv_xpath).text

    def csv(self):
        self.driver.find_element(By.XPATH, self.csv_xpath).click()

    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)


    def verify_data(self):
        data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
        l = []
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
            l.append(s)
        str1 = " ".join(l)
        words = str1.split(" ")
        numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
        # print(numbers)
        # print(l)
        sizes = l
        converted_sizes = []
        for size in sizes:
            value, unit = size.split()
            if unit == 'Bytes':
                converted_sizes.append(float(value) / 1024)
            elif unit == 'KB':
                converted_sizes.append(float(value))
            elif unit == 'MB':
                converted_sizes.append(float(value) * 1024)

        # print(converted_sizes)
        total_data = sum(converted_sizes)
        print("total data:", total_data)

        data = self.driver.find_elements(By.XPATH, self.transmitted_data_xpath)
        l = []
        # a = self.driver.find_element(By.XPATH, self.transmitted_data_xpath).text
        # print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
            l.append(s)
        str1 = " ".join(l)
        words = str1.split(" ")
        numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
        # print(numbers)
        # print(l)
        sizes = l
        converted_sizes = []
        for size in sizes:
            value, unit = size.split()
            if unit == 'Bytes':
                converted_sizes.append(float(value) / 1024)
            elif unit == 'KB':
                converted_sizes.append(float(value))
            elif unit == 'MB':
                converted_sizes.append(float(value) * 1024)
        # print(converted_sizes)
        transmitted_data = sum(converted_sizes)
        print("transmitted data:", transmitted_data)

        data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
        l = []
        # a = self.driver.find_element(By.XPATH, self.received_data_xpath).text
        # print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])[" + str(i) + "]").text
            l.append(s)
        str1 = " ".join(l)
        words = str1.split(" ")
        numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
        # print(numbers)
        # print(l)
        sizes = l
        converted_sizes = []
        for size in sizes:
            value, unit = size.split()
            if unit == 'Bytes':
                converted_sizes.append(float(value) / 1024)
            elif unit == 'KB':
                converted_sizes.append(float(value))
            elif unit == 'MB':
                converted_sizes.append(float(value) * 1024)
        # print(converted_sizes)
        received_data = sum(converted_sizes)
        print("received data:", received_data)

        total = received_data + transmitted_data
        print("received and transmitted data total:", total)

        if total==total_data:
            print("total data matched")
        else:
            print("not matched")

    def ip_tracking_table_total_data(self):
        data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
        l = []
        a = self.driver.find_element(By.XPATH, self.total_data_xpath).text
        print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
            l.append(s)
        str1 = " ".join(l)
        words = str1.split(" ")
        numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
        print(numbers)
        print(l)
        sizes = l
        converted_sizes = []
        for size in sizes:
            value, unit = size.split()
            if unit == 'Bytes':
                converted_sizes.append(float(value) / 1024)
            elif unit == 'KB':
                converted_sizes.append(float(value))
            elif unit == 'MB':
                converted_sizes.append(float(value) * 1024)
        print(converted_sizes)
        print(sum(converted_sizes))

    def ip_tracking_table_transmitted_data(self):
        data = self.driver.find_elements(By.XPATH, self.transmitted_data_xpath)
        l = []
        a = self.driver.find_element(By.XPATH, self.transmitted_data_xpath).text
        print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
            l.append(s)
        str1 = " ".join(l)
        words = str1.split(" ")
        numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
        print(numbers)
        print(l)
        sizes = l
        converted_sizes = []
        for size in sizes:
            value, unit = size.split()
            if unit == 'Bytes':
                converted_sizes.append(float(value) / 1024)
            elif unit == 'KB':
                converted_sizes.append(float(value))
            elif unit == 'MB':
                converted_sizes.append(float(value) * 1024)
        print(converted_sizes)
        print(sum(converted_sizes))
        print("success")

    def ip_tracking_table_received_data(self):
        data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
        l = []
        a = self.driver.find_element(By.XPATH, self.received_data_xpath).text
        print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])[" + str(i) + "]").text
            l.append(s)
        str1 = " ".join(l)
        words = str1.split(" ")
        numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
        print(numbers)
        print(l)
        sizes = l
        converted_sizes = []
        for size in sizes:
            value, unit = size.split()
            if unit == 'Bytes':
                converted_sizes.append(float(value) / 1024)
            elif unit == 'KB':
                converted_sizes.append(float(value))
            elif unit == 'MB':
                converted_sizes.append(float(value) * 1024)

        print(converted_sizes)
        print(sum(converted_sizes))

        # print(sum(numbers))
        print("success")



    def ip_tracking_table_data(self):
        # tbody =self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table/tbody")
        # data= []
        # for tr in tbody.find_elements(By.XPATH, "//tr"):
        #     row =[item.text for item in tr.find_elements(By.XPATH, ".//td")]
        #     data.append(row)
        #     # print(data, end='')
        #     output_text = ['\t'.join(map(str, sublist)) for sublist in data]
        #
        #     # Write the output to a temporary text file
        #     with open('ip_output.txt', 'w') as file:
        #         file.write('\n'.join(output_text))
        #
        #     subprocess.Popen(['notepad.exe', 'ip_output.txt'])

        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr")
        rows = len(row)
        column = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//th")
        columns = len(column)
        for r in range(1, rows+1):
            for c in range(1, columns+1):
                if r == 1:
                    data =self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r)+"]//th["+str(c)+"]")
                    print(data.text, end='       ')
                else:
                    data = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tr["+str(r-1)+"]//td["+str(c)+"]")
                    print(data.text, end='    ')
            print()


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


    def verify_ip_tracking_page(self):
        return self.driver.find_element(By.XPATH, self.verify_ip_tracking_page_xpath).text

    def verify_report_button(self):
        return self.driver.find_element(By.XPATH, self.verify_reports_page).text

    def report_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()

    def iptracking_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ip_tracking_page_xpath)))
        element.click()

    def table_title(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        print("title of the table:", title)

    def table_title_data(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        print("title of the table:", title)
        title_head = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/thead)[1]").text
        print(title_head)


    def total_table_data_for_single_row(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tbody/tr")
        print(len(row))
        t_internal = []
        t_external = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(1, len(row) + 1):
            internal_ip = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[1])[" + str(r) + "]").text
            external_ipip = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[2])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[3])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[4])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH,"(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[5])[" + str(r) + "]").text
            t_internal.append(internal_ip)
            t_external.append(external_ipip)
            t_received.append(received)
            t_transmitted.append(transmitted)
            t_total.append(total)
        print(t_internal)
        print(t_external)
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
                print("Received:", r_sizes_in_bytes[i])
                print("Transmitted:", tr_sizes_in_bytes[i])
                print("total data:", to_sizes_in_bytes[i])
                total_tr =  r_sizes_in_bytes[i] + tr_sizes_in_bytes[i]
                print("Total matches the sum of received and transmitted data",total_tr)
                if total_tr == to_sizes_in_bytes[i]:
                    print("Total data meets the condition")
                else:
                    print("Total data does not meet the condition")



















































        # data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
        # r = []
        # t = []
        # t_data = []
        # # for i in range(1, len(data) + 1):
        # received = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[3])").text
        # transmitted = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[4])").text
        # total = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[5])").text
        #     # s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
        # r.append(received)
        # t.append(transmitted)
        # t_data.append(total)
        # print(r)
        # print(t)
        # print(t_data)
        #
        # sizes = r
        # r_converted_sizes = []
        # for size in sizes:
        #     parts = size.split()
        #     if len(parts) == 2:
        #         value, unit = parts
        #         if unit == 'Bytes':
        #             r_converted_sizes.append(float(value) / 1024)
        #         elif unit == 'KB':
        #             r_converted_sizes.append(float(value))
        #         elif unit == 'MB':
        #             r_converted_sizes.append(float(value) * 1024)
        #         elif unit == "GB":
        #             r_converted_sizes.append(float(value) * 1024 * 1024 * 1024)
        #     else:
        #         print("received data:", size)
        # print(r_converted_sizes)
        # received_data = r_converted_sizes
        #
        # sizes= t
        # t_converted_sizes = []
        # for size in sizes:
        #     parts = size.split()
        #     if len(parts) == 2:
        #         value, unit = parts
        #         if unit == 'Bytes':
        #             t_converted_sizes.append(float(value) / 1024)
        #         elif unit == 'KB':
        #             t_converted_sizes.append(float(value))
        #         elif unit == 'MB':
        #             t_converted_sizes.append(float(value) * 1024)
        #         elif unit == "GB":
        #             t_converted_sizes.append(float(value) * 1024 * 1024 * 1024)
        #     else:
        #         print("transmitt data:", size)
        # print(t_converted_sizes)
        # transmitt_data = t_converted_sizes
        #
        #
        # sizes = t_data
        # converted_sizes = []
        # for size in sizes:
        #     parts = size.split()
        #     if len(parts) == 2:
        #         value, unit = parts
        #         if unit == 'Bytes':
        #             converted_sizes.append(float(value) / 1024)
        #         elif unit == 'KB':
        #             converted_sizes.append(float(value))
        #         elif unit == 'MB':
        #             converted_sizes.append(float(value) * 1024)
        #         elif unit == "GB":
        #             converted_sizes.append(float(value) * 1024 * 1024 * 1024)
        #     else:
        #         print("total data:", size)
        # print(converted_sizes)
        # total_data = converted_sizes
        # print("total data:", total_data)
        #
        # total = sum(received_data + transmitt_data)
        # print("total received and transmitted data:",total)
        # if total_data == total:
        #     print("Total data meets the condition")
        # else:
        #     print("Total data does not meet the condition")




























# import time
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# class Iptracking:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
#     verify_reports_page = "//*[text()='Reports']"
#     ip_tracking_page_xpath = "//*[text()='IP Tracking']"
#     verify_ip_tracking_page_xpath = "//*[@class='MuiBox-root css-1c1kq07']"
#
#     public_ip_dropdown_button_xpath = "//select[contains(@aria-invalid,'false')]"
#     public_ip_list_xpath = "(//select[contains(@aria-invalid,'false')])/option"
#     submit_button_xpath = "//button[text()='Submit']"
#
#     received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])"
#     transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])"
#     total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])"
#
#
#     def verify_data(self):
#         data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
#         l = []
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         # print(numbers)
#         # print(l)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             value, unit = size.split()
#             if unit == 'Bytes':
#                 converted_sizes.append(float(value) / 1024)
#             elif unit == 'KB':
#                 converted_sizes.append(float(value))
#             elif unit == 'MB':
#                 converted_sizes.append(float(value) * 1024)
#
#         # print(converted_sizes)
#         total_data = sum(converted_sizes)
#         print("total data:", total_data)
#
#         data = self.driver.find_elements(By.XPATH, self.transmitted_data_xpath)
#         l = []
#         # a = self.driver.find_element(By.XPATH, self.transmitted_data_xpath).text
#         # print(a)
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         # print(numbers)
#         # print(l)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             value, unit = size.split()
#             if unit == 'Bytes':
#                 converted_sizes.append(float(value) / 1024)
#             elif unit == 'KB':
#                 converted_sizes.append(float(value))
#             elif unit == 'MB':
#                 converted_sizes.append(float(value) * 1024)
#         # print(converted_sizes)
#         transmitted_data = sum(converted_sizes)
#         print("transmitted data:", transmitted_data)
#
#         data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
#         l = []
#         # a = self.driver.find_element(By.XPATH, self.received_data_xpath).text
#         # print(a)
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         # print(numbers)
#         # print(l)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             value, unit = size.split()
#             if unit == 'Bytes':
#                 converted_sizes.append(float(value) / 1024)
#             elif unit == 'KB':
#                 converted_sizes.append(float(value))
#             elif unit == 'MB':
#                 converted_sizes.append(float(value) * 1024)
#         # print(converted_sizes)
#         received_data = sum(converted_sizes)
#         print("received data:", received_data)
#
#         total = received_data + transmitted_data
#         print("received and transmitted data total:", total)
#
#         if total==total_data:
#             print("total data matched")
#         else:
#             print("not matched")
#
#     def ip_tracking_table_total_data(self):
#         data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
#         l = []
#         a = self.driver.find_element(By.XPATH, self.total_data_xpath).text
#         print(a)
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         print(numbers)
#         print(l)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             value, unit = size.split()
#             if unit == 'Bytes':
#                 converted_sizes.append(float(value) / 1024)
#             elif unit == 'KB':
#                 converted_sizes.append(float(value))
#             elif unit == 'MB':
#                 converted_sizes.append(float(value) * 1024)
#         print(converted_sizes)
#         print(sum(converted_sizes))
#
#     def ip_tracking_table_transmitted_data(self):
#         data = self.driver.find_elements(By.XPATH, self.transmitted_data_xpath)
#         l = []
#         a = self.driver.find_element(By.XPATH, self.transmitted_data_xpath).text
#         print(a)
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         print(numbers)
#         print(l)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             value, unit = size.split()
#             if unit == 'Bytes':
#                 converted_sizes.append(float(value) / 1024)
#             elif unit == 'KB':
#                 converted_sizes.append(float(value))
#             elif unit == 'MB':
#                 converted_sizes.append(float(value) * 1024)
#         print(converted_sizes)
#         print(sum(converted_sizes))
#         print("success")
#
#     def ip_tracking_table_received_data(self):
#         data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
#         l = []
#         a = self.driver.find_element(By.XPATH, self.received_data_xpath).text
#         print(a)
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         print(numbers)
#         print(l)
#         sizes = l
#         converted_sizes = []
#         for size in sizes:
#             value, unit = size.split()
#             if unit == 'Bytes':
#                 converted_sizes.append(float(value) / 1024)
#             elif unit == 'KB':
#                 converted_sizes.append(float(value))
#             elif unit == 'MB':
#                 converted_sizes.append(float(value) * 1024)
#
#         print(converted_sizes)
#         print(sum(converted_sizes))
#
#         # print(sum(numbers))
#         print("success")
#
#
#
#     def ip_tracking_table_data(self):
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
#     def verify_ip_tracking_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_ip_tracking_page_xpath).text
#
#     def verify_report_button(self):
#         return self.driver.find_element(By.XPATH, self.verify_reports_page).text
#
#     def report_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#
#     def iptracking_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#         time.sleep(5)
#
#         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ip_tracking_page_xpath)))
#         element.click()
#
#
#
#     def total_table_data_for_single_row(self):
#         # data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
#         r = []
#         t = []
#         t_data = []
#         # for i in range(1, len(data) + 1):
#         received = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[3])").text
#         transmitted = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[4])").text
#         total = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[5])").text
#             # s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
#         r.append(received)
#         t.append(transmitted)
#         t_data.append(total)
#         print(r)
#         print(t)
#         print(t_data)
#
#         sizes = r
#         r_converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     r_converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     r_converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     r_converted_sizes.append(float(value) * 1024)
#                 elif unit == "GB":
#                     r_converted_sizes.append(float(value) * 1024 * 1024 * 1024)
#             else:
#                 print("received data:", size)
#         print(r_converted_sizes)
#         received_data = r_converted_sizes
#
#         sizes= t
#         t_converted_sizes = []
#         for size in sizes:
#             parts = size.split()
#             if len(parts) == 2:
#                 value, unit = parts
#                 if unit == 'Bytes':
#                     t_converted_sizes.append(float(value) / 1024)
#                 elif unit == 'KB':
#                     t_converted_sizes.append(float(value))
#                 elif unit == 'MB':
#                     t_converted_sizes.append(float(value) * 1024)
#                 elif unit == "GB":
#                     t_converted_sizes.append(float(value) * 1024 * 1024 * 1024)
#             else:
#                 print("transmitt data:", size)
#         print(t_converted_sizes)
#         transmitt_data = t_converted_sizes
#
#
#         sizes = t_data
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
#                 elif unit == "GB":
#                     converted_sizes.append(float(value) * 1024 * 1024 * 1024)
#             else:
#                 print("total data:", size)
#         print(converted_sizes)
#         total_data = converted_sizes
#         print("total data:", total_data)
#
#         total = sum(received_data + transmitt_data)
#         print("total received and transmitted data:",total)
#         if total_data == total:
#             print("Total data meets the condition")
#         else:
#             print("Total data does not meet the condition")