import subprocess
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

class Bandwidth:

    def __init__(self,driver):
        self.driver = driver

    report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
    bandwidth_button_xpath = "(//div[text()='Bandwidth'])"

    verify_reports_page = "//*[text()='Reports']"

    verify_bandwidth_page_xpath = "//*[text()='Bandwidth | All IP']"

    bandwidth_data_from_input_xpath = "(//input[contains(@aria-invalid,'false')])[3]"
    bandwidth_data_to_input_xpath = "(//input[contains(@aria-invalid,'false')])[4]"

    submit_button_xpath = "//button[text()='Submit']"

    received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])"
    transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])"
    total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])"

    csv_xpath = "//label[contains(@aria-label,'csv')]"

    location_xpath = "//div[@class='MuiFormControl-root css-mj41ll']"
    dropdown_elements_xpath = "//ul[@class='MuiList-root MuiList-padding MuiMenu-list css-r8u8y9']/li[1]"


    def csv(self):
        self.driver.find_element(By.XPATH, self.csv_xpath).click()

    def current_url(self):
        current_url = self.driver.current_url
        print(current_url)

    def location(self):
        self.driver.find_element(By.XPATH, self.location_xpath).click()

    def location_dropdown(self):
        # self.driver.find_element(By.XPATH, self.dropdown_elements_xpath).click()
        # element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.dropdown_elements_xpath)))
        # element.click()
        element = self.driver.find_element(By.XPATH,self.dropdown_elements_xpath)
        element.click()

    def band_width_table_data(self):
        tbody =self.driver.find_element(By.XPATH, "//div[@class='MuiBox-root css-1fpff4c']/table/")
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


    def band_table_data(self):
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

    def bandwidth_from_date(self,from_date):
        self.driver.find_element(By.XPATH, self.bandwidth_data_from_input_xpath).click()
        self.driver.find_element(By.XPATH, self.bandwidth_data_from_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.bandwidth_data_from_input_xpath).send_keys(from_date)

    def bandwidth_to_date(self,to_date):
        self.driver.find_element(By.XPATH, self.bandwidth_data_to_input_xpath).click()
        self.driver.find_element(By.XPATH, self.bandwidth_data_to_input_xpath).clear()
        self.driver.find_element(By.XPATH, self.bandwidth_data_to_input_xpath).send_keys(to_date)

    def verify_bandwidth_page(self):
        return self.driver.find_element(By.XPATH, self.verify_bandwidth_page_xpath).text

    def verify_reports(self):
        return self.driver.find_element(By.XPATH, self.verify_reports_page).text



    def report_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()
        time.sleep(5)

    def bandwidth_page(self):
        self.driver.find_element(By.XPATH, self.report_button_xpath).click()
        time.sleep(5)

        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.bandwidth_button_xpath)))
        element.click()

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
            if ele.text == "2":
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
        actions.drag_and_drop_by_offset(minute, 0, 100).perform()
        # actions.click_and_hold(before_min).move_by_offset(100, 0).release().perform()
        # actions.drag_and_drop_by_offset(before_minute, 0, offset_minutes)
        # actions.drag_and_drop_by_offset(before_sec, 0, offset_seconds)
        # actions.perform()
        # actions.click_and_hold(before_minute).move_to_element(after_minute).release().perform()

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
            if ele.text == "3":
                ele.click()
                break

        hour = self.driver.find_element(By.XPATH, "(//span[contains(@data-index,'0')])[1]")
        actions = ActionChains(self.driver)
        for i in range(100, 0, -1):
            actions.drag_and_drop_by_offset(hour, -i, 0).perform()
        # actions.drag_and_drop_by_offset(hour, 100, 0).perform()
        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[4]")
        element.click()
        time.sleep(2)
        minute = self.driver.find_element(By.XPATH, "(//span[contains(@data-index,'0')])[2]")
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(minute, 100, 0).perform()



    def bandwidth_table_received_data(self):
        data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
        l = []
        a = self.driver.find_element(By.XPATH, self.received_data_xpath).text
        print(a)
        for i in range(1, len(data) + 1):
            s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])[" + str(i) + "]").text
            l.append(s)
        str1 = " ".join(l)
        words = str1.split(" ")
        # str1 = l.split(" ")
        # b = [int(a) for a in words if a.isdigit]
        # print(b)
        numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
        print(numbers)

        print(l)

        sizes = l
        # Convert each size to GB
        sizes_in_gb = []
        for size in sizes:
            value, unit = size.split()
            value = float(value)
            if unit == 'MB':
                value /= 1024  # Convert MB to GB
            sizes_in_gb.append(value)

        print(sizes_in_gb)
        print(sum(sizes_in_gb))

        # print(sum(numbers))
        print("success")


    def bandwidth_table_transmitted_data(self):
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
        # Convert each size to GB
        sizes_in_gb = []
        for size in sizes:
            value, unit = size.split()
            value = float(value)
            if unit == 'MB':
                value /= 1024  # Convert MB to GB
            sizes_in_gb.append(value)

        print(sizes_in_gb)
        print(sum(sizes_in_gb))

        # print(sum(numbers))
        print("success")


    def bandwidth_table_total_data(self):
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
        # Convert each size to GB
        sizes_in_gb = []
        for size in sizes:
            value, unit = size.split()
            value = float(value)
            if unit == 'MB':
                value /= 1024  # Convert MB to GB
            sizes_in_gb.append(value)

        print(sizes_in_gb)
        print(sum(sizes_in_gb))

        # print(sum(numbers))
        print("success")

    def verify_the_total_table_data(self):
        data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
        r = []
        t = []
        t_data = []
        for i in range(1, len(data) + 1):
            received = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr/descendant::td[3])[" + str(i) + "]").text
            transmitted = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr/descendant::td[4])[" + str(i) + "]").text
            total = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr/descendant::td[5])[" + str(i) + "]").text
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
        received_data = sum(r_converted_sizes)
        print("received data:", received_data)

        sizes = t
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
        transmitted = sum(t_converted_sizes)
        print("transmitted data:",transmitted)

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
        total_data = sum(converted_sizes)
        print("total data:", total_data)

        total = received_data + transmitted
        print("total:", total)
        if total_data == total:
            print("Total data meets the condition")
        else:
            print("Total data does not meet the condition")



    def table_data(self):
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

    def single_row_total(self):
        row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']//tbody/tr")
        print(len(row))
        t_label = []
        t_public_ip = []
        t_received = []
        t_transmitted = []
        t_total = []
        for r in range(1, len(row) + 1):
            label = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[1])[" + str(r) + "]").text
            ip = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[2])[" + str(r) + "]").text
            received = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[3])[" + str(r) + "]").text
            transmitted = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[4])[" + str(r) + "]").text
            total = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table//descendant::td[5])[" + str(r) + "]").text
            t_label.append(label)
            t_public_ip.append(ip)
            t_received.append(received)
            t_transmitted.append(transmitted)
            t_total.append(total)
        print(t_label)
        print(t_public_ip)
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
                print("domain address:", t_label[i])
                print("Public ip address:", t_public_ip[i])
                print("Received:", r_sizes_in_bytes[i])
                print("Transmitted:", tr_sizes_in_bytes[i])
                print("total data:", to_sizes_in_bytes[i])
                total_tr =  r_sizes_in_bytes[i] + tr_sizes_in_bytes[i]
                print("the sum of received and transmitted data",total_tr)
                if total_tr == to_sizes_in_bytes[i]:
                    print("Total data meets the condition")
                else:
                    print("Total data does not meet the condition")
                # output = t_label
                # output_text = '\n'.join(output)
                # with open('bandwidth_output.txt', 'w') as file:
                #     file.write(output_text)
                # import subprocess
                # subprocess.Popen(['notepad.exe', 'bandwidth_output.txt'])
                #
                # output = t_public_ip
                # output_text = '\n'.join(output)
                # with open('bandwidth_output.txt', 'w') as file:
                #     file.write(output_text)
                # import subprocess
                # subprocess.Popen(['notepad.exe', 'bandwidth_output.txt'])
                #
                # output = t_received
                # output_text = '\n'.join(output)
                # with open('bandwidth_output.txt', 'w') as file:
                #     file.write(output_text)
                # import subprocess
                # subprocess.Popen(['notepad.exe', 'bandwidth_output.txt'])
                #
                # output = t_transmitted
                # output_text = '\n'.join(output)
                # with open('bandwidth_output.txt', 'w') as file:
                #     file.write(output_text)
                # import subprocess
                # subprocess.Popen(['notepad.exe', 'bandwidth_output.txt'])
                #
                # output = t_total
                # output_text = '\n'.join(output)
                # with open('bandwidth_output.txt', 'w') as file:
                #     file.write(output_text)
                #
                # import subprocess
                # subprocess.Popen(['notepad.exe', 'bandwidth_output.txt'])






        # output_text_label = ['\t'.join(map(str, sublist)) for sublist in t_label]
        # output_text_public = ['\t'.join(map(str, sublist)) for sublist in t_public_ip]
        # output_text_received = ['\t'.join(map(str, sublist)) for sublist in r_sizes_in_bytes]
        # output_text_transmitted = ['\t'.join(map(str, sublist)) for sublist in tr_sizes_in_bytes]
        # output_text_total = ['\t'.join(map(str, sublist)) for sublist in to_sizes_in_bytes]
        # # output_text = ['\t'.join(map(str, sublist)) for sublist in total_tr]
        #     # Write the output to a temporary text file
        # with open('band_width_output.txt', 'w') as file:
        #     file.write('\n'.join(output_text_label))
        #     file.write('\n'.join(output_text_public))
        #     file.write('\n'.join(output_text_received))
        #     file.write('\n'.join(output_text_transmitted))
        #     file.write('\n'.join(output_text_total))
        #
        # subprocess.Popen(['notepad.exe', 'band_width_output.txt'])



        # sizes = t_received
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
        # received_data = r_converted_sizes
        # print("received data:", received_data)

        # sizes = t_transmitted
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
        #         print("transmit data:", size)
        # transmitted_data = t_converted_sizes
        # print("transmitted data:", transmitted_data)
        #
        # # total_r_s = sum(transmitted_data + received_data)
        # # print("Total matches the sum of received and transmitted data:", total_r_s)
        #
        # sizes = t_total
        # total_converted_sizes = []
        # for size in sizes:
        #     parts = size.split()
        #     if len(parts) == 2:
        #         value, unit = parts
        #         if unit == 'Bytes':
        #             total_converted_sizes.append(float(value) / 1024)
        #         elif unit == 'KB':
        #             total_converted_sizes.append(float(value))
        #         elif unit == 'MB':
        #             total_converted_sizes.append(float(value) * 1024)
        #         elif unit == "GB":
        #             total_converted_sizes.append(float(value) * 1024 * 1024 * 1024)
        #     else:
        #         print("total data:", size)
        # total_data = total_converted_sizes
        # print("total data:", total_data)
        #
        # if len(received_data) != len(transmitted_data):
        #     print("Error: Lists have different lengths.")
        # else:
        #     # Iterate over the indices and print each index value along with its sum
        #     for i in range(len(received_data)):
        #         print("Index:", i)
        #         print("Received:", received_data[i])
        #         print("Transmitted:", transmitted_data[i])
        #         print("total data:", total_data[i])
        #         print("Total:", received_data[i] + transmitted_data[i])
        #         print()










        #     if len(cells) >= 5:
        #         received_text = cells[2].text
        #         transmitted_text = cells[3].text
        #         total_text = cells[4].text
        #         print("received text:",received_text)
        #         print("transmitted text is:",transmitted_text)
        #         print("total text is:", total_text)
        #         # received_data = float(received_text.split()[0])  # Extract numeric value and convert to float
        #         # transmitted_data = float(transmitted_text.split()[0])
        #         # total_data = float(total_text.split()[0])
        #         # total_received += received_data
        #         # total_transmitted += transmitted_data
        #         # total_total += total_data
        #
        # print("received data:",total_received)
        # print("transmitted data is:",total_transmitted)
        # print("total data is:", total_total)
        # received_data_and_transmitted_data = total_received + total_transmitted
        # print("sum of received and transmitted data:", received_data_and_transmitted_data)
        # # total_received_expected = float(row[-1].find_elements(By.TAG_NAME, "td")[2].text.split()[0])
        # # total_transmitted_expected = float(row[-1].find_elements(By.TAG_NAME, "td")[3].text.split()[0])
        # # total_total_expected = float(row[-1].find_elements(By.TAG_NAME, "td")[4].text.split()[0])
        # # print(total_received_expected)
        # # print(total_transmitted_expected)
        # # print(total_total_expected)
        # if received_data_and_transmitted_data == total_total:
        #     print("Total matches the sum of received and transmitted data.")
        # else:
        #     print("Total does not match the sum of received and transmitted data.")

                # cells = row.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td[" + str(r) + "]")
            # self.driver.close()





    # def band_table_data(self):
    #     table = self.driver.find_element(By.XPATH, "//table[@class='MuiTable-root css-s064k4']")
    #     # tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
    #     # data = []
    #     # for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
    #     #     row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
    #     #     data.append(row)
    #     #     print("    |    ".join(data))
    #     # print(data)
    #
    #     for row_data in table:
    #         print("    |    ".join(str(cell) for cell in row_data))




    def table_row(self):
        table_row = self.driver.find_elements(By.XPATH, "//table[@class='MuiTable-root css-s064k4']/tbody/tr")
        l=[]
        for i in range(1, len(table_row)+1):
            row = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr[" + str(i) + "]/descendant::td)").text
            l.append(row)
        print(l)










    def total_table_data_for_single_row(self):
        # data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
        r = []
        t = []
        match = []
        t_data = []
        # for i in range(1, len(data) + 1):
        received = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[3])").text
        transmitted = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[4])").text
        total = self.driver.find_element(By.XPATH, "(//table[@class='MuiTable-root css-s064k4']/tbody/tr[1]/descendant::td[5])").text
                # s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])[" + str(i) + "]").text
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
        print("total:",total)
        if total_data == total:
            print("Total data meets the condition")
        else:
            print("Total data does not meet the condition")



















































