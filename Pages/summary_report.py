import os
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

    external_communication_table_received_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[3]"
    external_communication_table_transmitted_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[4]"
    external_communication_table_total_data_xpath = "//*[contains(@class,'MuiBox-root css-1xaekgw')]/div[2]//table/tbody/tr/descendant::td[5]"

    apps_table_received_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[4])"
    apps_table_transmitted_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[5])"
    apps_table_total_data_xpath = "(//*[@class='MuiBox-root css-1xaekgw']/div[3]//table/tbody/tr/descendant::td[6])"

    city_wise_traffic_table_xpath = "//*[contains(@class,'MuiBox-root css-14w0bz')]/div"
    # city_wise_traffic_table_xpath = "//p[text()='No Data']"

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

    def table_title(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        print("title of the table:", title)
        title_head = self.driver.find_element(By.XPATH, "(//*[@class='MuiBox-root css-1fpff4c']/table/thead)[1]").text
        print(title_head)

    def summary_table_data(self):
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
