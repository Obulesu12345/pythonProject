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

    def bandwidth_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end=' ')

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
        # mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        # print(mon_yy)
        # while True:
        #     if mon_yy == "April 2024":
        #         break
        #     else:
        #         self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()
        #
        # dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
        # print(len(dates))
        #
        # for ele in dates:
        #     print(ele.text)
        #     if ele.text == "1":
        #         ele.click()
        #         break

        before_minute = self.driver.find_element(By.XPATH, "(//span[contains(@class,'MuiSlider-thumb MuiSlider-thumbSizeSmall MuiSlider-thumbColorPrimary MuiSlider-thumb MuiSlider-thumbSizeSmall MuiSlider-thumbColorPrimary css-1rw23sq')])[1]")
        after_minute = self.driver.find_element(By.XPATH, "(//input[contains(@aria-orientation,'horizontal')])[1]")
        actions = ActionChains(self.driver)
        actions.drag_and_drop(before_minute, after_minute).perform()

    def to_date(self):
        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[4]")
        element.click()
        mon_yy = self.driver.find_element(By.XPATH, "//div[@class='MuiPickersFadeTransitionGroup-root css-1bx5ylf']").text
        print(mon_yy)
        while True:
            if mon_yy == "April 2024":
                break
            else:
                self.driver.find_element(By.XPATH, "//button[contains(@title,'Previous month')]").click()

        dates = self.driver.find_elements(By.XPATH, "//button[contains(@role,'gridcell')]")
        print(len(dates))

        for ele in dates:
            print(ele.text)
            if ele.text == "2":
                ele.click()
                break

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

































    def total_table_data_for_single_row(self):
        # data = self.driver.find_elements(By.XPATH, self.total_data_xpath)
        r = []
        t = []
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