# import time
#
# from selenium.webdriver import ActionChains
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.action_chains import ActionChains
#
# class Bandwidth:
#
#     def __init__(self,driver):
#         self.driver = driver
#
#     report_button_xpath = "(//div[@class='MuiBox-root css-84nudp'])[4]"
#     bandwidth_button_xpath = "(//div[text()='Bandwidth'])"
#
#     verify_reports_page = "//*[text()='Reports']"
#
#     verify_bandwidth_page_xpath = "//*[text()='Bandwidth | All IP']"
#
#     bandwidth_data_from_input_xpath = "(//input[contains(@aria-invalid,'false')])[3]"
#     bandwidth_data_to_input_xpath = "(//input[contains(@aria-invalid,'false')])[4]"
#
#     submit_button_xpath = "//button[text()='Submit']"
#
#     received_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])"
#
#     transmitted_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])"
#
#     total_data_xpath = "(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[5])"
#
#     def bandwidth_table_data(self):
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
#     def bandwidth_from_date(self,from_date):
#         self.driver.find_element(By.XPATH, self.bandwidth_data_from_input_xpath).click()
#         self.driver.find_element(By.XPATH, self.bandwidth_data_from_input_xpath).clear()
#         self.driver.find_element(By.XPATH, self.bandwidth_data_from_input_xpath).send_keys(from_date)
#
#     def bandwidth_to_date(self,to_date):
#         self.driver.find_element(By.XPATH, self.bandwidth_data_to_input_xpath).click()
#         self.driver.find_element(By.XPATH, self.bandwidth_data_to_input_xpath).clear()
#         self.driver.find_element(By.XPATH, self.bandwidth_data_to_input_xpath).send_keys(to_date)
#
#     def verify_bandwidth_page(self):
#         return self.driver.find_element(By.XPATH, self.verify_bandwidth_page_xpath).text
#
#     def verify_reports(self):
#         return self.driver.find_element(By.XPATH, self.verify_reports_page).text
#
#
#
#     def report_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#         time.sleep(5)
#
#     def bandwidth_page(self):
#         self.driver.find_element(By.XPATH, self.report_button_xpath).click()
#         time.sleep(5)
#
#         element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.bandwidth_button_xpath)))
#         element.click()
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
#
#         dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
#         print(len(dates))
#
#         for ele in dates:
#             print(ele.text)
#             if ele.text == "1":
#                 ele.click()
#                 break
#
#         # before_minute = self.driver.find_element(By.XPATH, "(//span[contains(@class,'MuiSlider-thumb MuiSlider-thumbSizeSmall MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeSmall MuiSlider-thumbColorPrimary css-1rw23sq')])[1]")
#         # after_minute = self.driver.find_element(By.XPATH, "(//input[contains(@aria-orientation,'horizontal')])[1]")
#         # actions = ActionChains(self.driver)
#         # actions.drag_and_drop(before_minute, after_minute).perform()
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
#
#         dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
#         print(len(dates))
#         for ele in dates:
#             if ele.text == "3":
#                 ele.click()
#                 break
#
#     def bandwidth_table_received_data(self):
#         data = self.driver.find_elements(By.XPATH, self.received_data_xpath)
#         l = []
#         a = self.driver.find_element(By.XPATH, self.received_data_xpath).text
#         print(a)
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[3])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#         # str1 = l.split(" ")
#         # b = [int(a) for a in words if a.isdigit]
#         # print(b)
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         print(numbers)
#
#         print(l)
#
#         sizes = l
#         # Convert each size to GB
#         sizes_in_gb = []
#         for size in sizes:
#             value, unit = size.split()
#             value = float(value)
#             if unit == 'MB':
#                 value /= 1024  # Convert MB to GB
#             sizes_in_gb.append(value)
#
#         print(sizes_in_gb)
#         print(sum(sizes_in_gb))
#
#         # print(sum(numbers))
#         print("success")
#
#
#     def bandwidth_table_transmitted_data(self):
#         data = self.driver.find_elements(By.XPATH, self.transmitted_data_xpath)
#         l = []
#         a = self.driver.find_element(By.XPATH, self.transmitted_data_xpath).text
#         print(a)
#         for i in range(1, len(data) + 1):
#             s = self.driver.find_element(By.XPATH,"(//*[contains(@class,'MuiTable-root css-s064k4')]/tbody/tr/descendant::td[4])[" + str(i) + "]").text
#             l.append(s)
#         str1 = " ".join(l)
#         words = str1.split(" ")
#
#         numbers = [float(a) for a in words if a.replace('.', '').isdigit()]
#         print(numbers)
#
#         print(l)
#
#         sizes = l
#         # Convert each size to GB
#         sizes_in_gb = []
#         for size in sizes:
#             value, unit = size.split()
#             value = float(value)
#             if unit == 'MB':
#                 value /= 1024  # Convert MB to GB
#             sizes_in_gb.append(value)
#
#         print(sizes_in_gb)
#         print(sum(sizes_in_gb))
#
#         # print(sum(numbers))
#         print("success")
#
#
#     def bandwidth_table_total_data(self):
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
#
#         sizes = l
#         # Convert each size to GB
#         sizes_in_gb = []
#         for size in sizes:
#             value, unit = size.split()
#             value = float(value)
#             if unit == 'MB':
#                 value /= 1024  # Convert MB to GB
#             sizes_in_gb.append(value)
#
#         print(sizes_in_gb)
#         print(sum(sizes_in_gb))
#
#         # print(sum(numbers))
#         print("success")
#
#     def verify_the_total_table_data(self):
#         data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
#         r = []
#         t = []
#         t_data = []
#         for i in range(1, len(data) + 1):
#             received = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr/descendant::td[3])[" + str(i) + "]").text
#             transmitted = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr/descendant::td[4])[" + str(i) + "]").text
#             total = self.driver.find_element(By.XPATH,"(//table[@class='MuiTable-root css-s064k4']/tbody/tr/descendant::td[5])[" + str(i) + "]").text
#             r.append(received)
#             t.append(transmitted)
#             t_data.append(total)
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
#         received_data = sum(r_converted_sizes)
#         print("received data:", received_data)
#
#         sizes = t
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
#         transmitted = sum(t_converted_sizes)
#         print("transmitted data:",transmitted)
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
#         total_data = sum(converted_sizes)
#         print("total data:", total_data)
#
#         total = received_data + transmitted
#         print("total:", total)
#         if total_data == total:
#             print("Total data meets the condition")
#         else:
#             print("Total data does not meet the condition")
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
#         print("total:",total)
#         if total_data == total:
#             print("Total data meets the condition")
#         else:
#             print("Total data does not meet the condition")
#
#
#
#
#
