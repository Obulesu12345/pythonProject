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

        print(converted_sizes)
        total_data = sum(converted_sizes)
        print(total_data)

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
        print(converted_sizes)
        transmitted_data = sum(converted_sizes)
        print(transmitted_data)

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
        print(converted_sizes)
        received_data = sum(converted_sizes)
        print(received_data)

        total = received_data + transmitted_data
        print(total)
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
            if ele.text == "103.174.106.87":
                ele.click()
                break
    def from_date(self):
        element = self.driver.find_element(By.XPATH, "(//input[contains(@aria-invalid,'false')])[3]")
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
            if ele.text == "1":
                ele.click()
                break


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
