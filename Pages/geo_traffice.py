import os
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
    verify_geo_traffic_page_xpath = "//*[contains(@class,'MuiBox-root css-1c1kq07')]/p"

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


    def rows_per_page(self):
        self.driver.find_element(By.XPATH, self.rows_per_page_xpath).click()

    def rows_per_page_dropdown(self):
        list = self.driver.find_elements(By.XPATH, self.rows_per_page_dropdown_xpath)
        print(list)
        for i in list:
            if i.text == '100':
                i.click()
                break

    def table_title(self):
        title = self.driver.find_element(By.XPATH, self.table_title_xpath).text
        print("title of the table:", title)

    def summary_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end=' ')

    def ip_tracking_table_data(self):
        tbody = self.driver.find_element(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table")
        data = []
        for tr in tbody.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//tr"):
            row = [item.text for item in tr.find_elements(By.XPATH, "//*[@class='MuiBox-root css-1fpff4c']/table//td")]
            data.append(row)
        print(data, end=' ')

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
            if ele.text == "5":
                ele.click()
                break

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