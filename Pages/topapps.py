import os
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
        print(total)
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
            if ele.text == "3":
                ele.click()
                break


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
